---
source: https://www.twingate.com/docs/openclaw
type: docs
fetched: 2026-08-14
source_version: 3ee2d772f16d314fa44c61c1fe64c6849ea450919f9dd8bd937ca45669bb811d
---

# Secure OpenClaw Deployments with Twingate

## Summary
OpenClaw (formerly ClawdBot/MoltBot) is an AI-powered assistant platform integrable with WhatsApp and Telegram. This page covers securing OpenClaw deployments using Twingate's Zero Trust architecture to eliminate public port exposure. The Gateway runs on localhost only, accessed exclusively through the Twingate Client.

## Key Information
- OpenClaw Gateway listens on `localhost:18789` — never publicly accessible
- Twingate Connector uses outbound-only connections (no inbound ports required)
- Two deployment guides available: **Docker Compose** and **DigitalOcean**
- All traffic is end-to-end encrypted with full audit trails
- Even if server is compromised, Gateway remains inaccessible without Twingate auth

## Prerequisites
- Twingate account (free tier available for small teams)
- Cloud account or server access for chosen platform
- AI provider API key (Anthropic, OpenAI, etc.)
- Basic Linux/Unix CLI familiarity

## Step-by-Step (Core Twingate Setup)
1. Create Twingate account at `twingate.com/signup`
2. Define a **Remote Network** for OpenClaw infrastructure
3. Deploy a **Twingate Connector** on the same network as the Gateway
4. Create a **Resource** pointing to the OpenClaw Gateway
5. Configure **Resource Access** policies (who can reach the resource)
6. Install **Twingate Client** on team member devices
7. Connect — no public ports needed

## Configuration Values
| Item | Value |
|------|-------|
| OpenClaw Gateway port | `localhost:18789` |
| Connector connection type | Outbound-only to Twingate Cloud |
| Inbound ports required | None |

## Security Best Practices
- **MFA**: Enable for all users accessing production Gateways
- **Groups**: Manage access via groups, not individual user permissions
- **Port lockdown**: Block all inbound — no SSH, HTTP, or any other ports
- **Audit logs**: Enable and review connection logs regularly
- **Credential rotation**: Rotate AI provider API keys periodically
- **Private IPs**: Use private IP addresses for Resources whenever possible
- **Connector monitoring**: Monitor health to ensure availability

## Gotchas
- Gateway is intentionally not publicly accessible — do not expose port 18789
- Each platform (Docker Compose vs. DigitalOcean) has platform-specific steps not covered on this overview page
- Connector must be deployed on the **same network** as the Gateway

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- Remote Network Best Practices
- Connector Monitoring
- Access Groups and Policies
- OpenClaw docs: `docs.openclaw.bot`
- Community: `r/Twingate`