# AI and LLM Access with Twingate

## Summary
Twingate provides Zero Trust network access to private AI infrastructure including LLM servers, GPU clusters, and MCP servers. It eliminates public IP exposure while giving distributed teams secure, low-latency access to shared AI resources.

## Key Information
- Supports remote LLM servers (Ollama, vLLM, other inference engines)
- Supports Model Context Protocol (MCP) servers
- Compatible with AI coding assistants: Continue.dev, Cursor, Cody
- Uses peer-to-peer connections with split tunneling (only AI traffic routed through Twingate)
- Provides audit trails via Twingate Analytics

## Prerequisites
- Twingate account with Admin Console access
- Connector deployable on same network as AI servers
- AI servers configured for network access (not just localhost)

## Step-by-Step
1. **Deploy a Connector** on the same network as your AI/LLM servers
2. **Create Resources** defining your LLM or MCP server endpoints
3. **Grant Access** to users or groups via Admin Console
4. **Configure AI tools** to point to Twingate-protected endpoints
5. **Monitor usage** through Twingate Analytics

## Configuration Values
- No specific env vars or CLI flags listed on this page
- See sub-guides for server-specific configuration (Ollama, vLLM, MCP)

## Gotchas
- LLM servers must be configured for network access (default Ollama binds to localhost only — requires explicit network binding)
- Detailed server config and troubleshooting deferred to sub-guides

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/llms/remote-llm) — Ollama/vLLM setup + AI coding assistant config
- [Remote MCP Access Guide](https://www.twingate.com/docs/llms/remote-mcp) — MCP server deployment + AI assistant config
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall) — Protocol-aware security for MCP
- [Service Accounts](https://www.twingate.com/docs/service-accounts) — Headless/automated AI workload access