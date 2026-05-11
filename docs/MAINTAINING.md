# Maintaining a fork of twingate-assistant

This document is for people who want to **fork the project and customize it** — change skill content, route different docs to different skills, run the auto-update pipeline against their own documentation site, or extend the plugin for a Twingate-adjacent product.

If you just want to install and use the upstream plugin, see the [README](../README.md). If you want to contribute back upstream, see [CONTRIBUTING.md](../CONTRIBUTING.md) for SKILL.md conventions and the PR checklist.

---

## What this project actually is

A Claude Code plugin made up of:

- **Skills** — domain expertise modules (one per Twingate domain) that load automatically when relevant topics come up in a Claude Code session.
- **Agents** — orchestrating sub-agents that combine multiple skills for end-to-end deployment workflows.
- **Reference files** — auto-generated summaries of the live Twingate documentation, refreshed weekly by a GitHub Action.
- **Pipeline scripts** — Python scripts that fetch the docs sitemap, summarize changed pages via the Claude API, and write summaries to the right skill's `references/` directory.

The plugin is just files — no server, no MCP component, no live API calls at runtime. Everything ships as Markdown, YAML, and a handful of Python scripts that only run inside the GitHub Action.

---

## Architecture

```text
twingate-assistant/
├── .claude-plugin/
│   └── plugin.json               # Plugin manifest
├── skills/                       # 10 domain expertise skills
│   └── twingate-{domain}/
│       ├── SKILL.md              # Evergreen identity + guidelines (hand-authored)
│       └── references/           # Auto-generated doc summaries (pipeline-managed)
├── agents/                       # 6 orchestrating subagents
│   ├── twingate-se.md
│   ├── aws-deployer.md
│   ├── azure-deployer.md
│   ├── gcp-deployer.md
│   ├── network-designer.md
│   └── idfw-deployer.md
├── scripts/                      # Auto-update pipeline
│   ├── update_references.py     # Orchestrator
│   ├── fetch_sitemap.py         # Sitemap XML parser
│   ├── summarize_docs.py        # Claude API summarizer
│   ├── diff_docs.py             # New/removed doc detection
│   ├── doc_mapping.yaml         # Doc URL → skill routing
│   ├── test_pipeline.py         # Local test harness (no API key required)
│   └── requirements.txt
├── .github/workflows/
│   └── update-docs.yml          # Weekly cron GitHub Action
└── docs/
    ├── MAINTAINING.md           # ← this file
    └── twingate-context-template.md
```

### Design principles

1. **Evergreen knowledge is hand-authored and never overwritten.** SKILL.md files contain only identity, guidelines, and routing rules. The pipeline writes only to `references/`.
2. **Skills are expertise; agents are orchestrators.** Agents reference skills; they do not duplicate skill content.
3. **GitHub repos are referenced at runtime, not bundled.** Skills instruct Claude Code to clone or inspect external repos when needed.
4. **The sitemap is the source of truth for doc discovery.** `doc_mapping.yaml` routes known docs; the sitemap diff catches new ones.
5. **The pipeline is idempotent.** It commits nothing when nothing has changed.

---

## The auto-update pipeline

A weekly GitHub Action (`.github/workflows/update-docs.yml`) keeps every skill's `references/` directory current.

Each run:

1. Fetches the Twingate documentation sitemap.
2. Diffs it against the previous sitemap snapshot and `doc_mapping.yaml`.
3. For each new or changed doc, crawls the page and extracts the canonical text.
4. Summarizes the page via the Claude API (Sonnet model, ~500 output tokens).
5. Writes the summary to the appropriate skill's `references/` directory.
6. Opens a PR if anything changed; exits silently if nothing did.

Unmapped docs are routed to `_triage/` for manual review before being added to `doc_mapping.yaml`.

The pipeline requires one secret: `ANTHROPIC_API_KEY`. Set it as a repository secret in your fork.

### Running the pipeline locally

#### Without an API key (recommended for testing)

`scripts/test_pipeline.py` runs every pipeline step and uses the Claude Code CLI (`claude --print`) as the summarization engine instead of the Anthropic SDK — no API key needed.

```bash
cd scripts
pip install -r requirements.txt

# Fetch the sitemap, diff against doc_mapping.yaml, print what would be sent to Claude:
python test_pipeline.py

# Test a specific URL:
python test_pipeline.py --url https://www.twingate.com/docs/how-twingate-works

# End-to-end: summarize via Claude Code CLI and write the reference file:
python test_pipeline.py --claude-code --url https://www.twingate.com/docs/how-twingate-works

# Process N docs in sequence from the mapping:
python test_pipeline.py --claude-code --count 3
```

#### With an Anthropic API key (production pipeline)

```bash
cd scripts
pip install -r requirements.txt

export ANTHROPIC_API_KEY=your_key_here          # Linux/macOS
# $Env:ANTHROPIC_API_KEY = "your_key_here"      # Windows PowerShell

python update_references.py
```

Cost: each page summarization is ~500 output tokens. A full first-run seed (~286 docs) costs roughly $0.50–1.00. Steady-state weekly runs only re-summarize the 6–10 pages that typically change, keeping incremental cost under $0.05.

---

## Customizing your fork

### Change what a skill teaches

Edit the `SKILL.md` file directly. The pipeline never overwrites it. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the identity format if you're rewriting from scratch.

### Add a new skill

1. Create `skills/twingate-{domain}/SKILL.md` using the identity format.
2. Create `skills/twingate-{domain}/references/` with at least one placeholder file.
3. Add the new skill to `scripts/doc_mapping.yaml` mapping URLs to it.
4. Add the skill name to any agent `skills:` frontmatter that should preload it.

### Route different docs to different skills

Edit `scripts/doc_mapping.yaml`:

```yaml
- url: https://www.twingate.com/docs/some-feature
  skill: twingate-{domain}
  keywords:
    - keyword1
    - keyword2
```

After editing, verify routing with:

```bash
python scripts/test_pipeline.py --url https://www.twingate.com/docs/some-feature
```

### Point the pipeline at a different documentation site

If you're forking for a Twingate-adjacent product or a private documentation source:

1. Edit `scripts/fetch_sitemap.py` to point at your sitemap URL.
2. Replace `scripts/doc_mapping.yaml` with mappings appropriate to your docs.
3. Re-run `python scripts/update_references.py` (or wait for the weekly Action).

### Change the update cadence

Edit the `cron:` schedule in `.github/workflows/update-docs.yml`.

---

## Tests, linting, type checking

Local development tools only — not enforced in CI:

```bash
pytest scripts/tests/ -q
ruff check scripts/
mypy scripts/ --ignore-missing-imports
```

All HTTP and Claude API calls are mocked in the test suite, so tests run offline.

---

## License

Apache 2.0. Forks must preserve the [LICENSE](../LICENSE) file and attribution.
