# Pending: Identity Firewall → Privileged Access Management (PAM) rename

Status: **waiting** on Twingate docs/pricing rename. Delete this file once the rename lands.

## Trigger

The first weekly `docs/weekly-update` PR whose diff shows the IDFW pages renamed (new URLs, or
"Identity Firewall" replaced by "Privileged Access Management"/"PAM" in summaries). Pull that PR
branch locally, do everything below on it, commit to the PR, then merge.

## Footprint (measured 2026-11-09)

~227 mentions of `Identity Firewall` / `IDFW` / `idfw` across 48 files: CLAUDE.md, README.md,
docs/MAINTAINING.md, 10 SKILL.md files, all 7 agents, onboarding guides, `doc_mapping.yaml`
(27), `.repo_state.json`, test fixtures, and `skills/twingate-idfw/references/`.

## Pipeline gaps to check first on the PR

1. **New URLs fall to `_triage/`.** `auto_assign_patterns` in `scripts/doc_mapping.yaml` match only
   `/docs/ssh-`, `/docs/idfw`, `/docs/identity-firewall`, `/docs/web-app`. If pages moved to e.g.
   `/docs/pam` or `/docs/privileged-access`, they will be in `_triage/`. Add the patterns and route
   them to the skill.
2. **Removed URLs are never pruned.** `update_references.py` only logs "N URL(s) removed from
   sitemap". Old `identity-firewall*.md` references and their explicit `url:` entries stay behind
   until deleted by hand. Check the run log for the removed list.

If URLs are unchanged and only content changed, the pages re-summarize normally; only the
hand-authored sweep is needed.

## Steps (in order)

1. Fix triage routing (gap 1) and move any triaged PAM pages into the skill's `references/`.
2. Rename skill `skills/twingate-idfw/` → `skills/twingate-pam/` and its frontmatter `name`.
3. Rename agent `agents/idfw-deployer.md` → `agents/pam-deployer.md` and its `name`.
4. Update every `skill: twingate-idfw` in `doc_mapping.yaml`, `doc_path` entries in
   `scripts/.repo_state.json`, and the `twingate-idfw` paths in `scripts/tests/` fixtures.
5. Update cross-references in other skills, agents, onboarding guides
   (`agent-delegation.md`, `persona-catalog.md`, `question-bank.md`, `phase-4-access-model.md`),
   CLAUDE.md (architecture tree, skill/agent tables, design rule 9), README, MAINTAINING.md.
6. Delete stale old-name references and their `url:` entries (gap 2); rebuild the PAM skill's
   `## References` routing table so every file is reachable.
7. Re-measure every edited skill `description` against the 1024-char cap.
8. Bump `plugin.json` version — skill and agent ids change, which breaks anyone invoking them by name.
9. Run ruff, mypy, pytest locally.

## Sweep rules

- **"PAM" collides with Linux Pluggable Authentication Modules** (e.g. "PAM module errors" in
  `skills/twingate-troubleshoot/SKILL.md`). No blind find-and-replace. Write "Privileged Access
  Management (PAM)" on first use per file; leave Linux-PAM wording alone.
- **Keep the old name as a trigger.** Retain "Identity Firewall" / "IDFW" as keywords in the PAM
  skill and agent descriptions — customers, blogs, and older Terraform/Ansible repos will keep using it.
- **Do not rename API/Terraform/GraphQL identifiers** unless the references show they changed.

## Name-change callout

- PAM skill `## Role`: one line — formerly Identity Firewall (IDFW), renamed <month year>; treat the
  old name in user input, older docs, and repos as the same product.
- PAM skill `## Decisions & Guidelines`: API/Terraform identifiers do not follow the marketing
  rename — read them from `references/`.
- README: dated note of the rename (no CHANGELOG exists).
