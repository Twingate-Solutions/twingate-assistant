# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts enable machine-to-machine secure communications in Twingate without human interaction. They use Service Keys for authentication and run the Twingate Client in headless mode. Unlike user accounts, they cannot use 2FA or standard credentials (SSO/IdP).

## Key Information
- **Cannot** fulfill 2FA requirements
- **Cannot** use standard credentials (social login, IdP)
- Authenticate via **Service Keys** (expirable, API-manageable)
- Run Twingate Client in **headless mode** (non-interactive)

## Use Cases
1. **SaaS → Private Resources**: Connect SaaS apps (GitHub Actions, CircleCI, GitHub Codespaces) to private infrastructure (K8s, VMs)
2. **Private → Private (cross-site)**: Connect systems in different private sites; deploy Client in headless mode on the initiating system
3. **Pool of devices → Private Resources (gateway mode)**: When headless Client can't run on the source system (incompatible OS), use a VM as a proxy gateway

## Prerequisites
- Twingate tenant with Service Account creation permissions
- Compatible OS for headless Client (or Ubuntu VM for gateway setup)

## Step-by-Step: Ubuntu Gateway Setup

1. Create a Service Account in your Twingate tenant
2. Install Twingate Client in headless mode configured with the Service Account
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
| Setting | Value/Location |
|---|---|
| IP forwarding config | `/etc/sysctl.conf` |
| IP forwarding directive | `net.ipv4.ip_forward=1` |
| Apply command | `sudo sysctl -p` |

## Gotchas
- Gateway VM approach requires layer 3 switch/router configuration — Twingate alone doesn't handle the routing
- Service Keys must be managed/rotated; use the API for automation at scale
- Headless mode must be configured to reference the Service Account credentials, not a user account

## Related Docs
- Headless mode setup
- Service Keys management
- How to connect CircleCI and GitHub Actions to Private Resources
- How to connect GitHub Codespaces to Private Resources