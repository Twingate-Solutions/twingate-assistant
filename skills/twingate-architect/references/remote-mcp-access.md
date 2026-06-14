# Remote MCP Access with Twingate

## Summary
Securely connect a local IDE to a self-hosted remote MCP (Model Context Protocol) server using Twingate as a zero-trust connectivity layer. The MCP server listens only on localhost; Twingate handles encrypted routing without exposing public ports.

## Key Information
- MCP server must listen on `localhost` only — never `0.0.0.0`
- Twingate Connector runs on the remote server, making outbound-only connections (no inbound firewall rules needed)
- Traffic is routed: `IDE → Twingate Client → Twingate Network → Connector → localhost:PORT on remote server`
- Compatible with VS Code, Cursor, JetBrains IDEs, and any MCP-compatible tooling
- Works with any cloud VM (AWS, GCP, DigitalOcean) or on-prem server

## Prerequisites
- Twingate account (free tier available)
- Remote server running an MCP-compliant server
- Twingate client installed on local development machine
- Admin access to Twingate console

## Step-by-Step

1. **Configure MCP server** — bind to `localhost` only on the remote machine
2. **Create Remote Network** in Twingate admin console (e.g., name: `mcp-dev-network`)
3. **Deploy Connector** — run the generated script on the remote MCP server
4. **Define Resource** in Twingate admin console:
   - Label: e.g., `Remote MCP Server`
   - Address: internal IP of the remote machine
   - Port: MCP server port (e.g., `65432`)
   - Protocol: `TCP`
5. **Assign users** access to the Resource
6. **Install Twingate client** on local machine, sign in
7. **Configure IDE** to connect to `{internal_ip}:{port}` — Twingate routes automatically

## Configuration Values

| Parameter | Example Value | Notes |
|-----------|---------------|-------|
| Resource Address | `{internal_ip}` | Internal IP of remote server |
| Resource Port | `65432` | Port MCP server listens on |
| Protocol | `TCP` | Required |
| MCP server bind address | `127.0.0.1` | Never `0.0.0.0` |

## Gotchas
- **Do not** set MCP server to listen on `0.0.0.0` — defeats the entire security model
- IDE configuration format varies (JSON files vs. UI panels) — consult IDE-specific docs for exact syntax
- Twingate client must be running and authenticated on local machine before IDE attempts connection
- Access must be explicitly granted per user in Twingate admin console

## Related Docs
- [Twingate Getting Started](https://www.twingate.com/docs)
- [Model Context Protocol specification](https://modelcontextprotocol.io)
- Twingate Connector deployment documentation
- IDE-specific MCP configuration guides (VS Code, Cursor, JetBrains)