---
source: https://github.com/Twingate-Community/openclaw-secure-access
type: github
fetched: 2026-08-06
source_version: c138604bd7e83b370288efb8c32b69429b2e4062
---

<!-- triage: unassigned -->

# Twingate-Community/openclaw-secure-access

## Summary
Collection of Infrastructure as Code templates and deployment guides for running OpenClaw (an AI chat assistant for WhatsApp/Telegram) on various cloud platforms. All deployments use Twingate as a Zero Trust access layer, binding the OpenClaw Gateway to localhost only with no public inbound ports.

## Key Information
- Two deployment targets currently available: Docker Compose and DigitalOcean (via Terraform)
- OpenClaw Gateway binds exclusively to `localhost:18789`; Twingate Connector handles all remote access via outbound-only connections
- Firewall configured with zero inbound rules across all deployments
- OpenClaw supports Claude and GPT models via WhatsApp/Telegram interfaces
- Terraform 1.0+ used for DigitalOcean provisioning; Docker Compose for local/container deployments
- License: MIT

## Prerequisites
- Account with chosen cloud/platform provider (DigitalOcean, Docker host, etc.)
- Twingate account (free tier supported)
- Terraform 1.0+ (for cloud deployments)
- OpenClaw account/license
- API keys for AI provider (Claude or OpenAI)

## Usage / Step-by-Step
1. Select a deployment target from the table (Docker Compose or DigitalOcean)
2. Follow the linked deployment guide for that platform
3. For DigitalOcean: use Terraform configs in `terraform/digitalocean/`
4. For Docker Compose: use configs in `docker-compose/`
5. Configure Twingate Connector with your network credentials
6. Add OpenClaw resource in Twingate pointing to `localhost:18789`
7. Grant team members access via Twingate Zero Trust policies

## Configuration Values
- **Gateway bind address**: `localhost:18789` (do not change to public interface)
- **Twingate Connector**: requires `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` (environment variables; do not commit)
- **AI provider keys**: set via environment variables (not hardcoded)
- Terraform variables documented in `terraform/digitalocean/digital-ocean-deployment-guide.md`

## Gotchas
- Never expose port 18789 publicly; the security model depends entirely on localhost binding
- Do not commit API keys, Twingate tokens, or secrets to the repository
- OpenClaw was previously named Clawdbot and Moltbot; documentation may reference old names
- Additional cloud providers (AWS, GCP, Azure) are referenced in architecture diagrams but not yet implemented in this repo
- MFA enforcement in Twingate is optional per the README but strongly implied for production use

## Related Docs
- [OpenClaw Documentation](https://docs.openclaw.ai/)
- [Twingate Documentation](https://docs.twingate.com)
- [Docker Compose Deployment Guide](https://docs.twingate.com/docs/openclaw-docker-compose)
- [DigitalOcean Deployment Guide](terraform/digitalocean/digital-ocean-deployment-guide.md)
- [GitHub Issues](https://github.com/Twingate-Community/openclaw-secure-access/issues)