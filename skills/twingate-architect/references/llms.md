---
source: https://www.twingate.com/docs/llms
type: docs
fetched: 2026-11-19
source_version: df972d0c7868d170084eab56d0e7fb9e78f5c85c6f2d50deea410e6c6eb15704
trust: official
---

# AI and LLM Access with Twingate

## Summary
This page is an overview of using Twingate to securely reach private AI infrastructure, including remote LLM servers (Ollama, vLLM) and Model Context Protocol (MCP) servers. It lists use cases, benefits, and a five-step getting-started flow, and links to two detailed guides (Remote LLM Access and Remote MCP Access).

## Key Information
- **Use cases:** remote LLM servers on private GPU hosts; AI coding assistants (Continue.dev, Cursor, Cody) pointed at private LLM endpoints; MCP servers exposing internal tools, data, and APIs; distributed dev team access; centralizing GPU workloads.
- **Security model:** Zero Trust access for authorized users and devices; no public IPs needed for LLM or MCP servers; access control through Groups and Security Policies; connection auditing via Twingate Analytics.
- **Performance:** peer-to-peer connections for low latency; split tunneling so only AI traffic traverses Twingate.
- **Simplicity:** no VPN config files or routing tables; Connectors deploy near the AI infrastructure.
- **Linked guides:**
  - *Remote LLM Access:* configuring LLM servers (e.g., Ollama) for network access, creating Resources for GPU servers, connecting coding assistants, troubleshooting connectivity.
  - *Remote MCP Access:* MCP concepts, deploying MCP servers on private networks, configuring assistants to connect via Twingate, security best practices.

## Prerequisites
- A Twingate account and Admin Console access.
- An LLM or MCP server on a private network.
- A Connector deployable on the same network as the AI servers.
- Twingate Client on end-user devices (implied by the access model).

## Step-by-Step
1. Deploy a Connector on the same network as your AI servers.
2. Create Resources for the LLM or MCP server endpoints.
3. Grant access to appropriate users or groups.
4. Configure AI tools to connect to the endpoints through Twingate.
5. Monitor usage in the Twingate Admin Console.

## Configuration Values
None are specified on this page. Ports, addresses, and server settings (for example, making Ollama listen on a non-loopback interface) are covered in the linked guides.

## Gotchas
- This page is only an overview; implementation details such as server bind addresses, Resource definitions, and troubleshooting live in the sub-guides.
- The Connector must have network reachability to the AI servers, so place it on the same network.
- For headless or automated AI workloads, use Service Accounts rather than user credentials.

## Related Docs
- Remote LLM Access Guide
- Remote MCP Access Guide
- Twingate Architecture
- Security Policies
- Privileged Access Management (protocol-aware security for MCP and other services)
- Service Accounts (headless access for AI workloads)