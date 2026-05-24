# Service Accounts Guide

## Page Title
How Service Accounts Work

## Summary
Service Accounts enable machine-to-machine secure communications in Twingate using headless Client mode instead of interactive credentials. They are secured via Service Keys (with configurable expiration) rather than standard auth methods like SSO or 2FA.

## Key Information
- Service Accounts **cannot** fulfill 2FA requirements
- Service Accounts **cannot** use standard credentials (social login, IdP accounts)
- Authentication uses **Service Keys** — can be time-limited and managed via API
- Twingate Client runs in **headless mode** (non-interactive) for Service Accounts

## Use Cases
1. **SaaS → Private Resources**: Connect GitHub Actions, CircleCI, Codespaces to private infrastructure
2. **Private → Private (cross-site)**: Secure connections between systems at different sites using headless Client
3. **Device pool → Private Resources**: When Client can't run directly on a device, use a gateway VM

## Gateway VM Setup (Ubuntu)

### Prerequisites
- Twingate tenant with admin access
- Ubuntu VM accessible on the network
- Layer 3 switch/router to configure routing

### Steps
1. Create a Service Account in your Twingate tenant
2. Install Twingate Client in headless mode configured for the Service Account
3. Enable IP forwarding: uncomment `net.ipv4.ip_forward=1` in `/etc/sysctl.conf`
4. Apply changes: `sudo sysctl -p`
5. Start Twingate Client in headless mode
6. Configure route on L3 switch/router to forward tunneled resource traffic through the Ubuntu gateway

## Configuration Values
| Setting | Value/Location |
|---|---|
| IP forwarding config | `/etc/sysctl.conf` |
| IP forwarding directive | `net.ipv4.ip_forward=1` (uncomment to enable) |
| Apply sysctl changes | `sudo sysctl -p` |

## Gotchas
- Gateway VM approach is a workaround for **incompatible OS** scenarios — deploy Client directly on the source system when possible
- Service Keys must be actively managed (rotation/expiration) — API automation recommended for security
- IP forwarding + routing setup requires network-level configuration outside of Twingate

## Related Docs
- Headless mode setup
- Service Keys management
- Connecting CircleCI and GitHub Actions to Private Resources
- Connecting GitHub Codespaces to Private Resources