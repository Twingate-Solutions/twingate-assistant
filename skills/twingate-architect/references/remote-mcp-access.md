## Remote MCP Access with Twingate

Explains how to secure a self-hosted Model Context Protocol (MCP) server behind Twingate to prevent public internet exposure. The Connector runs on the same machine as the MCP server; the IDE connects via the server's internal IP through the Twingate tunnel.

**Key Information:**
- MCP server must listen on `localhost` only -- do not bind to `0.0.0.0`
- Connector is installed on the remote MCP server and creates an outbound-only connection -- no inbound firewall ports needed
- Resource is configured with the server's internal IP and port (e.g., `65432`) with TCP protocol
- IDE uses the internal IP address as the MCP server address -- Twingate routes traffic transparently
- Works with VS Code, Cursor, JetBrains, and any MCP-compatible IDE

**Prerequisites:**
- Twingate account and admin access
- Remote VM or server running an MCP-compliant server
- Twingate Client installed on the developer's local machine

**Step-by-Step:**
1. Install and run MCP server on remote machine, configured to listen on `localhost` only
2. In Twingate admin console, create a Remote Network (e.g., `mcp-dev-network`)
3. Deploy a Connector on the remote MCP server via the generated script
4. Add a Resource: label it clearly, set address to the server's internal IP, set port to the MCP server's port, allow TCP
5. Assign the Resource to a Group and add authorized users
6. Install and sign in to the Twingate Client on the local machine
7. Configure the IDE MCP connection to use the internal IP and port

**Gotchas:**
- Configuring the MCP server to listen on `0.0.0.0` defeats the entire security model
- The IDE configuration format varies (JSON config files vs. UI panels) -- consult IDE documentation for the exact syntax
- No inbound firewall ports need to be opened on the remote server

**Related Docs:**
- /docs/connector -- Connector installation and deployment
- /docs/remote-networks -- Creating Remote Networks
- /docs/resources -- Defining Resources
