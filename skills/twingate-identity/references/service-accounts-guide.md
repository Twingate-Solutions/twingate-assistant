# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts enable secure machine-to-machine communications in Twingate, using Service Keys instead of standard credentials. They operate via the Twingate Client in headless (non-interactive) mode. Common use cases include SaaS-to-private-resource connections and cross-site private resource connectivity.

## Key Information
- Service Accounts **cannot** fulfill 2FA requirements
- Service Accounts **cannot** use standard credentials (social login, IdP accounts)
- Authentication uses **Service Keys** (expirable, API-manageable)
- Client runs in **headless mode** (non-interactive)

## Use Cases
1. **SaaS → Private Resources**: Connect tools like GitHub Actions, CircleCI, or Codespaces to private infrastructure (K8s clusters, VMs)
2. **Private → Private (cross-site)**: Secure connections between remote systems at different sites using headless Client
3. **Device pool → Private Resources**: When headless Client can't run on target OS, use a gateway VM with IP forwarding

## Prerequisites
- Twingate tenant with Service Account created
- Twingate Client installed (headless mode capable)
- For gateway setup: Ubuntu VM (or compatible Linux)

## Step-by-Step: Ubuntu Gateway Setup

1. Create a Service Account in your Twingate tenant
2. Install Twingate Client in headless mode configured for the Service Account
3. Enable IP forwarding:
   ```bash
   # Uncomment in /etc/sysctl.conf:
   net.ipv4.ip_forward=1
   ```
4. Apply changes:
   ```bash
   sudo sysctl -p
   ```
5. Start Twingate Client in headless mode
6. Configure layer 3 switch/router to route tunneled resource traffic through the Ubuntu gateway VM

## Configuration Values
| Parameter | Value/Location |
|-----------|---------------|
| IP forwarding config | `/etc/sysctl.conf` |
| IP forwarding key | `net.ipv4.ip_forward=1` |
| Apply command | `sudo sysctl -p` |

## Gotchas
- Service Accounts require **Service Keys** (not passwords/SSO) — manage rotation via API for automation
- Gateway VM approach is a workaround only when the target system's OS is incompatible with the Twingate Client
- IP forwarding must be enabled at the OS level **and** routing must be configured at the network layer (L3 switch/router)

## Related Docs
- Headless mode Client setup
- Service Keys documentation
- How to connect CircleCI and GitHub Actions to Private Resources
- How to connect GitHub Codespaces to Private Resources
- Twingate API (for automated Service Key management)