#!/usr/bin/env python3
"""CLI device authorization helper for Huangli toolkit.

Usage:
    python auth.py login
    python auth.py register
    python auth.py status
    python auth.py login --print-shell
    python auth.py login --append-zshrc

Env vars:
    HUANGLI_BASE           Optional API base, default https://api.nongli.skill.4glz.com
    HUANGLI_TOKEN_FILE     Optional output path, default ~/.huangli_token.json
    HUANGLI_ENV_FILE       Optional shell env file, default ~/.huangli.env
"""
import json
import os
import sys
import time
import webbrowser
import urllib.request
import urllib.error

BASE = os.environ.get('HUANGLI_BASE', 'https://api.nongli.skill.4glz.com').rstrip('/')
TOKEN_FILE = os.path.expanduser(os.environ.get('HUANGLI_TOKEN_FILE', '~/.huangli_token.json'))
ENV_FILE = os.path.expanduser(os.environ.get('HUANGLI_ENV_FILE', '~/.huangli.env'))
ZSHRC_FILE = os.path.expanduser('~/.zshrc')


def post_json(url, payload):
    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=body, method='POST', headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as resp:
        return resp.getcode(), json.loads(resp.read())


def get_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as resp:
        return resp.getcode(), json.loads(resp.read())


def shell_quote(value):
    return value.replace("'", "'\"'\"'")


def shell_exports(access_token, base_url):
    return (
        f"export HUANGLI_TOKEN='{shell_quote(access_token)}'\n"
        f"export HUANGLI_BASE='{shell_quote(base_url)}'\n"
    )


def write_env_file(access_token, base_url):
    with open(ENV_FILE, 'w', encoding='utf-8') as f:
        f.write(shell_exports(access_token, base_url))


def append_to_zshrc():
    snippet = f"\n# Huangli CLI\n[ -f '{ENV_FILE}' ] && source '{ENV_FILE}'\n"
    existing = ''
    if os.path.exists(ZSHRC_FILE):
        with open(ZSHRC_FILE, 'r', encoding='utf-8') as f:
            existing = f.read()
    if f"source '{ENV_FILE}'" not in existing:
        with open(ZSHRC_FILE, 'a', encoding='utf-8') as f:
            f.write(snippet)
        return True
    return False


def load_saved_token():
    if not os.path.exists(TOKEN_FILE):
        return None
    try:
        with open(TOKEN_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        token = data.get('access_token')
        return data if token else None
    except Exception:
        return None


def show_status():
    print('=== Huangli CLI Status ===')
    print(f'API Base: {BASE}')
    print(f'Token file: {TOKEN_FILE} ({"exists" if os.path.exists(TOKEN_FILE) else "missing"})')
    print(f'Env file: {ENV_FILE} ({"exists" if os.path.exists(ENV_FILE) else "missing"})')
    print(f'Zshrc: {ZSHRC_FILE} ({"exists" if os.path.exists(ZSHRC_FILE) else "missing"})')

    saved = load_saved_token()
    env_token = os.environ.get('HUANGLI_TOKEN', '').strip()
    token = (saved or {}).get('access_token') or env_token
    if not token:
        print('Token status: missing')
        print('Hint: run `python huangli-toolkit/auth.py login` first.')
        return 1

    try:
        _, data = get_json(
            f'{BASE}/api/auth/verify',
            headers={'Authorization': f'Bearer {token}'}
        )
        print('Token status: valid')
        print(f"User: {data.get('username')} (id={data.get('user_id')})")
        print(f"Session type: {data.get('session_type')}")
        return 0
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f'Token status: invalid (HTTP {e.code})')
        if body:
            print(body)
        return 1
    except urllib.error.URLError as e:
        print(f'Network error: {e.reason}')
        return 1


def main():
    action = 'login'
    print_shell = '--print-shell' in sys.argv
    append_zshrc = '--append-zshrc' in sys.argv

    positional = [arg for arg in sys.argv[1:] if not arg.startswith('--')]
    if positional:
        action = positional[0].strip().lower()

    if action not in {'login', 'register', 'status'}:
        print('Usage: python auth.py [login|register|status] [--print-shell] [--append-zshrc]', file=sys.stderr)
        sys.exit(1)

    if action == 'status':
        sys.exit(show_status())

    try:
        _, start = post_json(f'{BASE}/api/auth/cli/device/start', {'action': action})
    except urllib.error.HTTPError as e:
        print(f'Error: HTTP {e.code} while starting device auth', file=sys.stderr)
        print(e.read().decode('utf-8', errors='replace'), file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f'Error: Cannot connect to {BASE}\n{e.reason}', file=sys.stderr)
        sys.exit(1)

    device_code = start['device_code']
    interval = int(start.get('interval', 5))
    verify_url = start['verification_uri_complete']
    user_code = start['user_code']

    print('\n=== Huangli CLI Authorization ===')
    print(f'Action: {action}')
    print(f'User code: {user_code}')
    print(f'Open this URL in your browser:\n{verify_url}\n')

    try:
        webbrowser.open(verify_url)
        print('Browser opened automatically. If not, copy the URL above.\n')
    except Exception:
        pass

    while True:
        time.sleep(interval)
        try:
            status, data = post_json(f'{BASE}/api/auth/cli/device/poll', {'device_code': device_code})
            _ = status
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='replace')
            try:
                data = json.loads(body)
            except Exception:
                data = {'error': body or f'HTTP {e.code}'}

            if e.code == 428 and data.get('error') == 'authorization_pending':
                print('Waiting for browser authorization...')
                interval = int(data.get('interval', interval))
                continue
            if e.code == 429 and data.get('error') == 'slow_down':
                interval = int(data.get('interval', interval))
                print(f'Slow down requested. Polling every {interval}s...')
                continue
            print(f"Authorization failed: {data.get('message') or data.get('error')}", file=sys.stderr)
            sys.exit(1)
        except urllib.error.URLError as e:
            print(f'Network error: {e.reason}', file=sys.stderr)
            sys.exit(1)

        with open(TOKEN_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        write_env_file(data['access_token'], BASE)
        zshrc_updated = append_to_zshrc() if append_zshrc else False
        exports = shell_exports(data['access_token'], BASE).strip()

        print('Authorization successful.')
        print(f'Tokens saved to: {TOKEN_FILE}')
        print(f'Shell env saved to: {ENV_FILE}')
        if append_zshrc:
            print('Updated ~/.zshrc to source ~/.huangli.env' if zshrc_updated else '~/.zshrc already sources ~/.huangli.env')
        print(f"\nsource '{ENV_FILE}'")
        if print_shell:
            print('\n# shell exports')
            print(exports)
        else:
            print(f"export HUANGLI_TOKEN='{data['access_token']}'")
            print(f"export HUANGLI_BASE='{BASE}'")
        print('\nNote: logout and device unbinding must be done from the web dashboard for security.')
        break


if __name__ == '__main__':
    main()
