---
source: https://www.twingate.com/docs/remote-mcp-access
type: docs
fetched: 2026-08-14
source_version: 986fc5f62b27cd5967fb8d9e555a89b745b070c969aaaa41e0bb437bacb9a226
---

# Remote MCP Access with Twingate

## Summary
Twingate secures remote Model Context Protocol (MCP) server connections by creating an encrypted private network tunnel, eliminating the need to expose the MCP server to the public internet. The Connector agent on the remote server makes outbound-only connections, requiring no open inbound firewall ports.

## Key Information
- MCP server listens only on `localhost`/`127.0.0.1` — never on `0.0.0.0`
- Twingate Connector installed on the same host as the MCP server
- IDE uses the remote server's **internal IP** (not localhost) as the MCP endpoint
- Traffic is automatically routed through Twingate when the client is running
- No firewall rule changes required on the remote server

## Prerequisites
- Twingate account (free tier available)
- Remote server (cloud VM or on-prem) with MCP server installed
- Twingate client installed on local dev machine
- MCP-compatible IDE (VS Code, Cursor, JetBrains, etc.)

## Step-by-Step

1. **Install MCP server** on remote machine; configure it to bind to `localhost` only
2. **Create Remote Network** in Twingate admin console (e.g., name: `mcp-dev-network`)
3. **Deploy Connector** on the remote server using the generated script from admin console
4. **Add Resource** in Twingate admin console:
   - Label: `Remote MCP Server`
   - Address: internal IP of remote server
   - Port: MCP server port (e.g., `65432`)
   - Protocol: `TCP`
5. **Assign users/groups** access to the Resource
6. **Install Twingate client** on local machine; sign in
7. **Configure IDE** MCP settings to point to `{internal_ip}:{port}` (e.g., `65432`)

## Configuration Values

| Field | Value |
|-------|-------|
| MCP server bind address | `127.0.0.1` or `localhost` |
| Twingate Resource address | Internal IP of remote server |
| Twingate Resource port | MCP server port (e.g., `65432`) |
| Twingate Resource protocol | `TCP` |

## Gotchas
- **Do not** bind MCP server to `0.0.0.0` — defeats the entire security model
- IDE must use the **internal IP address**, not `localhost` or `127.0.0.1` (those resolve locally, not on the remote)
- Twingate client must be running and authenticated for IDE connectivity to work
- IDE MCP config format varies (JSON files vs. UI panels) — consult IDE-specific docs for exact syntax

## Related Docs
- [Twingate Getting Started](https://www.twingate.com/docs)
- [Model Context Protocol (MCP) specification](https://modelcontextprotocol.io)
- Twingate Connector deployment documentation
- Twingate Resource configuration documentation