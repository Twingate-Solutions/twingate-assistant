# CLAUDE.md — twingate-assistant

## What This Project Is

A public Claude Code plugin that turns Claude Code into a Twingate implementation specialist. Customers install the plugin and their sessions gain deep ZTNA domain expertise — architecture knowledge, deployment playbooks, IaC generation, troubleshooting, and current documentation awareness. The plugin contains 10 skills (domain expertise modules), 6 agents (orchestrating subagents), reference files (auto-updated doc summaries), and Python scripts for a GitHub Action that refreshes doc summaries weekly via the Claude API. Hosted at `Twingate-Solutions` org, Apache 2.0 license.

## Architecture

```
twingate-assistant/
├── .claude-plugin/
│   └── plugin.json                     # Plugin manifest
├── skills/                             # 10 domain expertise skills
│   ├── twingate-architect/             # Core ZTNA architecture & design
│   │   ├── SKILL.md                    # Evergreen knowledge + instructions
│   │   └── references/                 # Auto-generated doc summaries
│   ├── twingate-connectors/            # Connector deployment across platforms
│   ├── twingate-terraform/             # Terraform provider usage
│   ├── twingate-pulumi/                # Pulumi provider
│   ├── twingate-kubernetes/            # K8s operator, Helm, routing
│   ├── twingate-idfw/                  # Identity Firewall (SSH, K8s gateway)
│   ├── twingate-identity/              # IdP, SCIM, policies, device trust
│   ├── twingate-api/                   # GraphQL API & automation
│   ├── twingate-dns-security/          # DNS filtering, exit networks
│   └── twingate-troubleshoot/          # Diagnostics decision tree
├── agents/                             # 6 orchestrating subagents
│   ├── twingate-se.md                  # Senior SE — primary orchestrator
│   ├── aws-deployer.md                 # AWS-specific guidance
│   ├── azure-deployer.md               # Azure-specific guidance
│   ├── gcp-deployer.md                 # GCP-specific guidance
│   ├── network-designer.md             # Topology & resource planning
│   └── idfw-deployer.md                # Identity Firewall setup
├── scripts/                            # Auto-update pipeline
│   ├── update_references.py            # Orchestrator (sitemaps + GitHub source)
│   ├── fetch_sitemap.py                # Sitemap XML parser (multi-source: docs + help)
│   ├── summarize_docs.py               # Claude API summarizer + frontmatter builder
│   ├── diff_docs.py                    # New/removed doc detection
│   ├── github_repos.py                 # GitHub org/repo/wiki discovery, zero-LLM
│   ├── github_summarize.py             # GitHub delta/full summarization (LLM)
│   ├── pipeline_metrics.py             # Per-run token/time/cost metrics
│   ├── backfill_frontmatter.py         # One-time frontmatter backfill (dry-run default)
│   ├── doc_mapping.yaml                # Multi-source (sources:) + doc/repo → skill routing
│   └── requirements.txt
├── .github/workflows/
│   └── update-docs.yml                 # Weekly cron GH Action
├── docs/
│   ├── MAINTAINING.md                  # Pipeline maintenance guide
│   ├── twingate-context-template.md    # Schema for per-repo context files
│   └── metrics/                        # Committed per-run pipeline/GitHub metrics (.jsonl)
├── LICENSE                             # Apache 2.0
├── CONTRIBUTING.md
└── README.md
```

**Key architecture notes:**
- Skills contain evergreen knowledge (SKILL.md, hand-authored, never auto-updated) + dynamic references (references/, auto-generated weekly)
- Agents are lightweight subagent .md files that orchestrate skills for specific deployment scenarios
- The auto-update pipeline crawls two sitemaps (`www.twingate.com/docs`, `help.twingate.com`) plus GitHub repos/wikis across four Twingate orgs, summarizes via Claude API (Sonnet), and writes to references/ with source provenance frontmatter
- GitHub repos (Terraform provider, Helm charts, K8s operator, gateway) are referenced at runtime, not bundled — and also discovered/summarized directly by the pipeline (see `github_repos.py`)

## Tech Stack

| Concern | Choice |
|---|---|
| **Language** | Markdown (skills/agents), Python 3.12+ (scripts) |
| **HTTP client** | requests |
| **HTML parsing** | beautifulsoup4 + lxml |
| **AI API** | anthropic Python SDK (Sonnet for summarization) |
| **Config** | YAML (doc_mapping.yaml) |
| **Linting** | ruff |
| **Type checking** | mypy |
| **Testing** | pytest |
| **Packaging** | requirements.txt (scripts only — plugin itself is just files) |
| **CI** | GitHub Actions |

## Project Structure

```
twingate-assistant/
├── CLAUDE.md                           ← you are here
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── twingate-architect/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── twingate-connectors/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── twingate-terraform/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── twingate-pulumi/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── twingate-kubernetes/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── twingate-idfw/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── twingate-identity/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── twingate-api/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── graphql-schema-reference.md
│   ├── twingate-dns-security/
│   │   ├── SKILL.md
│   │   └── references/
│   └── twingate-troubleshoot/
│       ├── SKILL.md
│       └── references/
├── agents/
│   ├── twingate-se.md
│   ├── aws-deployer.md
│   ├── azure-deployer.md
│   ├── gcp-deployer.md
│   ├── network-designer.md
│   └── idfw-deployer.md
├── scripts/
│   ├── update_references.py
│   ├── fetch_sitemap.py
│   ├── summarize_docs.py
│   ├── diff_docs.py
│   ├── github_repos.py
│   ├── github_summarize.py
│   ├── pipeline_metrics.py
│   ├── backfill_frontmatter.py
│   ├── doc_mapping.yaml
│   ├── .repo_state.json          # per-repo GitHub state, generated at runtime
│   ├── requirements.txt
│   └── tests/
│       ├── test_fetch_sitemap.py
│       ├── test_diff_docs.py
│       ├── test_summarize_docs.py
│       ├── test_update_references.py
│       ├── test_frontmatter.py
│       ├── test_backfill_frontmatter.py
│       ├── test_github_repos.py
│       ├── test_github_summarize.py
│       └── test_pipeline_metrics.py
├── .github/
│   └── workflows/
│       └── update-docs.yml
└── docs/
    ├── MAINTAINING.md
    ├── twingate-context-template.md
    └── metrics/                   # pipeline-runs.jsonl, github-runs.jsonl
```

## Git Policy

**Claude Code must NEVER run any git commands.** No `git add`, `git commit`, `git push`, `git checkout`, `git stash`, or any other git operation. All version control is handled manually by the maintainer. When work is complete, prompt the user to review and commit.

## Code Style & Conventions

### SKILL.md Files

SKILL.md files follow the **identity format** — a lean document that answers: *Who are you? What decisions do you help with? What are your guidelines?* The authoritative source of technical facts is `references/`, not the skill body. Illustrative examples in the body (a short YAML/JSON/HCL/CLI snippet that shows the *shape* of a thing) are fine — they are examples, not the canonical spec, and the skill must still force a reference check (`## Search References First`) so exact values, current versions, and field names are read from `references/` rather than copied from the example.

**Length:** keep the *prose* lean (Role + Decisions & Guidelines ≈ 400 words). The `## References` routing table is navigation, not content, and is exempt — a skill owning 70–150 references legitimately runs 800–2000 words total. Never pad the prose; never truncate the routing table to hit a word count. **Every file in `references/` must be reachable from the routing table** — an unnamed reference is an invisible one.

**Required sections (in order):**

```markdown
---
name: twingate-{domain}
description: >
  {Pushy trigger description — aggressive claim of ownership. Use imperative:
  "Use when...", "Load when...", "Activate for..."}
---

## Role

One short paragraph. Who this skill is. What domain it owns. What problems it solves.
No technical facts — just identity and scope.

## Decisions & Guidelines

Bulleted list of opinionated guidelines this skill enforces. These are the things a
domain expert would say that are NOT derivable from reading a doc page — tradeoffs,
anti-patterns, default recommendations, when to escalate.

## Search References First

Mandate grepping `references/` with the user's own keywords BEFORE answering, with
2–3 concrete `grep -ril "{keyword}" references/` examples using strings verified to
actually appear in that skill's reference bodies. State that filenames reveal only the
topic — vendor names, tool names, error strings, and API details live in the bodies.
Include: "If the user asks whether tooling exists for X, **search before saying no.**"
(For twingate-troubleshoot, make this error-string-oriented: grep the user's literal
error text before theorizing.)

## Routing

When to hand off to another skill or agent. Keeps the skill from over-reaching.

- **→ twingate-{other}**: when X, Y, Z is the real question
- **→ twingate-troubleshoot**: when the user reports a symptom rather than a design question

## References

Open with the file-kind taxonomy (omit kinds the skill has none of):

- **`{slug}.md`** — summaries of `twingate.com/docs` pages.
- **`{numeric-id}-{slug}.md`** — Twingate help-center articles: symptom-shaped support
  content, exact error strings, per-OS gotchas.
- **`gh-{org}-{repo}.md`** / **`-wiki.md`** — public Twingate GitHub repos: SE/community
  tooling, reference implementations, providers, operators.

Then a `| If the user asks about… | Read first |` routing table covering EVERY file in
`references/`. Rules:

- **Each `gh-*` reference gets its own row**, bolding the distinguishing capability and
  naming the vendor/tool/platform keywords buried in its body (a filename scan misses
  them). Flag experimental / reference-only / archived repos as such rather than
  implying support.
- **Help articles may be grouped by symptom cluster**, but still name each file so all
  are reachable.
- Cross-skill references use the full path `skills/{other-skill}/references/{file}.md`.
- Close with a note that the table is a fast path, not the whole corpus, and to grep
  when a question matches no row.
```

**What does NOT belong in SKILL.md:**

- `## Evergreen Knowledge` sections — move genuine guidelines to `## Decisions & Guidelines`, delete pure technical facts
- `## Common Patterns` — delete if it's just doc regurgitation; keep only opinionated choices
- `## Anti-Patterns` — fold into `## Decisions & Guidelines` as negative guidelines
- Long bullet lists explaining how the product works — that's what `references/` is for

**Illustrative examples are allowed.** A short snippet (YAML, JSON, HCL, a CLI invocation) used to show the *shape* of a config or command is fine in the body. What's disallowed is the body becoming the authoritative, exhaustive spec — long fact dumps, full option catalogs, or values a reader would copy verbatim without checking. The test: an example that says "roughly like this, verify the specifics in `references/`" stays; content that reads as "this is the complete, current, only way" moves to `references/`. The `## Search References First` mandate must remain intact regardless.

**Other conventions:**

- Description must be "pushy" — aggressively claim trigger conditions per Anthropic guidance
- Reference files using relative paths: `[guide](./references/file.md)`
- Use imperative form in guidelines

### Agent .md Files
- YAML frontmatter with `name`, `description`, `tools`, and `skills` fields
- Body contains the system prompt — role definition, workflow, guardrails
- Agents orchestrate; skills hold the authoritative detail. Illustrative examples (a sample task definition, an NSG/firewall rule, an IdP setup outline, a config snippet) are acceptable in an agent body to make guidance concrete — provided the agent still forces a reference check (`## When to Verify` / `## Search References First`) and cites the owning skill's reference for exact values. Do not turn an agent into a second copy of a skill's reference corpus.

### Python Scripts (auto-update pipeline)
- Python 3.12+ — modern type hints (`str | None`), match statements
- Minimal dependencies: requests, beautifulsoup4, anthropic, pyyaml, lxml
- Type hints on every function signature
- Docstrings on every public function
- `if __name__ == "__main__"` guard on every script

### General
- No secrets in any file — API keys go in GH Action secrets or env vars
- UTF-8 encoding, LF line endings

## Key Design Rules (Non-Negotiable)

1. **Evergreen knowledge is hand-authored and never auto-overwritten.** The pipeline only writes to `references/` directories.
2. **Skills are expertise, agents are orchestrators.** Agents route to skills for authoritative implementation detail; a skill's `references/` remains the single source of truth. Illustrative examples in an agent body (a sample snippet showing the shape of a config or command) are permitted — what's prohibited is an agent becoming a parallel copy of a skill's reference corpus, or presenting inline content as the authoritative spec. The agent must always force a reference check (`## When to Verify` / `## Search References First`) and cite the owning skill's reference for exact values.
3. **Descriptions must be pushy.** Aggressively claim trigger conditions per Anthropic guidance.
4. **GitHub repos are referenced, not bundled.** Skills instruct CC to clone/inspect at runtime.
5. **Two sitemaps plus the GitHub API are the sources of truth for discovery.** `doc_mapping.yaml`'s `sources:` list declares both sitemaps (`www.twingate.com/docs`, `help.twingate.com`); sitemap diff catches new pages on either. GitHub repos are discovered independently — live, on every run — across the four Twingate orgs via the GitHub API (`github_repos.discover_org_repos`), not via a static list; `doc_mapping.yaml`'s `repos:` section only routes a discovered repo to a skill.
6. **GraphQL SDL ships statically.** Hand-maintained in `twingate-api`.
7. **No MCP server, no live API calls.** Plugin provides expertise and generates code only.
8. **twingate-se agent always starts with environment assessment.**
9. **Identity Firewall skill is expansion-ready.** SSH PAM + K8s gateway today, structured for future protocols.
10. **Auto-update pipeline is idempotent.** No commits when nothing changes.

## Plugin Manifest Quick Reference

```json
{
  "name": "twingate-assistant",
  "description": "Twingate ZTNA implementation assistant — architecture, deployment, IaC, troubleshooting",
  "version": "1.0.0",
  "author": { "name": "Twingate Solutions Engineering" },
  "repository": "https://github.com/Twingate-Solutions/twingate-assistant",
  "license": "Apache-2.0"
}
```

## Skill Quick Reference

| Skill | Docs Owned | Key Topics |
|---|---|---|
| twingate-architect | ~15 | Architecture, how it works, DNS, P2P, encryption, use cases |
| twingate-connectors | ~20 | Deployment (all platforms), upgrades, metrics, logging, HA |
| twingate-terraform | ~3+repo | Provider resources, SE reference modules |
| twingate-pulumi | ~2+repo | Pulumi provider, reference scripts |
| twingate-kubernetes | ~7+repos | Helm chart, operator, CRDs, routing, kubectl |
| twingate-idfw | ~8+repo | SSH PAM, K8s gateway, session recording, Ansible, IDFW TF |
| twingate-identity | ~18 | IdP configs, SCIM, security policies, device trust, groups, JIT |
| twingate-api | ~6+SDL | GraphQL API, CLI tools, schema, Twingate Labs |
| twingate-dns-security | ~7 | DNS filtering, exit networks, DoH, browser security |
| twingate-troubleshoot | ~6 | Failure diagnostics: device, DNS, connector, firewall |

## Agent Quick Reference

| Agent | Role | Skills Preloaded |
|---|---|---|
| twingate-se | Senior SE orchestrator, environment assessment | all |
| aws-deployer | AWS deployment specialist | architect, connectors, terraform |
| azure-deployer | Azure deployment specialist | architect, connectors, terraform |
| gcp-deployer | GCP deployment specialist | architect, connectors, terraform |
| network-designer | Remote network topology planner | architect, connectors, identity |
| idfw-deployer | Identity Firewall implementation | idfw, kubernetes, terraform |

## Toolchain (Local Only)

ruff, mypy, and pytest are local development tools — **they are not published in the GitHub Action or any committed workflow.** Run them locally when building out Python scripts to validate correctness before committing, but do not add lint/type/test gates to `.github/workflows/`.

To run locally during development:

```bash
.venv/Scripts/ruff check scripts/
.venv/Scripts/mypy scripts/ --ignore-missing-imports
.venv/Scripts/pytest scripts/tests/
```
