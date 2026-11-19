---
source: https://www.twingate.com/docs/coding-agents-use-case
type: docs
fetched: 2026-11-19
source_version: 9391818a05f2c739ec49f1840d97e27987280b8a3d2c8af32688b7272475cd7b
trust: official
---

<!-- triage: unassigned -->

# Page Title
Coding Agents Use Case (Twingate Docs)

## Summary
Twingate lets coding agents reach private Resources (internal package registries, staging APIs, dev databases, private Kubernetes API servers) without exposing them to the internet. How the agent connects depends on where it runs: local agents use the developer's Twingate Client, while cloud and self-hosted agents use the headless Client authenticated as a Service.

## Key Information
- **Example agent uses:** run apps against staging and call internal APIs, E2E tests before opening a PR; read schemas, run migrations and integration tests on PostgreSQL/MySQL/MongoDB; install from internal registries and clone from self-hosted Git; call internal MCP servers, LLM gateways, ticketing/docs systems; run `kubectl` against non-public dev clusters.
- **Service:** a Twingate account for automated processes, authenticated with a Service Key rather than a user sign-in.
- **Headless Client:** Client without a UI, connects as a Service.
- **Local agents** (Claude Code, Codex CLI, Cursor): traffic goes through the developer's Client under their Security Policies. No extra setup, but the agent inherits all of the developer's access and only works while the machine is awake.
- **Cloud agents:** run in a hosted sandbox (VM/container). Run the headless Client with a Service Key; the agent accesses only Resources assigned to that Service. Devin and Cursor cloud agents let you run the Client in their sandboxes. Some platforms lock sandboxes down; if the platform can send commands to a sandbox provider (Depot, Daytona), run the Client there.
- **Self-hosted agents:** sandbox runs on infrastructure you manage (e.g., Devin Outposts, Cursor self-hosted machines). Use when the Client can't run in a platform/provider sandbox or agents must run on machines you control. Set up the headless Client as in cloud sandboxes; you maintain the infrastructure.
- **Benefits:** least-privilege access via Service assignments (specific hostnames/ports); sandbox gets no address on your private network; Connectors are outbound-only, so no inbound firewall rules or agent-platform IP allowlists; per-platform Service Keys with expiration and independent revocation; coexists with existing employee remote access; manage Services/Keys via Terraform, Pulumi, or the Admin API.

## Prerequisites
- A Twingate account with Resources defined and a Connector deployed.
- For cloud/self-hosted agents: a Service, a Service Key, and Resources assigned to the Service.
- A sandbox where the headless Client can run.

## Step-by-Step (general flow implied)
1. Choose agent location: local, cloud, or self-hosted.
2. Local: nothing extra; ensure the developer's Client is connected.
3. Cloud/self-hosted: create a Service, assign Resources, and generate a Service Key (set an expiration).
4. Run the headless Client in the sandbox using the Service Key.
5. If the platform blocks the Client, route commands to a sandbox provider (Depot, Daytona) and run it there.

## Configuration Values
None specified on this page. See the Linux Headless Mode and Services guides for specifics.

## Gotchas
- Local agents get all of the developer's access, not a restricted subset.
- Local agents stop working when the developer's machine sleeps.
- Some agent platforms' sandboxes prevent the Client from running.
- Self-hosted setups require you to run and maintain the infrastructure.
- Use a separate Service Key per agent platform so one can be revoked without affecting others.

## Related Docs
- Access Private Resources from Daytona Sandboxes
- Access Private Resources from RWX Sandboxes
- Services
- Linux Headless Mode
- Userspace Networking
- Route Traffic from Kubernetes
- Best Practices for Securing Access to Non-production Environments