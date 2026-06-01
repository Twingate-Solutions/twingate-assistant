# AI and LLM Access with Twingate

## Summary
Twingate provides Zero Trust network access to private AI infrastructure including LLM servers, GPU clusters, and MCP servers. It eliminates public IP exposure while enabling distributed teams to securely reach shared AI resources. Works with standard AI tools (Ollama, vLLM, Continue.dev, Cursor, Cody) without VPN configuration files.

## Key Information
- Supports remote LLM servers (Ollama, vLLM, other inference engines)
- Supports Model Context Protocol (MCP) servers
- Uses split tunneling — only AI traffic routes through Twingate
- Provides audit trails via Twingate Analytics
- Compatible with all major AI tools and frameworks
- Service Accounts available for headless/automated AI workloads

## Prerequisites
- Twingate account with Admin Console access
- Connector deployed on same network as AI server
- AI server (LLM or MCP) reachable on private network

## Step-by-Step
1. Deploy a **Connector** on the same network as your AI servers
2. Create **Resources** for your LLM or MCP server endpoints
3. **Grant Access** to appropriate users or groups
4. Configure AI tools to connect through Twingate
5. Monitor usage via Admin Console

## Configuration Values
- No client-side config files or routing tables required
- Resource definition: hostname/IP + port of LLM/MCP server
- Access control via Groups and Security Policies

## Gotchas
- LLM servers must be configured for network access (not just localhost) — covered in Remote LLM Access Guide
- MCP deployments have specific security considerations — see Remote MCP Access Guide
- Identity Firewall provides protocol-aware security specifically relevant for MCP

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/remote-llm-access)
- [Remote MCP Access Guide](https://www.twingate.com/docs/remote-mcp-access)
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)