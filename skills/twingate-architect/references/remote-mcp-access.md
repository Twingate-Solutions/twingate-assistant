# Remote MCP Access with Twingate

## Summary
Secure remote Model Context Protocol (MCP) servers using Twingate as a zero-trust connectivity layer instead of exposing ports publicly. Twingate creates an encrypted private network between the developer's local IDE and the remote MCP server, with no inbound firewall ports required.

## Key Information
- MCP server should listen on `localhost` only — never `0.0.0.0`
- Twingate Connector runs on the remote server, makes outbound-only connections (no open inbound ports)
- Traffic routes: `IDE → Twingate Client → Twingate Network → Connector → MCP Server (127.0.0.1)`
- Compatible IDEs: VS Code, Cursor, JetBrains IDEs
- Compatible hosts: any cloud VM (AWS, GCP, DigitalOcean) or on-prem server

## Prerequisites
- Twingate account (free tier available)
- Remote server/VM running an MCP-compliant server
- Twingate client installed on local development machine
- MCP server configured to bind to `localhost` only

## Step-by-Step

1. **Install MCP server** on remote machine; configure it to listen on `localhost` only
2. **Create Remote Network** in Twingate admin console (e.g., name: `mcp-dev-network`)
3. **Deploy Connector** on remote server using generated deployment script from admin console
4. **Add Resource** in Twingate admin console:
   - Label: `Remote MCP Server`
   - Address: internal IP of remote machine
   - Port: MCP server port (e.g., `65432`)
   - Protocol: `TCP`
5. **Assign users** access to the Resource
6. **Install Twingate client** on local machine; sign in
7. **Configure IDE** MCP connection using the remote server's internal IP and port

## Configuration Values

| Parameter | Value |
|-----------|-------|
| MCP server bind address | `127.0.0.1` (localhost only) |
| Resource address | Internal IP of remote server |
| Resource port | e.g., `65432` (MCP server's port) |
| Resource protocol | `TCP` |

## Gotchas
- **Never** bind MCP server to `0.0.0.0` — defeats the entire security model
- IDE config format varies (JSON files vs. UI panels) — consult specific IDE docs for exact syntax
- Twingate client must be running and authenticated before IDE can reach the MCP server
- Access must be explicitly granted per user to the Resource in admin console

## Related Docs
- [Twingate Getting Started](https://www.twingate.com/docs)
- [Model Context Protocol (MCP) specification](https://modelcontextprotocol.io)
- Twingate Connector deployment documentation
- Individual IDE MCP configuration documentation (VS Code, Cursor, JetBrains)