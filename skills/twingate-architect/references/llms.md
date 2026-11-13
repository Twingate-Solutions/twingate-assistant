---
source: https://www.twingate.com/docs/llms
type: docs
fetched: 2026-11-13
source_version: 24db6d29d5c541bc0da472eaa5cc89c028ccb92f12caff42a70d9beac7f24763
trust: official
---

# AI and LLM Access with Twingate

## Summary
This landing page describes how to use Twingate to securely reach private AI infrastructure, including remote LLM servers (Ollama, vLLM) and MCP servers, without exposing them publicly. It outlines the general setup flow and links to two detailed guides: Remote LLM Access and Remote MCP Access.

## Key Information
- **Use cases:**
  - Remote LLM servers on private GPU hosts (Ollama, vLLM, other inference engines).
  - AI coding assistants (Continue.dev, Cursor, Cody) pointed at private LLM endpoints.
  - MCP servers exposing internal tools, data sources, and APIs to AI assistants.
  - Shared AI resources for distributed teams.
  - Centralized GPU infrastructure for cost optimization.
- **Security model:**
  - Zero Trust access for authorized users and devices only.
  - No public IPs required for LLM or MCP servers.
  - Access control through Groups and Security Policies.
  - Connection auditing via Twingate Analytics.
- **Performance:**
  - Peer-to-peer connections where possible.
  - Split tunneling: only traffic to defined Resources goes through Twingate.
- **Guides:**
  - *Remote LLM Access*: configure LLM servers (e.g., Ollama) for network access, create Resources for GPU servers, connect coding assistants, troubleshoot connectivity.
  - *Remote MCP Access*: MCP basics, deploying MCP servers on private networks, configuring assistants to connect via Twingate, security best practices.

## Prerequisites
- A Twingate account and Admin Console access.
- An AI/LLM/MCP server on a private network.
- A host on that network able to run a Twingate Connector.
- Twingate Client installed on user devices (implied).

## Step-by-Step (General Flow)
1. Deploy a Connector on the same network as the AI servers.
2. Create Resources for the LLM or MCP server endpoints.
3. Grant access to appropriate users or groups.
4. Configure AI tools to connect to the endpoints through Twingate.
5. Monitor usage in the Admin Console.

## Configuration Values
None specified on this page. Ports, addresses, and server bind settings are covered in the detailed guides (e.g., Ollama must be configured to listen for network access).

## Gotchas
- The page is an overview only; the actual configuration details (server bind addresses, ports, Resource definitions) are in the linked guides.
- The Connector must have network reachability to the AI server.
- LLM servers like Ollama typically listen on localhost by default, so they need network-access configuration (per the LLM guide's scope).
- The page was last updated about 6 months before the scrape, so verify details against current docs.

## Related Docs
- Remote LLM Access Guide
- Remote MCP Access Guide
- Twingate Architecture
- Security Policies
- Identity Firewall (protocol-aware security for MCP and other services)
- Service Accounts (headless access for automated AI workloads)