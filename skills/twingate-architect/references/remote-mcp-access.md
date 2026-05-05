# Remote MCP Access with Twingate

## Page Title
Remote MCP Access with Twingate

## Summary
Twingate secures connections between local IDEs and self-hosted remote MCP (Model Context Protocol) servers without exposing ports to the public internet. Traffic routes through an encrypted private network via a Twingate Connector installed on the remote server. This eliminates the need for traditional VPNs or open firewall rules.

## Key Information
- MCP server must listen on `localhost` only — never `0.0.0.0`
- Twingate Connector establishes **outbound-only** connections; no inbound firewall ports required
- Compatible IDEs: VS Code, Cursor, JetBrains IDEs (any MCP-compatible tool)
- Works with any cloud VM (AWS, GCP, DigitalOcean) or on-prem server
- Access control is identity-based (zero-trust), not network-location-based

## Prerequisites
- Remote server running an MCP-compliant server process
- Twingate account (free tier available)
- Twingate Client installed on local development machine
- Twingate Connector deployed on remote MCP server

## Step-by-Step

1. **Configure MCP server** — bind to `localhost` (127.0.0.1) only on chosen port (e.g., `65432`)
2. **Create Remote Network** in Twingate admin console (e.g., name: `mcp-dev-network`)
3. **Deploy Connector** — run the generated script on the remote MCP server machine
4. **Add Resource** in Twingate admin console:
   - Label: `Remote MCP Server`
   - Address: internal IP of remote machine
   - Port: MCP server port (e.g., `65432`)
   - Protocol: `TCP`
5. **Assign users** to the Resource in admin console
6. **Install Twingate Client** on local machine and sign in
7. **Configure IDE** — set MCP server address to `{internal_ip}:{port}` (e.g., `65432`); Twingate routes traffic automatically

## Configuration Values

| Parameter | Value |
|-----------|-------|
| MCP server bind address | `127.0.0.1` (localhost only) |
| Resource protocol | `TCP` |
| Example port | `65432` |
| IDE server address | `{internal_ip}:{port}` |

## Gotchas
- **Do not** set MCP server to listen on `0.0.0.0` — this defeats the entire security model
- IDE configuration format varies (JSON files vs. UI panels) — consult IDE-specific docs for exact syntax
- Twingate Client must be running in background on local machine for routing to work
- Internal IP used in IDE config is the Twingate-routed address, not a public IP

## Related Docs
- [Twingate website / free account](https://www.twingate.com)
- Model Context Protocol (MCP) specification documentation
- Twingate Connector deployment documentation
- Twingate admin console Resource configuration