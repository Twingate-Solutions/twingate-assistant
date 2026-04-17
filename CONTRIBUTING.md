# Contributing to twingate-assistant

Thanks for contributing. This document covers all contribution paths: adding or updating skills, updating evergreen guidelines, extending the doc mapping, running the auto-update pipeline locally, and submitting PRs.

---

## Contribution Paths

| What you want to do | Where to look |
| --- | --- |
| Fix or improve a skill's guidelines | [Updating evergreen knowledge](#updating-evergreen-knowledge) |
| Add a new skill | [Adding a new skill](#adding-a-new-skill) |
| Add or fix a doc URL mapping | [Extending the doc mapping](#extending-the-doc-mapping) |
| Refresh reference files from live docs | [Running the pipeline locally](#running-the-pipeline-locally) |
| Add or improve an agent | [Updating agents](#updating-agents) |
| Fix a bug in the pipeline scripts | [Pipeline scripts](#pipeline-scripts) |

---

## Updating Evergreen Knowledge

Each skill's `SKILL.md` contains hand-authored guidelines that the auto-update pipeline never touches. This is the right place to add:

- Opinionated recommendations a domain expert would make
- Anti-patterns and common mistakes
- Non-obvious routing decisions (when to use this skill vs. another)

**What does NOT belong in `SKILL.md`:**

- Technical facts (configuration values, command syntax, API field names) — these belong in `references/`
- Step-by-step procedures — these belong in `references/`
- Product descriptions — these belong in `references/`

The identity format for `SKILL.md` has exactly four sections:

1. `## Role` — one paragraph, who this skill is and what it owns
2. `## Decisions & Guidelines` — opinionated bullet list
3. `## Routing` — when to hand off to another skill or agent
4. `## References` — pointer to `references/`; key file names listed

Target: under 400 words in the body (the `twingate-troubleshoot` skill is an approved exception due to its decision tree).

---

## Adding a New Skill

1. Create a directory under `skills/`: `skills/twingate-{domain}/`
2. Create `skills/twingate-{domain}/SKILL.md` using the identity format above
3. Create `skills/twingate-{domain}/references/` with at least one placeholder file (use the `<!-- initial seed -->` convention until the pipeline generates real content)
4. Add the new skill to `scripts/doc_mapping.yaml` — map the relevant doc URLs to it
5. Add the skill name to any agent `skills:` frontmatter that should have access to it
6. Update the plugin description in `.claude-plugin/plugin.json` if the new domain adds meaningful trigger keywords

The `description:` field in the skill frontmatter is the most important part for discoverability — write it in imperative trigger language: "Use when...", "Load when...", "Activate for...". Be aggressive in claiming trigger conditions. See the existing skills for examples.

---

## Extending the Doc Mapping

`scripts/doc_mapping.yaml` routes documentation URLs to skills. The pipeline uses this to know where to write each reference summary.

Structure of an entry:

```yaml
- url: https://www.twingate.com/docs/some-feature
  skill: twingate-{domain}
  keywords:
    - keyword1
    - keyword2
```

To add a new mapping:

1. Find the canonical URL for the doc page (use the live Twingate docs site)
2. Identify the correct skill (see the Skill Quick Reference in `CLAUDE.md`)
3. Add the entry to `doc_mapping.yaml`
4. Run `python scripts/test_pipeline.py --url <your-url>` to verify it picks up and routes correctly (no API key needed)

The pipeline also auto-discovers new docs via sitemap diff. Any URL not in `doc_mapping.yaml` is routed to the `_triage/` directory for manual review and subsequent mapping.

---

## Running the Pipeline Locally

### Without an API key (recommended for testing)

`scripts/test_pipeline.py` runs every pipeline step and lets you test individual docs without an Anthropic API key. It uses the Claude Code CLI (`claude --print`) as the summarization engine.

```bash
cd scripts
pip install -r requirements.txt

# Fetch sitemap, diff against doc_mapping.yaml, extract text, and print what would be sent to Claude:
python test_pipeline.py

# Test a specific URL:
python test_pipeline.py --url https://www.twingate.com/docs/how-twingate-works

# End-to-end: fetch, summarize via Claude Code CLI, and write the reference file (no API key needed):
python test_pipeline.py --claude-code --url https://www.twingate.com/docs/how-twingate-works

# Process N docs in sequence from the mapping:
python test_pipeline.py --claude-code --count 3
```

The `--claude-code` mode requires an active Claude Code CLI session but no `ANTHROPIC_API_KEY`.

### With an Anthropic API key (production pipeline)

```bash
cd scripts
pip install -r requirements.txt

# Set your API key
export ANTHROPIC_API_KEY=your_key_here   # Linux/macOS
# $Env:ANTHROPIC_API_KEY="your_key_here"  # Windows PowerShell

# Run the full pipeline (writes to skills/*/references/)
python update_references.py

# Or test individual components:
python fetch_sitemap.py          # Fetches and prints sitemap URLs
python diff_docs.py              # Diffs sitemap against doc_mapping.yaml
```

The pipeline is idempotent — it skips pages whose content hasn't changed since the last run (hash-checked). On first run, it will fetch and summarize all mapped docs. Subsequent runs only update changed pages.

**Cost note:** Each page summarization makes one Claude API call (~500 tokens output). With ~286 mapped docs, a first-run full seed costs roughly $0.50–1.00. Steady-state weekly runs process only the 6–10 pages that typically change, keeping incremental cost under $0.05.

### Running tests

```bash
pytest scripts/tests/ -q
```

All HTTP and Claude API calls are mocked in the test suite — no network access or API key required to run tests.

### Linting and type checking

```bash
ruff check scripts/
mypy scripts/ --ignore-missing-imports
```

All three (tests, ruff, mypy) must be clean before submitting a PR that changes Python code.

---

## Updating Agents

Agents live in `agents/*.md` and are orchestrating subagents — they combine multiple skills for end-to-end deployment workflows.

**Agent format:**

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

Guidelines for agent content:
- Agents may contain code examples, deployment sequences, and cloud-provider-specific patterns — unlike skills, they are execution-layer documents
- Do not duplicate skill guidelines in agents — reference the relevant skill instead
- The `skills:` frontmatter list determines which skill files are loaded when the agent is invoked — include every skill the agent's workflow touches
- Verify every skill name in `skills:` matches an actual directory under `skills/`

---

## Pipeline Scripts

The four pipeline scripts in `scripts/` follow these conventions:

- Python 3.12+ — modern type hints, no `Optional[X]` (use `X | None`)
- Type hints on every function signature
- Docstrings on every public function
- `if __name__ == "__main__"` guard on every script
- No hardcoded secrets — API keys via environment variables only
- `requests` for HTTP (not `httpx`, not `aiohttp`)

Tests live in `scripts/tests/`. The test suite uses `unittest.mock` to mock all HTTP and API calls. Add tests for any new public function.

---

## Pull Request Checklist

Before opening a PR:

- [ ] All CI checks pass: `pytest scripts/tests/ -q`, `ruff check scripts/`, `mypy scripts/ --ignore-missing-imports`
- [ ] If you changed a `SKILL.md`: it follows the identity format (4 sections, under 400 words, no technical facts)
- [ ] If you added a skill: `doc_mapping.yaml` has entries for its docs; `references/` has at least one file
- [ ] If you changed `doc_mapping.yaml`: you ran the pipeline locally to verify routing
- [ ] If you changed an agent: `skills:` frontmatter is accurate; skill names match actual directories
- [ ] No secrets, API keys, or real customer data in any file
- [ ] PR description explains what changed and why

---

## License

By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](LICENSE).
