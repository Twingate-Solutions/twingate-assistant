# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts secure machine-to-machine communications in Twingate, replacing human credentials with Service Keys and headless Client mode. They cannot use 2FA or standard identity provider credentials. Common use cases include SaaS-to-private-resource connections, cross-site private connections, and gateway setups for unsupported OS devices.

## Key Information
- Service Accounts use **headless mode** for non-interactive Twingate Client operation
- Authentication via **Service Keys** (expirable, API-manageable) instead of social login/IdP credentials
- Three primary use cases:
  1. SaaS apps (CircleCI, GitHub Actions, Codespaces) → private Resources
  2. Private-to-private Resource connections across different sites
  3. Gateway VM for devices with unsupported operating systems

## Prerequisites
- Twingate tenant with Service Account creation permissions
- Twingate Client installed on target machine
- For gateway use case: Ubuntu (or compatible) VM with network routing access

## Step-by-Step: Ubuntu Gateway Setup

1. Create a Service Account in your Twingate tenant
2. Install Twingate Client in headless mode configured with the Service Account
3. Enable IP forwarding: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`
4. Apply changes: `sudo sysctl -p`
5. Start Twingate Client in headless mode
6. Configure a route on layer 3 switch/router to direct tunneled resource traffic through the Ubuntu gateway

## Configuration Values
| Setting | Location | Value |
|---|---|---|
| IP forwarding | `/etc/sysctl.conf` | `net.ipv4.ip_forward=1` |
| Apply sysctl | CLI | `sudo sysctl -p` |

## Gotchas
- Service Accounts **cannot fulfill 2FA** — do not assign them to Resources requiring MFA
- Service Accounts **cannot use standard credentials** (no OAuth, no IdP login)
- If deploying a gateway VM, IP forwarding must be enabled or traffic will not forward to tunneled Resources
- Unsupported OS devices require a separate gateway VM — Twingate Client cannot run directly on them

## Related Docs
- Headless Mode setup
- How to connect CircleCI and GitHub Actions to Private Resources
- How to connect GitHub Codespaces to Private Resources
- Service Keys management
- Twingate API (for automated Service Key rotation)