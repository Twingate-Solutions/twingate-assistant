# Contributing to twingate-assistant

Thanks for contributing. This document covers contributing back upstream — fixing or extending skills, agents, or pipeline scripts in a way that benefits everyone using the plugin.

If you're customizing a fork for your own use, see [`docs/MAINTAINING.md`](docs/MAINTAINING.md) instead — it covers the project's architecture, the auto-update pipeline, and how to run things locally.

---

## Contribution paths

| What you want to do | Where to look |
| --- | --- |
| Fix or improve a skill's guidelines | [Updating a SKILL.md](#updating-a-skillmd) |
| Add a new skill | [Adding a new skill](#adding-a-new-skill) |
| Add or fix a doc URL mapping | [Updating doc mapping](#updating-doc-mapping) |
| Add or improve an agent | [Updating agents](#updating-agents) |
| Fix a bug in the pipeline scripts | [Pipeline scripts](#pipeline-scripts) |

For details on how the pipeline works or how to run it locally, see [`docs/MAINTAINING.md`](docs/MAINTAINING.md).

---

## Updating a SKILL.md

Each skill's `SKILL.md` contains hand-authored guidelines that the auto-update pipeline never touches. This is the right place to add:

- Opinionated recommendations a domain expert would make
- Anti-patterns and common mistakes
- Non-obvious routing decisions (when to use this skill vs. another)

**What does NOT belong in `SKILL.md`:**

- Technical facts (configuration values, command syntax, API field names) — these belong in `references/`
- Step-by-step procedures — these belong in `references/`
- Product descriptions — these belong in `references/`

The identity format has exactly four sections:

1. `## Role` — one paragraph, who this skill is and what it owns
2. `## Decisions & Guidelines` — opinionated bullet list
3. `## Routing` — when to hand off to another skill or agent
4. `## References` — pointer to `references/`; key file names listed

Target: under 400 words in the body. (`twingate-troubleshoot` is an approved exception due to its decision tree.)

---

## Adding a new skill

1. Create a directory under `skills/`: `skills/twingate-{domain}/`
2. Create `skills/twingate-{domain}/SKILL.md` using the identity format above
3. Create `skills/twingate-{domain}/references/` with at least one placeholder file
4. Add the new skill to `scripts/doc_mapping.yaml`
5. Add the skill name to any agent `skills:` frontmatter that should have access to it
6. Update the plugin description in `.claude-plugin/plugin.json` if the new domain adds meaningful trigger keywords

The `description:` field in the skill frontmatter is the most important part for discoverability — write it in imperative trigger language ("Use when...", "Load when...", "Activate for..."). Be aggressive in claiming trigger conditions.

---

## Updating doc mapping

`scripts/doc_mapping.yaml` routes documentation URLs to skills. Structure:

```yaml
- url: https://www.twingate.com/docs/some-feature
  skill: twingate-{domain}
  keywords:
    - keyword1
    - keyword2
```

To add a mapping, find the canonical URL on the live Twingate docs site, pick the correct skill, add the entry, and verify routing with:

```bash
python scripts/test_pipeline.py --url <your-url>
```

The pipeline auto-discovers new docs via sitemap diff. Any URL not in `doc_mapping.yaml` is routed to the `_triage/` directory for manual review.

---

## Updating agents

Agents live in `agents/*.md` and orchestrate multiple skills for end-to-end deployment workflows.

```yaml
---
name: agent-name
description: >
  Pushy description of when to invoke this agent.
tools: Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch
skills: twingate-{skill1}, twingate-{skill2}
---

## Role

...
```

Guidelines:

- Agents may contain code examples, deployment sequences, and cloud-provider-specific patterns. Unlike skills, they are execution-layer documents.
- Do not duplicate skill guidelines in agents — reference the relevant skill instead.
- The `skills:` frontmatter list determines which skill files are loaded when the agent is invoked — include every skill the agent's workflow touches.
- Every name in `skills:` must match an actual directory under `skills/`.

---

## Pipeline scripts

The pipeline scripts in `scripts/` follow these conventions:

- Python 3.12+ — modern type hints, no `Optional[X]` (use `X | None`)
- Type hints on every function signature
- Docstrings on every public function
- `if __name__ == "__main__"` guard on every script
- No hardcoded secrets — API keys via environment variables only
- `requests` for HTTP (not `httpx`, not `aiohttp`)

Tests live in `scripts/tests/` and use `unittest.mock` for all HTTP and API calls. Add tests for any new public function.

For details on running the pipeline locally (with or without an API key), see [`docs/MAINTAINING.md`](docs/MAINTAINING.md).

---

## Pull request checklist

Before opening a PR:

- [ ] Tests pass: `pytest scripts/tests/ -q`
- [ ] Lint passes: `ruff check scripts/`
- [ ] Types pass: `mypy scripts/ --ignore-missing-imports`
- [ ] Any changed `SKILL.md` follows the identity format (4 sections, under 400 words, no technical facts)
- [ ] Any new skill has `doc_mapping.yaml` entries and at least one `references/` file
- [ ] Any `doc_mapping.yaml` change has been verified by running the pipeline locally
- [ ] Any changed agent has accurate `skills:` frontmatter; skill names match actual directories
- [ ] No secrets, API keys, or real customer data in any file
- [ ] PR description explains what changed and why

---

## License

By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).
