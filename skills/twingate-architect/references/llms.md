# AI and LLM Access with Twingate

## Summary
Twingate provides Zero Trust network access to private AI infrastructure including LLM servers, GPU instances, and MCP servers. It enables secure access without exposing endpoints publicly, using Connectors deployed near AI resources. Supports tools like Ollama, vLLM, Continue.dev, Cursor, and MCP-compatible AI assistants.

## Key Information
- Supports remote LLM servers (Ollama, vLLM), AI coding assistants (Continue.dev, Cursor, Cody), and MCP servers
- Traffic uses split tunneling — only AI infrastructure traffic routes through Twingate
- No public IP required for LLM/MCP servers
- Peer-to-peer optimized connections for low latency
- Access control via Groups and Security Policies
- Usage auditable via Twingate Analytics

## Prerequisites
- Twingate account with Admin Console access
- Connector deployable on same network as AI server
- AI servers (LLM/MCP) running on private network

## Step-by-Step
1. **Deploy a Connector** on the same network as your AI/LLM/MCP server
2. **Create Resources** pointing to LLM or MCP server endpoints
3. **Grant Access** to users or groups via Admin Console
4. **Configure AI tools** (e.g., Continue.dev, Cursor) to use Twingate-resolved endpoints
5. **Monitor usage** via Twingate Admin Console Analytics

## Configuration Values
- No specific env vars or CLI flags listed on this page
- See sub-guides for endpoint-specific configuration

## Gotchas
- LLM servers must be configured to listen on network interfaces (not just localhost) — covered in Remote LLM Access Guide
- MCP server deployments have specific security considerations — covered in Remote MCP Access Guide

## Related Docs
- [Remote LLM Access Guide](https://www.twingate.com/docs/remote-llm-access)
- [Remote MCP Access Guide](https://www.twingate.com/docs/remote-mcp-access)
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall)
- [Service Accounts](https://www.twingate.com/docs/service-accounts) — for headless/automated AI workloads