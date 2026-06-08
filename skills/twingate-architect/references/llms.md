# AI and LLM Access with Twingate

## Summary
Twingate enables secure Zero Trust access to private AI infrastructure including LLM servers, GPU clusters, and MCP servers without public IP exposure. It supports AI coding assistants (Continue.dev, Cursor, Cody) and distributed team access to shared AI resources.

## Key Information
- Supports private LLM inference engines: Ollama, vLLM, and similar
- Supports Model Context Protocol (MCP) servers for AI assistant tool integration
- No public IP required for AI infrastructure
- Split tunneling: only AI traffic routes through Twingate
- Peer-to-peer connections minimize latency for interactive AI use

## Prerequisites
- Twingate account with admin access
- Connector deployable on same network as AI servers
- AI servers configured for network access (not just localhost)

## Step-by-Step

1. **Deploy a Connector** on the same network as your AI/LLM servers
2. **Create Resources** pointing to your LLM or MCP server endpoints
3. **Grant Access** to users or groups via Groups and Security Policies
4. **Configure AI tools** (Cursor, Continue.dev, etc.) to use Twingate-protected endpoints
5. **Monitor usage** via Twingate Admin Console Analytics

## Configuration Values
- No specific env vars on this overview page
- Detailed config in sub-guides: Remote LLM Access Guide, Remote MCP Access Guide

## Related Features
| Feature | Use Case |
|---|---|
| Security Policies | Granular access control per resource |
| Identity Firewall | Protocol-aware security for MCP |
| Service Accounts | Headless/automated AI workload access |
| Analytics | Audit trails for all connections |

## Gotchas
- LLM servers must be configured to listen on network interfaces (not just `localhost/127.0.0.1`) before Twingate can proxy them
- Use Service Accounts for automated/headless AI workloads—regular user accounts are not appropriate for CI/automation
- MCP server security requires additional consideration; see Identity Firewall docs

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/llms/remote-llm)
- [Remote MCP Access Guide](https://www.twingate.com/docs/llms/remote-mcp)
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)