# Secure OpenClaw Deployments with Twingate

## Summary
OpenClaw (formerly ClawdBot/MoltBot) is an AI assistant platform integrating with WhatsApp, Telegram, and other messaging services. This page covers securing OpenClaw deployments using Twingate Zero Trust architecture to eliminate public port exposure. The Gateway runs on `localhost:18789` with all access routed through Twingate Connectors.

## Key Information
- OpenClaw Gateway runs on `localhost:18789` (not publicly exposed)
- Twingate Connector uses outbound-only connections to Twingate Cloud
- Supported deployment platforms: Docker Compose, DigitalOcean
- No inbound ports required on host infrastructure
- End-to-end encrypted traffic with full audit trails

## Prerequisites
- Twingate account (free tier available for small teams)
- Cloud account or server access for chosen platform
- AI provider API key (Anthropic, OpenAI, etc.)
- Basic Linux/Unix CLI familiarity

## Step-by-Step (Common Setup)
1. Create Twingate account at `twingate.com/signup`
2. Define a **Remote Network** for OpenClaw infrastructure
3. Deploy a **Twingate Connector** on same network as Gateway
4. Create a **Resource** pointing to the OpenClaw Gateway
5. Configure **Resource Access** policies (who can reach the resource)
6. Install **Twingate Client** on team member devices
7. Connect — no public ports needed

## Configuration Values
| Component | Value |
|-----------|-------|
| OpenClaw Gateway port | `localhost:18789` |
| Connector connection type | Outbound-only to Twingate Cloud |

## Security Best Practices
- Enable MFA for all users accessing production Gateways
- Use Groups for access management (not individual user permissions)
- Lock down **all** inbound ports — SSH, HTTP, everything
- Enable audit logging; review connection logs regularly
- Rotate AI provider API keys periodically
- Use private IP addresses for Resources whenever possible
- Monitor Connector health for availability

## Gotchas
- No specific platform credentials or env vars documented on this page — refer to platform-specific guides (Docker Compose, DigitalOcean)
- Gateway must not be publicly accessible; defense-in-depth relies on Twingate auth being the sole access path
- Even a compromised server won't expose the Gateway without valid Twingate authentication

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- Remote Network Best Practices
- Connector Monitoring
- Access Groups and Policies
- [OpenClaw Documentation](https://docs.openclaw.bot)
- Platform guides: Docker Compose, DigitalOcean (linked from this page)