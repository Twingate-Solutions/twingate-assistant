# Remote MCP Access with Twingate

## Summary
Twingate secures remote Model Context Protocol (MCP) server connections by creating a private encrypted network between local IDEs and remote servers. This eliminates the need to expose MCP server ports to the public internet while allowing seamless developer access.

## Key Information
- MCP server should bind to `localhost` only—never `0.0.0.0`
- Twingate Connector runs on the remote server and makes outbound-only connections (no inbound firewall ports required)
- Traffic is routed: IDE → Twingate Client → Twingate Network → Connector → `127.0.0.1:{port}` on remote server
- Compatible IDEs: VS Code, Cursor, JetBrains IDEs

## Prerequisites
- Remote server (cloud VM or on-prem) running an MCP-compliant server
- Twingate account (free tier available)
- Twingate Client installed on local machine
- Twingate Connector deployed on remote server

## Step-by-Step

1. **Configure MCP server** to listen on `localhost` only (not `0.0.0.0`)
2. **Create Remote Network** in Twingate admin console (e.g., `mcp-dev-network`)
3. **Deploy Connector** on remote server using generated deployment script from admin console
4. **Add Resource** in Twingate admin console:
   - Label: `Remote MCP Server`
   - Address: internal IP of remote machine
   - Port: MCP server port (e.g., `65432`)
   - Protocol: `TCP`
5. **Assign users** access to the Resource
6. **Install Twingate Client** on local machine and sign in
7. **Configure IDE** to connect to `{internal_ip}:{port}` (e.g., `65432`)—Twingate client handles routing automatically

## Configuration Values

| Field | Value |
|-------|-------|
| MCP server bind address | `127.0.0.1` (localhost only) |
| Resource Protocol | TCP |
| Example port | `65432` |
| IDE connection address | `{internal_ip}:{port}` |

## Gotchas
- Do **not** bind MCP server to `0.0.0.0`—defeats the security model
- IDE config format varies (JSON files vs. UI panels)—check IDE-specific docs for exact syntax
- Twingate Client must be running and authenticated for IDE routing to work

## Related Docs
- [Twingate website](https://www.twingate.com) — account creation
- MCP server documentation — server-specific install/config instructions
- Twingate admin console — Connector deployment scripts, Resource management