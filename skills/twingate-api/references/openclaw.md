# Secure OpenClaw Deployments with Twingate

## Summary
OpenClaw (formerly ClawdBot/MoltBot) is an AI-powered assistant platform integrating with WhatsApp, Telegram, and other messaging services. This page provides an overview of securing OpenClaw deployments using Twingate's Zero Trust architecture to eliminate public port exposure. Deployment guides exist for Docker Compose and DigitalOcean platforms.

## Key Information
- OpenClaw Gateway runs on `localhost:18789` (never publicly exposed)
- Twingate Connector makes outbound-only connections to Twingate Cloud — no inbound ports required
- Supports AI providers: Anthropic, OpenAI, and others (API key required)
- Two deployment guides available: **Docker Compose** and **DigitalOcean**

## Prerequisites
- Twingate account (free tier available for small teams)
- Access to target infrastructure platform (cloud or on-prem)
- AI provider API key (Anthropic, OpenAI, etc.)
- Basic Linux/Unix CLI familiarity

## Architecture
```
Team Members (Twingate Client)
        ↓ Zero Trust auth
Twingate Cloud
        ↓ outbound-only tunnel
Twingate Connector (same network as Gateway)
        ↓ private network
OpenClaw Gateway (localhost:18789)
```

## Step-by-Step (Common Setup)
1. Create Twingate account at `twingate.com/signup`
2. Define a **Remote Network** for OpenClaw infrastructure
3. Deploy a **Twingate Connector** on the same network as the Gateway
4. Create a **Resource** pointing to the OpenClaw Gateway
5. Configure **Resource Access** policies (who can reach it)
6. Install **Twingate Client** on team member devices
7. Connect — no public ports needed

## Configuration Values
| Component | Value |
|---|---|
| OpenClaw Gateway port | `localhost:18789` |
| Connector connection type | Outbound-only |
| Inbound ports required | None |

## Security Best Practices
- Enable **MFA** for all users accessing production Gateways
- Use **Groups** for access management, not individual user permissions
- Block **all** inbound ports (no SSH, no HTTP)
- Enable and review **audit logs** regularly
- Rotate AI provider API keys periodically
- Monitor Connector health
- Use **private IP addresses** for Resources

## Gotchas
- No inbound firewall rules should be created — architecture relies entirely on outbound Connector tunnels
- Even if a server is compromised, the Gateway remains inaccessible without Twingate auth (defense in depth)
- Previously known as ClawdBot and MoltBot — documentation may reference old names

## Related Docs
- [Twingate Connector Deployment Options]
- [Remote Network Best Practices]
- [Connector Monitoring]
- [Access Groups and Policies]
- OpenClaw Documentation: `docs.openclaw.bot`
- Community: `r/Twingate`