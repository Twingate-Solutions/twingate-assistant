<!-- manual-reference: do-not-overwrite -->
# Agent delegation

The onboarding conversation runs in the **main thread**: it holds the multi-turn Q&A with the
admin and is the **only writer** of `deployment.yaml`. Subagents cannot hold an interactive Q&A,
so they get bounded jobs, a brief, and a slice of the state file — and return results that the
main thread records (as `inferred` until the admin approves).

## Which agent, when

| Phase | Agent | Job | Returns |
|---|---|---|---|
| 1, 4 | `network-designer` | Draft Remote Network boundaries, the Resource table, and the persona/access matrix from the catalog | Proposed tables + rationale |
| 5, 6 | `aws-deployer` / `azure-deployer` / `gcp-deployer` (by `remote_networks[].location`) | Connector hosting plan and IaC for that cloud, network rules, preflight | Plan, generated code, admin tasks |
| 4, 7 | `idfw-deployer` | SSH, Kubernetes, or internal web-app resources needing per-user identity or session recording | IDFW design + tasks |
| Before 5 and before 7 | `deployment-reviewer` | Read-only review of the state file and planned build | Findings list (blocking / advisory) |
| Any, cross-domain | `twingate-se` | Broad design questions spanning several domains | Recommendation |

Delegate when the job needs deep, single-domain work or many file reads; handle quick lookups
yourself by loading the sibling skill. Run independent delegations in parallel (e.g. one deployer
per cloud).

## Brief template

```
Goal: <one sentence>
Phase: <n> — <name>
Deployment context (from deployment.yaml):
  <only the relevant slice: the remote network(s), resources, personas/groups, environment facts>
Constraints: assist_level=<…>, scripting=<…>, existing_iac=<…>, windows_only=<…>
Already decided: <decisions entries that bind this work>
Do not: write or edit deployment.yaml; create anything in the tenant; ask for or handle tokens.
Return: <tables / code / tasks>, each technical fact cited to the skill whose references it came from.
```

## After the agent returns

- Record proposals as `inferred` (or `sourced` if the agent read an artifact/API), with a
  `sources` entry `kind: doc`, description "<agent> proposal".
- Show the admin a compact summary and ask for approval as usual.
- Relay blocking findings from `deployment-reviewer` verbatim; do not build until each is
  resolved or explicitly accepted by the admin (log acceptance in `decisions`).
