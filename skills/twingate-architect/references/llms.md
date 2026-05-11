# AI and LLM Access with Twingate

## Summary
Twingate provides Zero Trust secure access to private AI infrastructure including LLM servers, MCP servers, and GPU resources without public IP exposure. It enables distributed teams to connect AI coding assistants and tools to private endpoints through encrypted peer-to-peer tunnels.

## Key Information
- Supports remote LLM servers (Ollama, vLLM, other inference engines)
- Supports Model Context Protocol (MCP) servers
- Compatible with AI coding tools: Continue.dev, Cursor, Cody
- No public IP required for AI infrastructure
- Split tunneling: only AI traffic routes through Twingate

## Prerequisites
- Twingate account with Admin Console access
- Connector deployment capability on AI server network
- AI servers (LLM/MCP) running on private network

## Step-by-Step Setup

1. **Deploy a Connector** on the same network as your AI servers
2. **Create Resources** for LLM or MCP server endpoints in Admin Console
3. **Grant Access** to users or groups via Access Policies
4. **Configure AI tools** to point to Twingate-protected endpoints
5. **Monitor usage** through Twingate Analytics

## Configuration Values
- Groups and Security Policies for granular access control
- Service Accounts for headless/automated AI workloads

## Gotchas
- LLM servers (e.g., Ollama) must be configured to listen on network interfaces, not just localhost
- MCP servers require specific security considerations — see Identity Firewall for protocol-aware controls
- Service Accounts needed for non-interactive/automated AI workload access

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/remote-llm-access)
- [Remote MCP Access Guide](https://www.twingate.com/docs/remote-mcp-access)
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)