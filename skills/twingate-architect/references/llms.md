# AI and LLM Access with Twingate

## Summary
Twingate provides Zero Trust secure access to private AI infrastructure including LLM servers, GPU clusters, and MCP servers without exposing them publicly. It enables distributed teams to connect AI coding assistants and tools to centralized private AI resources through encrypted peer-to-peer tunnels.

## Key Information
- Supports LLM inference engines: Ollama, vLLM, and similar
- Supports AI coding tools: Continue.dev, Cursor, Cody
- Supports Model Context Protocol (MCP) servers
- No public IP required for AI infrastructure
- Split tunneling ensures only AI traffic routes through Twingate
- Access logging available via Twingate Analytics

## Prerequisites
- Twingate account with Admin Console access
- Connector deployable on same network as AI servers
- AI servers (LLM/MCP) running on private network

## Step-by-Step Setup

1. **Deploy a Connector** on the same network as your AI/LLM servers
2. **Create Resources** defining your LLM or MCP server endpoints (hostname/IP + port)
3. **Grant Access** to users or groups via Admin Console
4. **Configure AI tools** (Cursor, Continue.dev, etc.) to point to the private endpoint
5. **Monitor usage** via Twingate Analytics in Admin Console

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Resource configuration: private IP/hostname of LLM/MCP server
- Access control: Groups + Security Policies
- See sub-guides for tool-specific configuration values

## Gotchas
- LLM servers must be configured to accept network connections (not just localhost) — covered in the Remote LLM Access Guide
- MCP servers require specific deployment considerations for private networks — covered in the Remote MCP Access Guide
- Automated/headless AI workloads require Service Accounts (not user accounts)

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/remote-llm-access)
- [Remote MCP Access Guide](https://www.twingate.com/docs/remote-mcp-access)
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall) — protocol-aware security for MCP
- [Service Accounts](https://www.twingate.com/docs/service-accounts) — headless/automated AI workload access