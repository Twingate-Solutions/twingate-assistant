# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts enable machine-to-machine communication in Twingate by running the Twingate Client in headless (non-interactive) mode. They use Service Keys instead of standard credentials and cannot fulfill 2FA requirements. Primary use cases include SaaS-to-private-resource connections, cross-site private resource connectivity, and gateway setups for unsupported operating systems.

## Key Information
- Service Accounts **cannot** use 2FA or standard credentials (social login, IdP accounts)
- Authentication uses **Service Keys** — support expiration and API-based management
- Client runs in **headless mode** (non-interactive)
- Three main use cases:
  1. SaaS apps (CircleCI, GitHub Actions, Codespaces) → private resources
  2. Private resource → private resource across different sites
  3. Pool of devices via a gateway VM (for incompatible OSes)

## Prerequisites
- Twingate tenant with Service Account creation permissions
- Twingate Client compatible with target system
- For gateway setup: Ubuntu VM with network access

## Step-by-Step: Ubuntu Gateway Setup

1. Create a Service Account in your Twingate tenant
2. Install Twingate Client in headless mode configured with the Service Account
3. Enable IP forwarding:
   ```
   # Uncomment in /etc/sysctl.conf:
   net.ipv4.ip_forward=1
   ```
4. Apply changes:
   ```bash
   sudo sysctl -p
   ```
5. Start the Twingate Client in headless mode
6. Configure layer 3 switch/router to route tunneled resource traffic through the Ubuntu gateway VM

## Configuration Values
| Item | Value/Location |
|------|---------------|
| IP forwarding config | `/etc/sysctl.conf` |
| IP forwarding directive | `net.ipv4.ip_forward=1` |
| Apply config command | `sudo sysctl -p` |

## Gotchas
- Systems running incompatible OSes **cannot** run the Client directly — requires a separate gateway VM
- Gateway VM requires IP forwarding enabled **and** a corresponding route on a layer 3 switch/router; both are necessary
- Service Keys should be rotated regularly; automate via API for production use

## Related Docs
- Headless mode setup
- Service Keys management
- Connect CircleCI and GitHub Actions to Private Resources
- Connect GitHub Codespaces to Private Resources