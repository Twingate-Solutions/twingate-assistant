---
source: https://www.twingate.com/docs/service-accounts-guide
type: docs
fetched: 2026-10-04
source_version: 2050677c9d0001bcf4c6a39b5a1de4047cc22f59d43e34c08346303170371e42
trust: official
---

# How Service Accounts Work

## Summary
Service Accounts enable machine-to-machine secure communication in Twingate, replacing human credentials with Service Keys. They run the Twingate Client in headless (non-interactive) mode and are suited for SaaS-to-private-infrastructure, site-to-site, and device-pool-to-resource connectivity patterns.

---

## Key Information
- Service Accounts **cannot** fulfill 2FA requirements
- Service Accounts **cannot** use standard credentials (social login, IdP accounts)
- Authentication uses **Service Keys**, which support expiration and API-based lifecycle management
- Client runs in **headless mode** (non-interactive)

---

## Use Cases
| Scenario | Approach |
|---|---|
| SaaS (CircleCI, GitHub Actions) → private Resources | Deploy Client in headless mode on SaaS runner/agent |
| Private Resource ↔ Private Resource (different sites) | Deploy Client in headless mode on the connecting system |
| Incompatible OS devices → private Resources | Deploy a gateway VM running Client in headless mode with IP forwarding |

---

## Ubuntu Gateway Setup (Step-by-Step)

For device pools where the Client cannot run directly on the source system:

1. Create a Service Account in your Twingate tenant (Admin Console)
2. Install the Twingate Client in headless mode, configured to use the Service Account's Service Key
3. Enable IP forwarding — uncomment the following line in `/etc/sysctl.conf`:
   ```
   net.ipv4.ip_forward=1
   ```
4. Apply the change:
   ```bash
   sudo sysctl -p
   ```
5. Start the Twingate Client in headless mode
6. Configure a route on a Layer 3 switch/router to direct tunneled resource traffic through the Ubuntu gateway VM

---

## Prerequisites
- A Twingate tenant with admin access
- Service Account created via Admin Console or API
- Service Key generated and available
- Target Resources already defined in Twingate
- For gateway pattern: Ubuntu VM with network routing access

---

## Configuration Values
- **Service Key**: replaces user credentials; set expiration via API
- **Headless mode**: Client flag/mode — see headless mode documentation for CLI parameters
- **IP forwarding sysctl key**: `net.ipv4.ip_forward=1`

---

## Gotchas
- Service Accounts have no 2FA path — security relies entirely on Service Key rotation and expiration policies
- If the source OS is incompatible with the Twingate Client, a gateway VM is required; direct deployment is preferred when possible
- IP forwarding must be applied persistently via `sysctl.conf`; runtime-only changes won't survive reboots

---

## Related Docs
- Headless mode Client setup
- Service Keys management
- How to connect CircleCI and GitHub Actions to Private Resources
- How to connect GitHub Codespaces to Private Resources
- Twingate API (for automated Service Key management)