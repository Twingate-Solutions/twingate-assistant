# Secure OpenClaw Deployments with Twingate

## Summary
OpenClaw (formerly ClawdBot/MoltBot) is an AI-powered assistant platform for WhatsApp/Telegram. This page provides an overview of deploying OpenClaw with Twingate Zero Trust access, eliminating public port exposure and VPN requirements. Specific deployment guides exist for Docker Compose and DigitalOcean.

## Key Information
- OpenClaw Gateway runs on `localhost:18789` (never publicly exposed)
- Twingate Connector uses outbound-only connections to Twingate Cloud
- No inbound ports required on infrastructure
- Supports MFA enforcement and audit logging per resource

## Prerequisites
- Twingate account (free tier available at twingate.com/signup)
- Cloud account or server access for chosen platform
- AI provider API key (Anthropic, OpenAI, etc.)
- Basic Linux/Unix CLI familiarity

## Architecture
```
Team Devices (Twingate Client)
    ↓ Zero Trust auth
Twingate Cloud
    ↓ outbound-only tunnel
Twingate Connector (same network as Gateway)
    ↓ private network
OpenClaw Gateway (localhost:18789)
```

## Step-by-Step (Common Setup)
1. Create Twingate account
2. Define a Remote Network for OpenClaw infrastructure
3. Deploy Twingate Connector on same network as Gateway
4. Create a Resource pointing to the OpenClaw Gateway
5. Configure Resource Access policies (users/groups)
6. Install Twingate Client on team member devices
7. Connect — no public ports needed

## Configuration Values
| Value | Detail |
|-------|--------|
| Gateway port | `localhost:18789` |
| Connector connection | Outbound-only to Twingate Cloud |
| Resource address | Private IP of Gateway host |

## Security Best Practices
- Enable MFA for all users accessing production Gateways
- Use Groups for access control (not individual users)
- Lock down **all** inbound ports — no SSH, HTTP, nothing
- Enable audit logging; review connection logs regularly
- Rotate AI provider API keys periodically
- Monitor Connector health for availability
- Always use private IP addresses for Resources

## Gotchas
- No inbound firewall rules should exist — any open port weakens the model
- This is an overview page; actual deployment steps are in platform-specific guides (Docker Compose, DigitalOcean)
- Even a compromised server won't expose the Gateway without valid Twingate auth

## Related Docs
- [Docker Compose Deployment Guide] (linked from page)
- [DigitalOcean Deployment Guide] (linked from page)
- Twingate Connector Deployment Options
- Remote Network Best Practices
- Access Groups and Policies
- OpenClaw docs: docs.openclaw.bot
- Community: r/Twingate