## How Service Accounts Work

Service Accounts authenticate **machines** (not humans) to Twingate. Used for automation, CI/CD, SaaS-to-private connectivity, and headless workloads.

**Key Properties:**
- Cannot fulfill 2FA requirements -- machines can't tap a security key
- Cannot use IdP-based credentials (no SSO, no social login)
- Always run the Twingate Client in **headless mode** (non-interactive)
- Authenticated via **Service Keys** -- file-based credentials with optional expiry

**Service Key Security:**
- Keys can have configurable expiry -- rotate regularly via the Twingate API
- Manage key lifecycle programmatically (see /docs/api-overview)
- Treat the JSON key file as a secret (Vault, AWS Secrets Manager, etc.)

**Common Use Cases:**

### 1. SaaS -> Private Resources (CI/CD, SaaS automation)
- GitHub Actions / CircleCI / GitLab CI runners reach private K8s clusters, databases, internal APIs
- Run Twingate Client in headless mode inside the runner container
- Service Account scoped to only the Resources the pipeline needs
- See: /docs/cicd-pipelines-with-twingate, /docs/example-cicd-configurations, /docs/github-codespaces

### 2. Cross-Site Private-to-Private
- Workload in Site A needs to reach a Resource in Site B (different VPCs, different clouds)
- Install Twingate Client (headless) directly on the source workload
- Service Account authenticates the Client; Resource access controlled via Group membership

### 3. Pool of Devices Without Native Client Support
For systems where the Twingate Client cannot be installed (legacy OS, embedded, etc.):
- Set up a **gateway VM** with the Twingate Client in headless mode
- Enable IP forwarding on the gateway
- Add a static route on a layer 3 switch/router pointing tunneled Resource traffic through the gateway
- Devices on the network reach Twingate Resources via the gateway transparently

**Ubuntu Gateway Setup (Reference):**
1. Create a Service Account in the Twingate Admin Console
2. Install the Twingate Client in headless mode on Ubuntu (using the Service Account key)
3. Enable IP forwarding: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`
4. Apply: `sudo sysctl -p`
5. Start the Twingate Client headless
6. Configure router/switch to send tunneled Resource traffic through this VM as next-hop

**Decision Notes:**
- Service Accounts cannot satisfy MFA -- design Resource Policies that allow no-MFA for Service Account-accessed Resources, or use a separate Group for service accounts
- Don't share keys across multiple machines -- one Service Account per machine for clean audit trails
- For ephemeral CI runners: short-lived keys + automated rotation via the API

**Gotchas:**
- Headless mode = no UI prompts; misconfigured Service Account keys cause silent connection failures -- check logs (e.g., `journalctl -u twingate-client`)
- Linux kernel `net.ipv4.ip_forward` is per-namespace -- containers may not inherit the host's setting
- Gateway VM is a SPOF -- consider deploying multiple gateway VMs for HA in production

**Related Docs:**
- /docs/services-headless-clients -- Headless Client overview
- /docs/linux-headless, /docs/windows-headless -- Platform-specific install
- /docs/cicd-pipelines-with-twingate -- CI/CD pattern
- /docs/aws-ecs-headless-configurations -- ECS headless pattern
- /docs/scim-provisioning-api -- API automation for key management
