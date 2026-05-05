## OpenClaw Deployment Hub

Index page for OpenClaw deployment guides. **OpenClaw** (formerly ClawdBot/MoltBot) is an AI-powered assistant for WhatsApp, Telegram, etc. The Twingate value-add: secure remote access without public ports, VPN, or bastion hosts.

### Why Twingate for OpenClaw

| Traditional Approach | Twingate Approach |
|---|---|
| Expose SSH or HTTP ports publicly | Zero inbound; Connector outbound-only |
| VPN credentials to manage | Twingate Client (per-user policies) |
| Bastion host setup | None needed |
| Trust the network | Authenticate every connection |

### Common Architecture

All OpenClaw + Twingate deployments share this pattern:
1. **OpenClaw Gateway** runs on `localhost:18789` (never publicly exposed)
2. **Twingate Connector** establishes outbound-only connection to Twingate Cloud
3. **Team members** connect via Twingate Client with Zero Trust policies
4. **End-to-end encryption** with full audit trails
5. **No inbound ports** required on the host

### Deployment Guides

- /docs/openclaw-docker-compose -- Any Docker host (local, homelab, VPS, cloud VM)
- /docs/openclaw-digitalocean -- DigitalOcean Droplet via Marketplace + locked-down VPC

### Setup Steps Common to All Deployments

1. Sign up at twingate.com (free for small teams)
2. Define a Remote Network for OpenClaw
3. Deploy a Twingate Connector on the same network as the Gateway
4. Create a Resource for the OpenClaw Gateway
5. Configure Resource Access (Groups + policies)
6. Install Twingate Client on team member devices
7. Connect — no public ports needed

### Prerequisites

- Twingate account (free tier OK)
- Infrastructure platform access (cloud account, server, etc.)
- AI provider API key (Anthropic, OpenAI, etc.)
- Linux command line familiarity

### Security Best Practices

- Enable MFA on production Gateways (Resource Policy with 2FA)
- Use Groups (not individual user assignments) for access management
- Lock inbound ports completely — including SSH
- Enable audit logging; review regularly
- Rotate AI provider keys periodically
- Monitor Connector health (dashboard / webhooks)
- Use private IP addresses for Resources where possible

### Decision Notes

- Pick the deployment guide that matches your existing infrastructure -- they're functionally equivalent
- For pure local/dev: Docker Compose mode without the Twingate add-on is fine
- For team/remote: always add Twingate; the public-port alternative is much riskier
- This is community-published content — Twingate-Community org owns the source repos

### Related Docs

- /docs/openclaw-docker-compose, /docs/openclaw-digitalocean -- Per-platform guides
- /docs/connector-deployment -- Connector deployment overview
- /docs/connector-monitoring -- Health monitoring
- /docs/security-policies-best-practices -- Policy + MFA design

### External Resources

- Twingate Subreddit: r/Twingate
- OpenClaw docs: docs.openclaw.bot
