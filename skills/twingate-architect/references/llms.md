## AI and LLM Access with Twingate -- Overview

Index page for Twingate's AI infrastructure access use cases. Covers securing remote LLM servers (Ollama, vLLM), AI coding assistant integrations (Continue.dev, Cursor, Cody), and Model Context Protocol (MCP) server access. Links to dedicated guides for Remote LLM Access and Remote MCP Access.

**Key Information**
- Use cases: private GPU servers running LLMs, AI coding assistants connecting to private endpoints, MCP servers on internal networks, distributed dev team access to shared AI resources
- Supported LLM runtimes: Ollama, vLLM, other inference engines
- Supported AI coding tools: Continue.dev, Cursor, Cody
- Standard Twingate pattern: Connector on AI server + Resource for the inference endpoint + Client on developer machine
- Service Accounts can be used for headless/automated AI workloads
- Identity Firewall mentioned for protocol-aware security on MCP and other AI services

**Related Docs**
- /docs/remote-llm-access
- /docs/remote-mcp-access
- /docs/service-accounts-guide
- /docs/identity-firewall
