---
source: https://www.twingate.com/docs/service-accounts-guide
type: docs
fetched: 2026-08-14
source_version: cb324e699786b12405c723d5b3ba89c5957c880d50ce390692a453fddb384f64
---

# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts enable machine-to-machine secure communications in Twingate, operating via headless mode Client rather than interactive login. They use Service Keys for authentication instead of standard credentials or 2FA. Primary use cases include SaaS-to-private-resource connections and cross-site private resource communication.

## Key Information
- Service Accounts **cannot** fulfill 2FA requirements
- Service Accounts **cannot** use standard credentials (social login, IdP accounts)
- Authentication is handled via **Service Keys** (expirable, API-manageable)
- Client runs in **headless (non-interactive) mode**
- Three main use cases: SaaS↔private resources, private↔private cross-site, device pool↔private resources

## Prerequisites
- Twingate tenant with Service Account created
- Twingate Client installed on target machine
- Service Key generated for the Service Account

## Use Cases

### SaaS to Private Resources
Deploy Twingate Client in headless mode within SaaS CI/CD environments (CircleCI, GitHub Actions, GitHub Codespaces) to reach private infrastructure.

### Private Cross-Site Communication
Deploy headless Client directly on systems needing connectivity to remote private Resources.

### Gateway for Unsupported OS (Pool of Devices)
Use when target system OS is incompatible with Twingate Client:
1. Deploy a separate VM running headless Twingate Client as gateway
2. Enable IP forwarding on the gateway VM
3. Configure layer 3 switch/router to route tunneled traffic through the gateway

## Step-by-Step: Ubuntu Gateway Setup

1. Create a Service Account in your Twingate tenant
2. Install the Twingate Client in headless mode (configured with Service Account)
3. Enable IP forwarding — uncomment `#net.ipv4.ip_forward=1` in `/etc/sysctl.conf`
4. Apply changes:
   ```bash
   sudo sysctl -p
   ```
5. Start the Twingate Client in headless mode
6. Configure layer 3 switch/router to route tunneled resource traffic through the Ubuntu gateway

## Configuration Values
| Setting | Location | Value |
|---|---|---|
| IP forwarding | `/etc/sysctl.conf` | `net.ipv4.ip_forward=1` |

## Gotchas
- Service Keys must be managed actively — set expiration and rotate via API to maintain security posture
- The gateway VM approach adds a network hop; ensure routing is correct at the layer 3 switch/router level
- Headless mode behavior differs from standard Client — interactive prompts and browser-based auth flows will not work

## Related Docs
- Headless mode setup (referenced but not linked inline)
- Service Keys documentation
- How to connect CircleCI and GitHub Actions to Private Resources
- How to connect GitHub Codespaces to Private Resources