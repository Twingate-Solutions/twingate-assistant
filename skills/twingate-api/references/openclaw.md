# Secure OpenClaw Deployments with Twingate

## Summary
OpenClaw (AI-powered assistant platform integrating with WhatsApp/Telegram) can be deployed with Twingate Zero Trust access to eliminate public port exposure. The Twingate Connector establishes outbound-only connections, keeping the OpenClaw Gateway (localhost:18789) fully private. Deployment guides cover Docker Compose and DigitalOcean platforms.

## Key Information
- OpenClaw Gateway runs on `localhost:18789` — never publicly exposed
- Twingate Connector uses outbound-only connections to Twingate Cloud
- No inbound firewall rules or open ports required on host infrastructure
- Replaces SSH port exposure, VPNs, and bastion host setups
- End-to-end encrypted traffic with built-in audit logging

## Prerequisites
- Twingate account (free tier available at twingate.com/signup)
- Infrastructure platform access (cloud account or on-prem servers)
- AI provider API key (Anthropic, OpenAI, etc.)
- Basic Linux/Unix CLI familiarity

## Step-by-Step (Core Setup)
1. Create Twingate account
2. Define a **Remote Network** for OpenClaw infrastructure
3. Deploy **Twingate Connector** on same network as OpenClaw Gateway
4. Create a **Resource** pointing to the OpenClaw Gateway
5. Configure **Resource Access policies** (users/groups)
6. Install **Twingate Client** on team member devices
7. Connect — no public ports needed

## Configuration Values
| Component | Value |
|-----------|-------|
| OpenClaw Gateway port | `localhost:18789` |
| Deployment guides | Docker Compose, DigitalOcean |

## Security Best Practices (Gotchas)
- **Lock down all inbound ports** — no SSH, HTTP, or any inbound access
- Use **Groups** for access control, not individual user assignments
- **Enable MFA** for all users accessing production Gateways
- Use **private IP addresses** for Resources (not public IPs)
- Rotate AI provider API keys periodically
- Monitor Connector health for availability issues
- Enable and review audit logs regularly

## Gotchas
- Gateway must not be publicly accessible — verify no inbound rules exist after deployment
- Even with server compromise, Gateway remains protected behind Twingate auth layer
- Platform-specific steps differ; use the appropriate deployment guide (Docker Compose vs. DigitalOcean)

## Related Docs
- Twingate Connector Deployment Options
- Remote Network Best Practices
- Connector Monitoring
- Access Groups and Policies
- OpenClaw docs: docs.openclaw.bot
- Community: r/Twingate