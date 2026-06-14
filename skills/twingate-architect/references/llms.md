# AI and LLM Access with Twingate

## Summary
Twingate provides Zero Trust network access to private AI infrastructure including LLM servers, GPU clusters, and MCP servers. It eliminates public exposure of AI endpoints while enabling distributed teams to securely connect AI coding tools to internal models.

## Key Information
- Supports private LLM inference engines: Ollama, vLLM, and similar
- Supports Model Context Protocol (MCP) servers for AI assistant tool access
- Compatible AI coding tools: Continue.dev, Cursor, Cody
- Uses peer-to-peer connections with split tunneling (only AI traffic routed through Twingate)
- No public IP required for AI servers

## Prerequisites
- Twingate account with Admin Console access
- Connector deployable on same network as AI servers
- AI server (LLM/MCP) running on a private network

## Step-by-Step Setup
1. **Deploy a Connector** on the same network as your AI servers
2. **Create Resources** defining your LLM or MCP server endpoints
3. **Grant Access** to users or groups via Twingate Admin Console
4. **Configure AI tools** to point to the Twingate-accessible endpoints
5. **Monitor usage** through Twingate Analytics

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Access control via: Groups, Security Policies
- Monitoring: Twingate Analytics / Admin Console

## Gotchas
- LLM servers must be configured to accept network connections (not just localhost) — covered in Remote LLM Access Guide
- Service Accounts required for headless/automated AI workloads
- MCP security may require Identity Firewall (protocol-aware) configuration

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/remote-llm-access)
- [Remote MCP Access Guide](https://www.twingate.com/docs/remote-mcp-access)
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)