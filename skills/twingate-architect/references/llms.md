# AI and LLM Access with Twingate

## Summary
Twingate provides Zero Trust network access to private AI infrastructure including LLM servers, MCP servers, and GPU compute resources. It eliminates public exposure of AI endpoints while enabling distributed team access with audit logging and granular controls.

## Key Information
- Supports remote LLM inference servers (Ollama, vLLM, etc.) on private GPU infrastructure
- Supports Model Context Protocol (MCP) servers for AI assistant tool integration
- Compatible with AI coding assistants: Continue.dev, Cursor, Cody
- Uses peer-to-peer connections with split tunneling (only AI traffic routed through Twingate)
- No public IP required on AI servers

## Prerequisites
- Twingate account with Admin Console access
- Connector deployable on same network as AI servers
- AI infrastructure (LLM server or MCP server) running on private network

## Step-by-Step (Getting Started)
1. **Deploy a Connector** on the same network as your AI servers
2. **Create Resources** for your LLM or MCP server endpoints
3. **Grant Access** to appropriate users or groups
4. **Configure AI tools** to connect through Twingate
5. **Monitor usage** through the Twingate Admin Console

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Refer to sub-guides for endpoint-specific configuration

## Use Cases Covered (Sub-guides)
| Use Case | Guide |
|----------|-------|
| Remote LLM servers (Ollama, vLLM) | Remote LLM Access Guide |
| MCP server access | Remote MCP Access Guide |

## Gotchas
- This page is an index only — implementation details are in the sub-guides
- Split tunneling means only AI-destined traffic routes through Twingate; verify tool routing if experiencing connectivity issues
- MCP server access may require Identity Firewall for protocol-aware security

## Related Docs
- [Twingate Architecture](https://www.twingate.com/docs/architecture)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Identity Firewall](https://www.twingate.com/docs/identity-firewall) — recommended for MCP deployments
- [Service Accounts](https://www.twingate.com/docs/service-accounts) — for headless/automated AI workloads
- Remote LLM Access Guide
- Remote MCP Access Guide