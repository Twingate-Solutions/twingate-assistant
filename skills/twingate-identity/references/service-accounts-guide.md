# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts enable machine-to-machine secure communications in Twingate, using headless mode Twingate Clients instead of interactive logins. They authenticate via Service Keys rather than standard credentials or identity providers. Common use cases include SaaS-to-private-resource connections, cross-site private resource connections, and gateway setups for unsupported OS devices.

## Key Information
- Service Accounts **cannot** fulfill 2FA requirements
- Service Accounts **cannot** use standard credentials (social login, IdP accounts)
- Authentication uses **Service Keys** (expirable, API-manageable)
- Twingate Client runs in **headless (non-interactive) mode**
- Three primary use cases:
  1. SaaS apps (GitHub Actions, CircleCI) → private resources
  2. Private resource → private resource across different sites
  3. Pool of devices → private resources via gateway VM

## Prerequisites
- Twingate tenant with Service Account creation permissions
- Twingate Client compatible OS (or a gateway VM if the target system is incompatible)
- For Ubuntu gateway: root/sudo access

## Step-by-Step: Ubuntu Gateway Setup
1. Create a Service Account in your Twingate tenant
2. Install Twingate Client in headless mode, configured with the Service Account
3. Enable IP forwarding: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`
4. Apply changes: `sudo sysctl -p`
5. Start Twingate Client in headless mode
6. Configure a route on a Layer 3 switch/router to direct tunneled resource traffic through the Ubuntu gateway VM

## Configuration Values
| Item | Value/Location |
|------|---------------|
| IP forwarding config | `/etc/sysctl.conf` |
| IP forwarding directive | `net.ipv4.ip_forward=1` (uncomment to enable) |
| Apply sysctl changes | `sudo sysctl -p` |

## Gotchas
- Service Accounts require headless mode — standard interactive Client setup will not work
- If the target system OS is incompatible with the Twingate Client, a separate gateway VM is required (not optional)
- Service Keys must be managed proactively; use APIs for automated rotation
- IP forwarding must be explicitly enabled on the gateway VM — it is off by default on Ubuntu

## Related Docs
- Headless mode setup
- Service Keys documentation
- How to connect CircleCI and GitHub Actions to Private Resources
- How to connect GitHub Codespaces to Private Resources