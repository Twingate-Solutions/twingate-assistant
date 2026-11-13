---
source: https://www.twingate.com/docs/deployment-semi-automation
type: docs
fetched: 2026-11-13
source_version: 74fc6dc3f8041ea2166aaa39ae20317f3402b909dca0b99ac23c4678e7f9aac4
trust: official
---

# Deployment Automation (Twingate Connectors)

## Summary
Twingate Connectors run as `linux/amd64` Docker containers, so they can be deployed in many environments. Deployment can be fully automated with the Terraform provider, driven via the Admin API, or semi-automated using tokens generated manually in the Admin Console.

## Key Information
- **Full automation:** Twingate Terraform provider provisions Connectors, Resources, Remote Networks, etc.
- **Admin API:** Programmatic control of most admin functions, including provisioning Connectors and generating new tokens.
- **Semi-automated:** Use the "Manual" Connector deployment option in the Admin Console to get tokens.
- Connector tokens are **unique per Connector** and **cannot be reused** across Connectors.
- New Connectors must still be provisioned via the Admin Console or API. Use the environment variables generated for that specific Connector.
- Image: public on Docker Hub, `docker.io/twingate/connector:latest`.
- A Helm chart example is available at https://github.com/Twingate/helm-charts.

## Prerequisites
- A Twingate account and Remote Network
- A provisioned Connector (via Console, API, or Terraform) with its tokens
- A container runtime or orchestrator that supports `linux/amd64`
- If using `DNS_SERVER`, a DNS server reachable from the Connector host

## Step-by-Step (Semi-Automated)
1. In the Admin Console, provision a new Connector and choose the **Manual** deployment option.
2. Copy the generated access and refresh tokens for that Connector.
3. Deploy the `twingate/connector` image with the required environment variables.
4. Set a restart policy equivalent to `--restart=unless-stopped`.
5. Name the container (`--name`), ideally matching the Connector name in the Admin Console.
6. Repeat the provisioning and token steps for each additional Connector.

## Configuration Values
| Name | Required | Notes |
|---|---|---|
| `TWINGATE_NETWORK` | Yes | Account subdomain (e.g. `acme` for `acme.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Yes | Connector-specific secret |
| `TWINGATE_REFRESH_TOKEN` | Yes | Connector-specific secret |
| `DNS_SERVER` | No | DNS server used to resolve Resources |
| `--restart=unless-stopped` | Yes (Docker) | Auto-restart unless explicitly stopped; use the equivalent in other platforms |
| `--name` | Recommended | Container identifier |

## Gotchas
- Never reuse a Connector's token variables for another Connector.
- Treat access and refresh tokens as secrets; never commit them to source control.
- A private `DNS_SERVER` must be reachable from the Connector host.
- Manual token generation does not remove the need to provision each Connector via Console or API.

## Related Docs
- Twingate Terraform provider documentation
- Twingate Admin API documentation
- Helm charts: https://github.com/Twingate/helm-charts