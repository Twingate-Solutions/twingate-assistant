# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts enable machine-to-machine secure communications in Twingate, using the Client in headless (non-interactive) mode instead of standard credentials. They are authenticated via Service Keys rather than social logins or identity providers. Common use cases include SaaS-to-private-resource connections, cross-site private resource communication, and gateway setups for unsupported OS devices.

## Key Information
- Service Accounts **cannot** fulfill 2FA requirements
- Service Accounts **cannot** use standard credentials (social login, IdP accounts)
- Authentication is via **Service Keys** (can be set to expire, manageable via API)
- Client runs in **headless mode** (non-interactive)

## Use Cases
1. **SaaS → Private Resources**: Connect tools like GitHub Actions, CircleCI, GitHub Codespaces to private infrastructure
2. **Private ↔ Private (cross-site)**: Deploy headless Client on the system needing remote resource access
3. **Unsupported OS gateway**: When headless Client can't run directly on a device, use a VM as a proxy gateway

## Prerequisites
- Twingate tenant with admin access
- Service Account created in tenant
- Twingate Client installed in headless mode
- For gateway setup: Ubuntu VM with network access

## Step-by-Step: Ubuntu Gateway Setup
1. Create a Service Account in your Twingate tenant
2. Install Twingate Client in headless mode configured with the Service Account
3. Enable IP forwarding: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`
4. Apply changes: `sudo sysctl -p`
5. Start Twingate Client in headless mode
6. Configure a route on L3 switch/router to direct tunneled resource traffic through the Ubuntu gateway

## Configuration Values
| Setting | Value/Location |
|---|---|
| IP forwarding config | `/etc/sysctl.conf` |
| IP forwarding directive | `net.ipv4.ip_forward=1` (uncomment) |
| Apply config command | `sudo sysctl -p` |

## Gotchas
- Devices running incompatible operating systems cannot run the headless Client directly — requires the VM gateway pattern
- Gateway VM requires both IP forwarding **and** a properly configured L3 route; missing either breaks connectivity
- Service Keys should be rotated regularly; automate via API for security

## Related Docs
- Headless mode setup
- Service Keys documentation
- How to connect CircleCI and GitHub Actions to Private Resources
- How to connect GitHub Codespaces to Private Resources