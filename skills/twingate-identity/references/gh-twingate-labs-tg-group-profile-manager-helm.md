---
source: https://github.com/Twingate-Labs/tg-group-profile-manager-helm
type: github
fetched: 2026-08-06
source_version: 60affada2a8e6be465c3dab35ec456e62b278826
---

<!-- triage: unassigned -->

# tg-group-profile-manager-helm

## Summary
Helm chart for deploying the Twingate Group Profile Manager, which enables Twingate group management through Slack. Users interact via Slack to request group membership changes according to defined profiles and approval workflows.

## Key Information
- Deploys a Slack bot that manages Twingate group assignments
- Supports profile types: `oneOf` (exclusive group selection) and `selfServeApproval` (approval-gated access with time limits)
- Profiles can be scoped to specific Twingate groups via `applicableToGroup` and `approverGroup`
- Chart hosted at `https://twingate-labs.github.io/tg-group-profile-manager-helm/`

## Prerequisites
- Helm 3
- A Kubernetes cluster with a target namespace
- Twingate account with API key (Read + Write permissions)
- Slack app with Bot Token (`xoxb-`) and Signing Secret
- Slack bot must be configured to receive interactions (requires accessible endpoint)

## Usage / Step-by-Step

**Add repo and install:**
```shell
helm repo add twingate-labs https://twingate-labs.github.io/tg-group-profile-manager-helm/

helm install tg-group-profile-manager twingate-labs/tg-group-profile-manager \
  -n [namespace] \
  --set variables.twingateAccount="xxx.twingate.com" \
  --set variables.twingateApiKey="xxx" \
  --set variables.slackSigningSecret="xxx" \
  --set variables.slackBotToken="xoxb-xxx" \
  --set-json='variables.profileConfig={"profiles":[...],"groupPermissions":{}}'
```

**Optional configurations:**
- Use Kubernetes Secrets instead of plain `--set` values: see `docs/WITH_SECRET.md`
- Expose via HTTPS/Ingress: see `docs/WITH_INGRESS.md`
- Set resource requests/limits: see `resources` section in `values.yaml`

## Configuration Values

| Parameter | Description |
|---|---|
| `variables.twingateAccount` | Twingate network address (e.g. `test1.twingate.com`) |
| `variables.twingateApiKey` | Twingate API key with Read/Write permissions |
| `variables.slackSigningSecret` | Slack app signing secret |
| `variables.slackBotToken` | Slack bot token (must start with `xoxb-`) |
| `variables.profileConfig` | JSON object defining profiles and group permissions |

**`profileConfig` structure:**
- `profiles[].profileName` – Display name
- `profiles[].profileType` – `oneOf` or `selfServeApproval`
- `profiles[].groups` – Twingate groups available in profile
- `profiles[].applicableToGroup` – Twingate group eligible to use this profile
- `profiles[].approverGroup` – (selfServeApproval only) Group that approves requests
- `profiles[].timeOptions` – (selfServeApproval only) Duration choices (e.g. `"1h"`, `"Forever"`)
- `groupPermissions` – Maps group names to permission levels (e.g. `"Prod":"Admin"`)

## Gotchas
- API key must have both Read **and** Write permissions; Read-only will cause failures
- `slackBotToken` must begin with `xoxb-`; other token types will not work
- Passing `profileConfig` requires `--set-json` flag, not `--set`, due to JSON complexity
- Slack interactions require a publicly reachable endpoint; configure ingress accordingly

## Related Docs
- [Profile Schema Documentation](./docs/SCHEMA.md)
- [Setup with Kubernetes Secret](./docs/WITH_SECRET.md)
- [Setup with Ingress/HTTPS](./docs/WITH_INGRESS.md)
- [values.yaml](./values.yaml)