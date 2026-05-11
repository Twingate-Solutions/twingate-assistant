# Secure OpenClaw Deployments with Twingate

## Summary
OpenClaw (formerly ClawdBot/MoltBot) is an AI-powered assistant platform for WhatsApp/Telegram that can be secured using Twingate's Zero Trust architecture. Deployment guides cover Docker Compose and DigitalOcean platforms. The integration eliminates public port exposure by routing all access through outbound-only Twingate Connectors.

## Key Information
- OpenClaw Gateway runs on `localhost:18789` (never publicly exposed)
- Twingate Connector uses outbound-only connections to Twingate Cloud
- No inbound ports required on host infrastructure
- Traffic is encrypted end-to-end with full audit trails
- Two deployment targets: Docker Compose and DigitalOcean

## Prerequisites
- Twingate account (free tier available for small teams)
- Cloud/server account for chosen platform
- AI provider API key (Anthropic, OpenAI, etc.)
- Basic Linux/Unix CLI familiarity

## Architecture
```
Team Devices (Twingate Client)
    → Twingate Cloud
        → Twingate Connector (outbound-only)
            → OpenClaw Gateway (localhost:18789)
```

## Common Setup Steps
1. Create Twingate account at `twingate.com/signup`
2. Define a Remote Network for OpenClaw infrastructure
3. Deploy Twingate Connector on same network as Gateway
4. Create a Resource pointing to OpenClaw Gateway
5. Configure Resource Access policies (users/groups)
6. Install Twingate Client on team member devices
7. Connect without any public port exposure

## Configuration Values
| Item | Value |
|------|-------|
| OpenClaw Gateway port | `localhost:18789` |
| Deployment guides | Docker Compose, DigitalOcean |

## Security Best Practices
- Enable MFA for all users accessing production Gateways
- Use Groups for access management (not individual users)
- Block all inbound ports (SSH, HTTP, everything)
- Enable and review audit logs regularly
- Rotate AI provider API keys periodically
- Monitor Connector health
- Use private IP addresses for Resources

## Gotchas
- No specific CLI flags or env vars documented on this page — see platform-specific deployment guides for details
- Gateway must remain on localhost; do not bind to public interfaces

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- Remote Network Best Practices
- Connector Monitoring
- Access Groups and Policies
- [OpenClaw Documentation](https://docs.openclaw.bot)
- Platform guides: Docker Compose, DigitalOcean (linked from this page)