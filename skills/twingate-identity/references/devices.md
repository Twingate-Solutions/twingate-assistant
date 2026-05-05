## Devices Overview

Top-level index for the Devices section. Three sub-topics: install the Client, deploy via MDM, administer devices in Twingate.

### What the Twingate Client Does

- Runs on user devices
- Enables access to private Resources
- Provides Internet Security features (DNS filtering, browser security)

### Three Domains Covered

**1. Install the Twingate Client**
- Where to download per platform
- Setup instructions per OS
- See /docs/clients (or platform-specific: /docs/windows, /docs/macos, /docs/linux, /docs/ios, /docs/android, /docs/chromeos)

**2. Deploying to Managed Devices**
- Client requires admin privileges (intercepts network traffic)
- Users without admin rights need MDM/EMM-pushed deployment
- See /docs/managed-devices

**3. Device Administration in Twingate**
- Posture and verification status
- Used to gate Resource access via Security Policies
- See /docs/managing-devices

### Decision Notes

- For BYOD users without local admin rights: MDM deployment is the only path
- Most production fleets use MDM regardless -- ensures version consistency, posture compliance, and remote management
- Self-managed installs work fine for evaluation and small teams

### Related Docs

- /docs/managed-devices -- MDM/EMM deployment
- /docs/managing-devices -- Devices tab + state management
- /docs/device-security-guide -- Trusted Profiles + Minimum OS Requirements
- Platform clients: /docs/windows, /docs/macos, /docs/linux, /docs/ios, /docs/android, /docs/chromeos
