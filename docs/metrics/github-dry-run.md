# GitHub Discovery Dry-Run — Cost/Time Sizing Report

Generated at: 2026-08-06T18:07:16.589599+00:00

> **Unauthenticated run** — no `GITHUB_TOKEN`. This source is token-free by design: all repos and pages here are public, so a token is never required. A first-run sizing pass makes only the four org-listing calls (no per-repo diff calls), which stays well within the 60 req/hr unauthenticated limit — this is the supported way to run it, and this dry-run/sizing pass deliberately does not enable the adaptive rate-limit throttle (it stays fast and log-and-give-up on a 403). If a future run does diff against recorded state and 403s more than expected, that throttle is available (see `rate_limit_wait()`), and a present `GITHUB_TOKEN` is still picked up automatically as an optional speed-up; check the run log for any 403 WARNING lines if counts look short.

## Per-Org Discovery

| Org | Total Public Repos | Forks Excluded | Non-Fork Kept | Stub Candidates |
|---|---:|---:|---:|---:|
| Twingate | 24 | 17 | 7 | 0 |
| Twingate-Solutions | 21 | 1 | 20 | 0 |
| Twingate-Labs | 25 | 3 | 22 | 7 |
| Twingate-Community | 12 | 2 | 10 | 0 |
| **Total** | **82** | **23** | **59** | **7** |

## Change Detection

- Repos changed since baseline (this run's baseline is empty — first run): **59** of 59 kept repos
- Repos with a wiki enabled (`has_wiki`): **52**

## Filtered Doc-Diff Size Distribution

- **59** repo(s) had no recorded `last_sha` (new repo / first observed run) — no compare call was made for these; they are sized by presence, not diff. Their filtered size shows as 0.
- No repos had a prior recorded state to diff against, so there is no real diff-size distribution yet. Run again after `.repo_state.json` has been populated by a real run to get meaningful sizing.

## Per-Repo Detail

| Repo | First Run | Doc Files Changed | Line Changes | Patch Bytes | Has Wiki |
|---|---|---:|---:|---:|---|
| Twingate-Community/.github | yes | 0 | 0 | 0 | yes |
| Twingate-Community/dashboards | yes | 0 | 0 | 0 | yes |
| Twingate-Community/diy-vpn | yes | 0 | 0 | 0 | yes |
| Twingate-Community/home-assistant-add-on | yes | 0 | 0 | 0 | yes |
| Twingate-Community/openclaw-secure-access | yes | 0 | 0 | 0 | yes |
| Twingate-Community/pi-starter | yes | 0 | 0 | 0 | no |
| Twingate-Community/twindeck | yes | 0 | 0 | 0 | yes |
| Twingate-Community/ubiquiti-connector | yes | 0 | 0 | 0 | yes |
| Twingate-Community/ubiquiti-headless-gateway | yes | 0 | 0 | 0 | yes |
| Twingate-Community/unraid-template | yes | 0 | 0 | 0 | no |
| Twingate-Labs/.github | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/Twingate-API-Intro-with-Python | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/Twingate-CLI | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/chocolatey-packages | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/connector-init-container | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/kasm-registry | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/kasm-workpsace-images | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/pulumi-twingate | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/pulumi-twingate-smallstep | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/saml_service_provider | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-aws-tag-sync | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-cli | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-client-k8s-sidecar | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-coder | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-github-codespaces | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-group-profile-manager | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-group-profile-manager-helm | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-ip-lookup | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-netbox | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tg-render | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/tgcli-web-py | yes | 0 | 0 | 0 | yes |
| Twingate-Labs/twingate-pagerduty | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/.github | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/connector-local-ui | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/gatorcast | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/general-scripts | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/health-report-generator | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/idp-migrator | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/janus-updater-service | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/network-utilities | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/pulumi-scripts | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/railway-private-web-app | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/terraform-scripts | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/twingate-assistant | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/twingate-client-userspace-spacelift | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/twingate-connector-hyperv | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/twingate-connector-log-shipper | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/twingate-custom-connector-container | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/twingate-fleet-commander | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/twingate-mdm-connector | yes | 0 | 0 | 0 | yes |
| Twingate-Solutions/twingate-raspberry-pi | yes | 0 | 0 | 0 | no |
| Twingate-Solutions/twingate-wayfinder-app | yes | 0 | 0 | 0 | no |
| Twingate/.github | yes | 0 | 0 | 0 | yes |
| Twingate/gateway | yes | 0 | 0 | 0 | yes |
| Twingate/github-action | yes | 0 | 0 | 0 | no |
| Twingate/helm-charts | yes | 0 | 0 | 0 | no |
| Twingate/kubernetes-operator | yes | 0 | 0 | 0 | yes |
| Twingate/pulumi-twingate | yes | 0 | 0 | 0 | yes |
| Twingate/terraform-provider-twingate | yes | 0 | 0 | 0 | no |

