# AI and LLM Access with Twingate

## Summary
Twingate provides Zero Trust network access to private AI infrastructure including LLM servers, MCP servers, and GPU compute resources. It eliminates public IP exposure for AI endpoints while enabling distributed teams to securely connect AI coding assistants and tools to private infrastructure.

## Key Information
- Supports remote LLM servers (Ollama, vLLM, other inference engines)
- Supports Model Context Protocol (MCP) servers
- Compatible with AI coding assistants: Continue.dev, Cursor, Cody
- Uses split tunneling — only AI traffic routes through Twingate
- Peer-to-peer connections optimized for low-latency interactive AI use

## Prerequisites
- Twingate account with Admin Console access
- Connector deployable on same network as AI servers
- Target AI servers (LLM/MCP) running on private network

## Step-by-Step Setup
1. **Deploy Connector** — place on same network segment as AI/GPU servers
2. **Create Resources** — define LLM or MCP server endpoints in Admin Console
3. **Grant Access** — assign Resources to users or Groups
4. **Configure AI tools** — point coding assistants/AI clients to private endpoints via Twingate
5. **Monitor usage** — review connections in Twingate Analytics

## Configuration Values
- No client-side config files or routing tables required
- Access control via Groups and Security Policies (configured in Admin Console)
- Service Accounts available for headless/automated AI workloads

## Key Features
| Feature | Detail |
|---|---|
| Zero Trust | Per-resource authorization, no implicit network access |
| No public IP needed | LLM/MCP servers stay fully private |
| Split tunneling | Non-AI traffic bypasses Twingate |
| Audit trails | All connections logged in Analytics |
| Identity Firewall | Protocol-aware security (relevant for MCP) |

## Gotchas
- LLM servers (e.g., Ollama) must be configured to listen on network interface, not just localhost
- Connector must be co-located on the same network as AI servers for proper routing
- MCP deployments have specific security considerations — see dedicated MCP guide

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/remote-llm-access)
- [Remote MCP Access Guide](https://www.twingate.com/docs/remote-mcp-access)
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)