# Identity Firewall Overview

**Page Title:** Twingate Identity Firewall

**Summary:** Identity Firewall extends Zero Trust and PAM controls to every user, resource, and agent by propagating IdP identity through a Layer 7 gateway proxy. Access is granted just-in-time and tied to authenticated identity with no static credentials. Currently supports Kubernetes API and SSH, with HTTPS, databases, and MCP planned.

**Key Information:**
- Available on all plans; free for up to 5 Resources
- Core component: **Twingate Gateway** — open-source Layer 7 reverse proxy deployed in-environment
- Identity from IdP flows through to every resource without separate auth tokens
- Session recording and forensic-level audit per user/agent
- Dynamic Zero-Standing Access: permissions auto-revoked when context no longer matches
- Policies enforce identity, device posture, location, and context at access time

**Prerequisites:**
- Existing IdP connected to Twingate
- Twingate Gateway deployed within the target environment

**Protocol Support:**
| Protocol | Status |
|---|---|
| Kubernetes API | Available |
| SSH | Available |
| HTTPS | Planned |
| Databases | Planned |
| MCP (remote servers) | Planned |

**Architecture Notes:**
- Gateway sits in-path as a reverse proxy before the protected resource
- No hardware appliances or complex infrastructure required
- Authentication and policy enforcement happen before requests reach the protected environment

**Gotchas:**
- Gateway must be deployed inside the environment — it is not a cloud-hosted component
- Free tier caps at 5 Resources; plan accordingly for larger deployments
- MCP support is not yet available despite being listed as a roadmap item

**Related Docs:**
- Privileged Access for Kubernetes
- Privileged Access for SSH
- `ssh-installation.md` (local reference)
- `ssh-privileged-access-overview.md` (local reference)