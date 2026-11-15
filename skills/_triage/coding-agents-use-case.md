---
source: https://www.twingate.com/docs/coding-agents-use-case
type: docs
fetched: 2026-11-15
source_version: 2a8aed5e27af7d734a47e1e0955523b75a4c9c2feae36b6d72b031b5ac4e6d98
trust: official
---

<!-- triage: unassigned -->

# Coding Agents Use Case

## Summary
Twingate lets coding agents reach private Resources (internal package registries, staging APIs, dev databases, private Kubernetes API servers) without exposing them to the internet. How the agent connects depends on where it runs: locally it uses the developer's Twingate Client, while cloud and self-hosted agents use the headless Client authenticated as a Service.

## Key Information
- **Example agent uses:** run the app against staging and E2E tests before opening a PR; read schemas, run migrations and integration tests on PostgreSQL/MySQL/MongoDB; install from internal registries and clone from self-hosted Git; call internal MCP servers, LLM gateways, ticketing/docs systems; run `kubectl` against non-public dev clusters.
- **Service:** a Twingate account for automated processes. It authenticates with a Service Key rather than a user sign-in.
- **Headless Client:** a Client with no UI, used by cloud and self-hosted agents.

### Deployment models
| Model | Examples | Connectivity | Tradeoffs |
|---|---|---|---|
| Local | Claude Code, Codex CLI, Cursor | Developer's Twingate Client, under the developer's Security Policies | No setup. The agent inherits all of the developer's access and only works while the machine is awake. |
| Cloud | Devin, Cursor cloud agents; sandbox providers such as Depot, Daytona | Headless Client in the sandbox with a Service Key | Unattended and parallel. Some platforms lock down sandboxes so the Client can't run. |
| Self-hosted | Devin Outposts, Cursor self-hosted machines | Headless Client on your own VMs or Kubernetes | Most control, but you maintain the infrastructure. |

- If a platform blocks the Client, route commands to a sandbox provider (Depot, Daytona) if the platform supports it. Otherwise, use self-hosted.

## Prerequisites
- A Twingate account with Resources defined.
- For cloud/self-hosted: a Service with assigned Resources and a Service Key.
- Ability to run the headless Client in the sandbox or VM.

## Steps (cloud/self-hosted, general flow)
1. Create a Service and assign only the needed Resources (specific hostnames and ports).
2. Generate a Service Key, ideally with an expiration date. Use one key per agent platform.
3. Run the headless Client in the sandbox with the Service Key (see the Linux Headless Mode guide).
4. Use Userspace Networking if the sandbox lacks the privileges for a standard setup (see that guide).

## Configuration Values
None specified on this page. Service Keys and Services can be managed via Terraform, Pulumi, or the Admin API.

## Gotchas
- Local agents inherit the full access of the developer and stop when the machine sleeps.
- Some agent platforms restrict sandboxes so the Client can't run.
- Self-hosting means you run and maintain the infrastructure.

## Benefits
- A Service restricts the agent to its assigned Resources, and the sandbox gets no address on your private network.
- Connectors make only outbound connections, so there are no inbound firewall ports or agent-platform IP allowlists.
- Per-platform Service Keys can be revoked independently.
- Employees' existing remote access setup is unaffected.

## Related Docs
- Services
- Linux Headless Mode
- Userspace Networking
- Route Traffic from Kubernetes
- Best Practices for Securing Access to Non-production Environments