# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts enable machine-to-machine secure communications in Twingate using headless mode Client deployments. They authenticate via Service Keys instead of standard credentials or 2FA. Primary use cases include SaaS-to-private-resource connections, cross-site private resource connections, and gateway configurations for unsupported OS devices.

## Key Information
- Service Accounts **cannot** fulfill 2FA requirements
- Service Accounts **cannot** use standard credentials (social login, IdP accounts)
- Authentication uses **Service Keys** (expirable, API-manageable)
- Client runs in **headless mode** (non-interactive)

## Use Cases
1. **SaaS → Private Resources**: Connect GitHub Actions, CircleCI, GitHub Codespaces to private infrastructure
2. **Private → Private (cross-site)**: Deploy headless Client on source system needing remote resource access
3. **Device pool → Private Resources**: Use a gateway VM when target systems can't run the Twingate Client directly (incompatible OS)

## Prerequisites
- Twingate tenant with Service Account created
- Twingate Client installed (headless mode capable)
- For gateway setup: Ubuntu VM with IP forwarding support

## Step-by-Step: Ubuntu Gateway Setup
1. Create a Service Account in Twingate tenant
2. Install Twingate Client in headless mode configured for the Service Account
3. Enable IP forwarding: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`
4. Apply changes: `sudo sysctl -p`
5. Start Twingate Client in headless mode
6. Configure layer 3 switch/router to route tunneled resource traffic through the Ubuntu gateway VM

## Configuration Values
| Parameter | Value/Location |
|-----------|---------------|
| IP forwarding config | `/etc/sysctl.conf` |
| IP forwarding directive | `net.ipv4.ip_forward=1` (uncomment to enable) |
| Apply sysctl changes | `sudo sysctl -p` |

## Gotchas
- Gateway VM approach requires a **layer 3 switch or router** route configuration — the VM alone is insufficient
- Service Keys must be actively managed (rotation/expiry) since they are the sole authentication mechanism
- Headless mode is required; standard interactive Client mode does not apply to Service Accounts

## Related Docs
- Headless mode setup
- Service Keys management
- How to connect CircleCI and GitHub Actions to Private Resources
- How to connect GitHub Codespaces to Private Resources
- Twingate API (for automated Service Key management)