<!-- manual-reference: do-not-overwrite -->
# Phase 0 — Kickoff

**Goal:** know why, what "done" means, how the admin wants to work, and where the tenant is.

**Load:** twingate-architect (keep loaded for the whole engagement). Use twingate-architect to answer
"how does Twingate work" questions that come up.

## Steps

1. Look for `twingate-deployment/deployment.yaml` (or an attached state file). If it exists, this
   is a resume: run `scripts/status.py`, summarise in 3–5 lines, and jump to the recorded phase.
2. Otherwise copy `assets/deployment.template.yaml` to `twingate-deployment/deployment.yaml`
   (see `state-schema.md` for chat-only environments). Mention once that it holds internal
   network detail and belongs outside public repos.
3. Look for existing context before asking: `twingate-context.md`, `*.tf` / Pulumi / Helm files
   touching Twingate, and the admin's IaC layout. Record findings (`existing_iac`, existing
   Twingate objects) as `sourced`.
4. Ask the kickoff questions from `question-bank.md`: driver, path, assist level, success
   criteria, tenant, config management, what artifacts they have. Ask path and assist level
   early — they set how much questioning follows.
5. Record everything; set `meta.phase: 1` when the gate passes.

## Exit gate

`meta.tenant`, `meta.path`, `meta.assist_level` set; ≥1 success criterion.

## Notes

- No tenant yet is fine — make "create the tenant" the first admin task, and record the chosen
  name once known.
- If the admin answers "just build it", explain in one line that nothing is built from guesses,
  and that the fastest path is the artifacts they already have.
