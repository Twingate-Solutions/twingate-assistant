# AI and LLM Access with Twingate

## Summary
Twingate enables secure Zero Trust access to private AI infrastructure including LLM servers, GPU instances, and MCP servers without public IP exposure. It supports AI coding assistants (Continue.dev, Cursor, Cody) and distributed team access to shared AI resources.

## Key Information
- Supports remote LLM servers: Ollama, vLLM, other inference engines
- Supports Model Context Protocol (MCP) servers
- No public IP required for AI infrastructure
- Split tunneling: only AI traffic routes through Twingate
- Peer-to-peer connections optimize latency for interactive AI use

## Prerequisites
- Twingate account with Admin Console access
- Connector deployable on same network as AI servers
- AI servers configured for network access (not just localhost)

## Step-by-Step Setup
1. **Deploy Connector** on the network hosting AI/LLM servers
2. **Create Resources** for LLM or MCP server endpoints
3. **Grant Access** to users or groups via Admin Console
4. **Configure AI tools** to point to Twingate-proxied endpoints
5. **Monitor usage** via Twingate Analytics

## Configuration Values
- No specific env vars/CLI flags on this page
- Access control via: Groups, Security Policies
- Monitoring: Twingate Analytics / Admin Console

## Gotchas
- LLM servers must be configured for network access (not bound to localhost only)
- Use Service Accounts for headless/automated AI workloads
- Identity Firewall required for protocol-aware MCP security

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/remote-llm-access)
- [Remote MCP Access Guide](https://www.twingate.com/docs/remote-mcp-access)
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)