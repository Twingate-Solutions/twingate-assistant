# Remote MCP Access with Twingate

## Summary
Twingate secures connections between local IDEs and self-hosted remote MCP (Model Context Protocol) servers without exposing ports to the public internet. Traffic is routed through an encrypted private network via a Twingate Connector installed on the remote server. This eliminates the need for traditional VPNs or open inbound firewall rules.

## Key Information
- MCP server must listen on `localhost` only — never `0.0.0.0`
- Twingate Connector makes outbound-only connections; no inbound ports need to be opened
- IDE connects using the remote machine's **internal IP** (not localhost, not public IP)
- Compatible with VS Code, Cursor, JetBrains IDEs, and any MCP-compatible tooling
- Works with any cloud provider (AWS, GCP, DigitalOcean) or on-prem servers

## Prerequisites
- A remote server (VM or bare metal) running an MCP-compliant server
- Twingate account (free tier available)
- Twingate client installed on local dev machine
- MCP server configured to bind to `127.0.0.1` only

## Step-by-Step

1. **Install MCP server** on remote machine; configure it to listen on `localhost` only
2. **Create Remote Network** in Twingate admin console (e.g., name: `mcp-dev-network`)
3. **Deploy Connector** — run the generated script on the remote MCP server machine
4. **Define a Resource** in Twingate admin:
   - Label: `Remote MCP Server`
   - Address: internal IP of remote machine
   - Port: MCP server port (e.g., `65432`)
   - Protocol: `TCP`
5. **Assign users** to the Resource
6. **Install Twingate client** on local machine; sign in
7. **Configure IDE** to point to `{internal_ip}:{port}` — Twingate routes traffic automatically

## Configuration Values

| Parameter | Value |
|-----------|-------|
| MCP server bind address | `127.0.0.1` (localhost only) |
| Resource address | Internal IP of remote server |
| Resource port | Port MCP server listens on (e.g., `65432`) |
| Resource protocol | `TCP` |

## Gotchas
- **Do not** bind MCP server to `0.0.0.0` — defeats the entire security model
- IDE config format varies (JSON file vs. UI panel) — check IDE-specific docs for exact syntax
- Twingate client must be running locally before IDE attempts to connect
- Internal IP in the Resource config is what the IDE uses as the target address — not `localhost`

## Related Docs
- [Twingate Getting Started](https://www.twingate.com/docs/)
- [Model Context Protocol specification](https://modelcontextprotocol.io/)
- Twingate Connector deployment documentation