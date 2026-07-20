# Remote MCP Access with Twingate

## Summary
Securely connect local IDEs to self-hosted remote MCP (Model Context Protocol) servers using Twingate as an encrypted private network layer. Avoids exposing MCP server ports to the public internet while maintaining seamless developer access. No traditional VPN or inbound firewall rules required.

## Key Information
- MCP server binds to `localhost` only — Twingate Connector proxies traffic without public port exposure
- Twingate Connector makes outbound-only connections; no inbound firewall rules needed
- IDE connects using the remote server's internal IP as if it were local
- Supports any cloud VM (AWS, GCP, DigitalOcean) or on-prem server
- Compatible with VS Code, Cursor, JetBrains IDEs

## Prerequisites
- Twingate account (free tier available)
- Remote VM/server with MCP server installed
- Twingate client installed on local developer machine
- MCP-compatible IDE

## Step-by-Step

### Remote Server Setup
1. Install and start your MCP server on the remote machine
2. Configure MCP server to listen on `localhost` only — **not** `0.0.0.0`

### Twingate Configuration
3. In Twingate admin console: create a **Remote Network** (e.g., `mcp-dev-network`)
4. Add a **Connector** to the network; run the generated deployment script on the remote server
5. Add a **Resource** with:
   - **Label:** `Remote MCP Server`
   - **Address:** Internal IP of the remote machine
   - **Port:** MCP server port (e.g., `65432`)
   - **Protocol:** TCP
6. Assign user/team access to the Resource

### Local IDE Setup
7. Install and sign in to Twingate client (Windows/macOS/Linux)
8. Configure IDE MCP connection using the remote server's **internal IP** and port (e.g., `{internal_ip}:65432`)

## Configuration Values

| Parameter | Value |
|-----------|-------|
| MCP server bind address | `127.0.0.1` (localhost only) |
| MCP server port (example) | `65432` |
| Resource protocol | `TCP` |
| Twingate network name | User-defined (e.g., `mcp-dev-network`) |

## Gotchas
- **Never bind MCP server to `0.0.0.0`** — defeats the entire security model
- IDE config format varies (JSON files vs. UI panels) — check IDE-specific docs for exact syntax
- Twingate client must be running on the local machine for routing to work
- Internal IP used in IDE config, not a public IP or hostname

## Related Docs
- [Twingate Getting Started](https://www.twingate.com/docs)
- [Model Context Protocol (MCP) specification](https://modelcontextprotocol.io)
- Twingate Connector deployment documentation
- IDE-specific MCP configuration guides (VS Code, Cursor, JetBrains)