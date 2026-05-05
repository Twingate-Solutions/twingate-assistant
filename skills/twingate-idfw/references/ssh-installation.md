## Installing Privileged Access for SSH

How to deploy the Twingate Gateway and configure SSH Resources -- the recommended path is the Twingate Terraform provider, which publishes complete runnable examples.

**Recommended Approach:**
- Use the Twingate Terraform provider with one of the published quick-start examples
- Each example includes the full Terraform config + startup scripts + step-by-step instructions

**Prerequisites:**
- Twingate account with admin privileges
- An existing Remote Network in Twingate
- Terraform installed
- Twingate Client meeting IDFW SSH minimum versions (see /docs/ssh-privileged-access-overview)

**Quick-Start Guides (Local SSH CA):**

| Guide | Cloud | Notes |
|---|---|---|
| Local SSH CA on AWS | AWS EC2 | Fastest to try |
| Local SSH CA on DigitalOcean | DO Droplets | Lowest-cost option |
| Local SSH CA on GCE | Google Compute Engine | If you're already in GCP |

All three use a **Local SSH CA** -- the Gateway holds the SSH CA private key and signs certificates directly. Good for evaluation and simple production setups.

**For Production -- Vault as SSH CA:**
- Use HashiCorp Vault's SSH secrets engine to sign certificates
- Keeps the SSH CA private key off the Gateway disk
- Provides audit logging of every certificate issuance
- See the **Vault integration guide** (linked from this doc)

**What the Terraform Modules Provision:**
- Gateway VM/container with the Twingate Gateway image
- X.509 CA for the Gateway
- SSH CA (local mode by default; configurable for Vault)
- Twingate Resources for each SSH host
- Group / access bindings for SSH Resources
- The Connector that fronts the Gateway's Remote Network

**After Installation:**
- Gateway pod / VM is running
- SSH Resources appear in the Admin Console with type indicating Gateway-served
- Users with Group access can `ssh user@<resource-fqdn-or-ip>` after enabling SSH Auto-Sync in their Twingate Client
- See /docs/ssh-remote-development for VS Code / JetBrains / Cursor IDE setup

**Decision: Local SSH CA vs. Vault**
- **Local CA**: simpler, fewer moving parts -- pick for getting started
- **Vault**: production-grade -- pick if you have compliance requirements (key off-disk), already use Vault, or want central CA management across multiple Gateways

**Gotchas:**
- Don't roll your own Gateway deployment -- use the Terraform modules; they handle Gateway-specific bootstrap (registration with the Twingate Controller, X.509 CA association, log forwarding)
- Plan for **session log retention** -- Gateway writes asciicast logs to stderr; you must forward + store them externally (Fluent Bit / Vector / SIEM)
- For HA, deploy multiple Gateways behind the same Connector / Remote Network

**Related Docs:**
- /docs/ssh-privileged-access-overview -- Concepts + components
- /docs/ssh-remote-development -- IDE integration after Gateway is running
- /docs/identity-firewall -- IDFW overview
