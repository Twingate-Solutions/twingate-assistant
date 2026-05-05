## Headless Clients

How to run Twingate Clients in headless (non-interactive) mode using a Service Account key, for use in CI/CD pipelines, containers, agents, and other non-human workloads.

**Supported Platforms:**
- **Linux** -- full headless mode (TUN networking)
- **Windows** -- headless mode supported
- **Linux userspace mode** -- HTTP/HTTPS proxy, no kernel/TUN required (works inside containers without elevated privileges)

**Authentication:**
- Headless Clients authenticate via a Service Account key (not user credentials)
- Service key file is mounted/written to the Client's expected path (e.g., `/etc/twingate/service_key.json` on Linux)

**Use Cases (linked from this doc):**
- CI/CD pipelines that need to reach private resources (GitHub Actions, Jenkins, GitLab runners)
- ECS / containerized workloads (see /docs/aws-ecs-headless-configurations)
- AI agents, frontend apps, batch jobs that need private backend access

**Mode Selection:**
- Use **TUN (full headless)** when the workload needs full network connectivity (TCP/UDP/ICMP) and the host supports kernel modules / `/dev/net/tun` / `CAP_NET_ADMIN`
- Use **userspace** when the environment cannot grant kernel privileges (e.g., AWS Fargate) and traffic is HTTP/HTTPS only

**Related Docs:**
- /docs/linux-headless -- Linux headless install instructions
- /docs/windows-headless -- Windows headless install instructions
- /docs/linux-userspace-networking -- Userspace (proxy) mode details
- /docs/cicd-pipelines-with-twingate -- CI/CD configuration examples
- /docs/aws-ecs-headless-configurations -- ECS-specific deployment patterns
- /docs/service-accounts-guide -- Service Account key creation and rotation
