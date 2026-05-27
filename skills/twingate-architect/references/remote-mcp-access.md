# Remote MCP Access with Twingate

## Summary
Twingate secures remote Model Context Protocol (MCP) server connections by creating an encrypted private network between a local IDE and a remote MCP server. This eliminates the need to expose the MCP server to the public internet while maintaining seamless developer access.

## Key Information
- MCP server runs on remote VM/cloud instance, bound to `localhost` only
- Twingate Connector installed on remote server creates outbound-only connection (no inbound firewall ports required)
- Local IDE connects using the remote server's internal IP — Twingate routes traffic transparently
- Supports any MCP-compatible IDE: VS Code, Cursor, JetBrains

## Prerequisites
- Remote server (AWS, GCP, DigitalOcean, or on-prem VM) with MCP server installed
- Twingate account (free tier available)
- Twingate client installed on local development machine
- MCP server configured to listen on `localhost` only

## Step-by-Step

1. **Configure MCP server** — bind to `localhost` (not `0.0.0.0`)
2. **Create Remote Network** in Twingate admin console (e.g., name: `mcp-dev-network`)
3. **Deploy Connector** — run generated script on remote MCP server machine
4. **Define Resource** in Twingate admin console:
   - Label: `Remote MCP Server`
   - Address: internal IP of remote machine
   - Port: MCP server port (e.g., `65432`)
   - Protocol: `TCP`
5. **Assign users** access to the Resource
6. **Install Twingate client** on local machine, sign in
7. **Configure IDE** to connect to `{internal_ip}:{port}` — Twingate routes automatically

## Configuration Values

| Parameter | Value |
|-----------|-------|
| MCP server bind address | `127.0.0.1` / `localhost` |
| Resource protocol | `TCP` |
| Example port | `65432` |
| Twingate traffic routing | Automatic when client is running |

## Gotchas
- **Never** bind MCP server to `0.0.0.0` — defeats the entire security model
- IDE configuration format varies (JSON files vs. UI panels) — consult IDE-specific docs for exact syntax
- Twingate client must be running on local machine for routing to work
- Connector must remain running on remote server to maintain connectivity

## Related Docs
- [Twingate website](https://www.twingate.com) — account setup
- MCP server documentation — server installation and configuration
- Twingate client downloads — Windows, macOS, Linux
- Twingate admin console — Connector deployment scripts