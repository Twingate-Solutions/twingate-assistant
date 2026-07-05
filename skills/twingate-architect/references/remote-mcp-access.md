# Remote MCP Access with Twingate

## Summary
Securely connect local IDEs to self-hosted remote MCP (Model Context Protocol) servers using Twingate as a zero-trust network layer. The MCP server listens only on localhost; Twingate handles encrypted routing without exposing public ports.

## Key Information
- MCP server binds to `localhost` only — never `0.0.0.0`
- Twingate Connector runs on the remote server, makes outbound-only connections (no inbound firewall rules needed)
- IDE uses the remote server's internal IP as if it were local
- Supports any cloud VM (AWS, GCP, DigitalOcean) or on-prem server
- Compatible IDEs: VS Code, Cursor, JetBrains IDEs

## Prerequisites
- Twingate account (free tier available)
- Remote server with MCP server installed and running
- Twingate client installed on local machine
- Twingate admin console access

## Step-by-Step

### Remote Server Setup
1. Install your MCP server per its documentation
2. Configure MCP server to listen on `localhost` only (not `0.0.0.0`)

### Twingate Configuration
3. In Twingate admin console, create a **Remote Network** (e.g., `mcp-dev-network`)
4. Add a **Connector** — run the generated deployment script on the remote MCP server
5. Add a **Resource**:
   - Label: `Remote MCP Server`
   - Address: internal IP of the remote machine
   - Port: MCP server port (e.g., `65432`)
   - Protocol: `TCP`
6. Assign user/team access to the Resource

### Local IDE Setup
7. Install and sign in to Twingate client (Windows/macOS/Linux)
8. In IDE MCP settings, set server address to the remote machine's internal IP and port `65432`
9. Twingate client auto-routes traffic through the secure tunnel

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MCP server bind address | `127.0.0.1` (localhost only) |
| Resource protocol | `TCP` |
| Example port | `65432` |
| IDE server address | `{internal_ip}:{port}` |

## Gotchas
- **Do not** set MCP server to listen on `0.0.0.0` — defeats the entire security model
- IDE config format varies (JSON files vs. UI panels) — consult IDE-specific docs for exact syntax
- Twingate client must be running and authenticated before IDE can reach the resource
- Access is identity-based; users must be explicitly granted access to the Resource in admin console

## Related Docs
- [Twingate website](https://www.twingate.com) — account setup
- Model Context Protocol specification
- Twingate Connector deployment documentation
- IDE-specific MCP configuration guides (VS Code, Cursor, JetBrains)