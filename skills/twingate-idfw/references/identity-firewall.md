## Twingate Identity Firewall Overview

Identity Firewall (IDFW) extends Twingate's Zero Trust controls **from the network layer (Layer 3/4) to the application layer (Layer 7)** -- propagating user identity and recording sessions for protocol-aware access.

**Availability:**
- Available now for all Twingate plans
- **Free for up to 5 Resources**

**Currently Supported Protocols:**
- **SSH** (Privileged Access for SSH)
- **Kubernetes API** (Privileged Access for Kubernetes)

**On the Roadmap:**
- HTTPS
- Database protocols (PostgreSQL, MySQL, etc.)
- Model Context Protocol (MCP) -- for AI agent / remote MCP server access

**How It Works -- The Twingate Gateway:**
- IDFW introduces the **Twingate Gateway**, an open-source Layer 7 reverse proxy deployed within the customer environment
- Sits between the Connector and the protected Resource
- Authenticates the user via their existing IdP (no separate creds, no static tokens)
- Propagates identity into the protocol (e.g., Kubernetes RBAC sees the actual user, SSH session is tied to the user identity)
- Records sessions for forensic-level audit + replay

**Key Capabilities:**

| Capability | What It Means |
|---|---|
| Unified Identity Enforcement | One IdP login -> identity flows to every Resource (K8s, SSH, etc.) |
| Zero-Standing Access | Just-in-time access based on identity + device posture + context; revoked when no longer needed |
| Session Recording | Every command / API call / query attributed to a specific user; replayable |
| Cost-Effective PAM | No hardware appliances, no separate PAM infrastructure |

**Vs. Twingate Without IDFW:**
- Without IDFW: Twingate gates *network reach* to a Resource. SSH/K8s still authenticate the user via local credentials (kubeconfig, SSH keys/passwords).
- With IDFW: Twingate gates network reach **and** propagates the IdP identity into the protocol -- the Kubernetes audit log shows the actual user, not a shared kubeconfig identity.

**When to Use IDFW:**
- Compliance requirements need command-level audit trails (SOC2, HIPAA, ISO 27001)
- Privileged operations on shared infrastructure (production K8s, jump hosts) where you need session replay
- Replacing legacy PAM solutions (CyberArk, BeyondTrust) for K8s/SSH workflows
- Contractor/vendor access where session recording is required

**Decision: IDFW SSH vs. Smallstep CA**
- /docs/ssh-smallstep -- Older pattern using Smallstep CA + OAuth -- works but requires separate CA infrastructure
- /docs/ssh-privileged-access-overview -- IDFW native SSH -- recommended for new deployments

**Related Docs:**
- /docs/ssh-privileged-access-overview -- IDFW SSH setup
- /docs/kubernetes-access -- IDFW Kubernetes setup
- Open source: github.com/Twingate/kubernetes-access-gateway
