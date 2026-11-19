---
source: https://github.com/Twingate-Community/twingate-in-a-box
type: github
fetched: 2026-11-19
source_version: 21d158f8bb3f96efff1a81a2ee0380f7ff37e731
trust: community
---

<!-- triage: unassigned -->

# Twingate in a Box

## Summary
Twingate in a Box provides two Terraform deployments that stand up a Twingate Remote Network, Connector, and Gateway as Docker containers. The Connector gives Zero Trust access to defined Resources. The Gateway adds identity-aware access to web apps (passwordless sign-in via passed-through identity) and SSH (short-lived certificates per session, no keys to manage). It is a lab tool, not a production deployment.

## Key Information
- Two Terraform roots, each with its own state:
  - `docker/`: apps run in the box from its own `docker-compose.yaml`. Terraform parses `twingate.*` labels from the compose file. Apps are at `https://<service>.box.internal`. Terraform creates a bridge network that Compose joins. Best for seeing how a Gateway works on a dev machine. Includes an SSH server to try.
  - `proxy/`: fronts apps that already run elsewhere. Uses an explicit `services` map. Apps are at `https://<name>.box.internal`. Uses the host's network namespace. Best for putting a Gateway in front of a homelab.
- Both call `modules/twingate-stack`, which owns the CA, Gateway, and Connector. The only structural difference is the module's `host_network` flag.
- No inbound ports needed. The Connector dials out.

## Prerequisites
- Terraform 1.11 or later
- Docker
- Twingate API token with Read, Write, and Provision permissions
- For the quick start: Ubuntu 22.04+ (amd64 or arm64), 2 vCPU, 4 GB RAM, 20 GB disk with all services on, and outbound internet access

## Usage / Step-by-Step
**Quick start (Ubuntu VM, deploys `docker/`):** the README provides an `install.sh` that is fetched from raw.githubusercontent.com and run with `sudo`, with `TG_API_TOKEN` and `TG_NETWORK` set. Review the script in the repo (`install.sh` on `main`) before running it, and follow the README's command there. The script installs Docker and Terraform if missing, places the box in `/opt/twingate-in-a-box`, creates the tenant resources, and prints app URLs and the box CA with trust commands.

**Manual:** `cd` into `docker/` or `proxy/` and follow that directory's README.

**Cloud-init:** the README shows a `runcmd` entry that runs the same installer at VM creation. Progress is logged to `/var/log/twingate-in-a-box-install.log`.

**Add or remove services:** re-run the installer with a different `TG_SERVICES`. A re-run without it keeps the current set and picks up additions to `/opt/twingate-in-a-box/docker/docker-compose.yaml`.

**Uninstall:** `sudo bash /opt/twingate-in-a-box/install.sh --uninstall`. This removes containers, the Remote Network, Resources, and other tenant objects. Docker and Terraform stay installed.

## Configuration Values
- `TG_API_TOKEN`: Twingate API token (prompted if omitted)
- `TG_NETWORK`: Twingate network name (prompted if omitted)
- `TG_SERVICES`: comma-separated list; unset means all. Echo is always on.
  - `openwebui`: sign-in from a trusted `X-Twingate-User` header (~1 GB RAM)
  - `grafana`: sign-in from the Gateway's signed token, groups mapped to roles, plus Prometheus dashboards
  - `uptimekuma`: app with its own login, behind a friendly name
  - `ssh`: keyless SSH with session recording
  - `ittools`: app with no authentication, reachable only via Twingate
- Module flag: `host_network` (in `modules/twingate-stack`)

## Gotchas
- Terraform state holds the CA private key, Gateway private key, and Connector tokens in plaintext. `.gitignore` covers state and `terraform.tfvars`; never commit them.
- HTTPS requires trusting the box CA, which is not name-constrained, so its key holder could sign for any domain. Remove the CA when finished.
- Cloud-init user data is readable via the instance metadata service and often in the cloud console. Use a lab-tenant token or revoke it afterward.
- Omitting `openwebui` reduces resource needs.

## Related Docs
- `docker/README.md` (CA install/removal commands)
- `proxy/README.md`
- `modules/twingate-stack`
- Support: GitHub issues; the Twingate Subreddit for account issues