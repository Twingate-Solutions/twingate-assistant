# Secure OpenClaw Deployments with Twingate

## Summary
OpenClaw (formerly ClawdBot/MoltBot) is an AI-powered assistant platform integrating with WhatsApp, Telegram, and other messaging services. This page provides an overview of securing OpenClaw deployments using Twingate's Zero Trust architecture, eliminating public port exposure. Deployment guides exist for Docker Compose and DigitalOcean.

## Key Information
- OpenClaw Gateway runs on `localhost:18789` — not publicly accessible by design
- Twingate Connector uses outbound-only connections; no inbound ports required
- Traffic is encrypted end-to-end with full audit trails
- Two deployment guides available: **Docker Compose** and **DigitalOcean**

## Prerequisites
- Twingate account (free tier available for small teams)
- Access to target infrastructure platform
- AI provider API key (Anthropic, OpenAI, etc.)
- Basic Linux/Unix CLI familiarity

## Architecture
```
Team Devices (Twingate Client)
        ↓ Zero Trust Auth
Twingate Cloud
        ↓
Twingate Connector (outbound-only, same network as Gateway)
        ↓
OpenClaw Gateway (localhost:18789, no public exposure)
```

## Common Setup Steps
1. Create Twingate account at `twingate.com/signup`
2. Define a **Remote Network** for OpenClaw infrastructure
3. Deploy a **Twingate Connector** on the same network as the Gateway
4. Create a **Resource** pointing to the OpenClaw Gateway
5. Configure **Resource Access** policies (who can reach it)
6. Install **Twingate Client** on team member devices
7. Connect — no public ports needed

## Configuration Values
| Item | Value |
|------|-------|
| OpenClaw Gateway port | `localhost:18789` |
| Connector connection type | Outbound-only |

## Security Best Practices (Gotchas)
- **No inbound ports** — block SSH, HTTP, everything; rely solely on Twingate
- **Use Groups** for access control, not individual user permissions
- **Enable MFA** for all users accessing production Gateways
- **Use private IPs** for Resources whenever possible
- **Rotate AI provider API keys** periodically
- Monitor Connector health to ensure availability
- Regularly review audit/connection logs

## Related Docs
- Twingate Connector Deployment Options
- Remote Network Best Practices
- Connector Monitoring
- Access Groups and Policies
- [OpenClaw Documentation](https://docs.openclaw.bot)
- Platform-specific guides: Docker Compose, DigitalOcean (linked from main page)