# Skill Authoring Best Practices (Applied in This Package)

This package follows the current Agent Skills ecosystem guidance.

## References

- Agent Skills Specification: https://agentskills.io/specification
- Skill Creation Best Practices: https://agentskills.io/skill-creation/best-practices
- Optimizing Descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- Using Scripts: https://agentskills.io/skill-creation/using-scripts
- Client Showcase: https://agentskills.io/clients

---

## Practical Rules Used Here

1. **Trigger-first descriptions**
   - `description` focuses on “when to use”, not long technical prose.

2. **Clear skill boundaries**
   - single date → `huangli-query-by-date`
   - date range/multi-date → `huangli-query-batch`
   - keyword search over periods → `huangli-search-by-keyword`

3. **Prefer batch for ranges**
   - avoid repeated single-date calls when batch endpoint exists.

4. **Progressive disclosure**
   - keep `SKILL.md` concise; push implementation depth into scripts/docs.

5. **Deterministic interfaces**
   - explicit required env vars (`HUANGLI_TOKEN`, optional `HUANGLI_BASE`)
   - stable output fields and error semantics.

6. **Agent-friendly scripts**
   - small, composable CLIs
   - bounded ranges and chunking where needed
   - clear errors for `401/429/network`.

7. **Portability first**
   - no frontend/backend coupling
   - can be dropped into any client with `SKILL.md` support.
