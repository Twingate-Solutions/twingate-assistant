---
source: https://help.twingate.com/articles/9784439823-windows-checking-the-client-service
type: help
fetched: 2026-11-08
source_version: 63c71a99bb5c70cf13073c5b75d23a5f3f07eb790707ab427569754795e762e2
trust: official
---

# [Windows] Checking the Client Service

## Summary
The Twingate Windows Client depends on a local Windows service ("Twingate Service") to function, including supporting Start Before Logon. If the service is not running, the client will not work. This guide covers how to verify and start the service.

## Key Information
- The Twingate Client on Windows runs as a background Windows service
- Service enables **Start Before Logon** functionality
- Service must be in **Running** status for the client to operate

## Prerequisites
- Twingate Client installed on Windows
- Access to run `services.msc` (may require admin privileges to start services)

## Step-by-Step

1. Open a CMD window and run:
   ```
   services.msc
   ```
2. Scroll the services list to find **Twingate Service**
3. Check the **Status** column:
   - If **Running** → service is healthy, look elsewhere for issues
   - If not running → right-click and select **Start**
4. If **Twingate Service** is not listed at all → reinstall the Twingate Client

## Troubleshooting / Gotchas
- **Service missing entirely**: Indicates a broken installation; reinstall the client
- **Cannot start the service**: Check two additional sources for root cause:
  - **Event Viewer** (Windows built-in) for system-level errors
  - **Twingate Client logs** for application-level errors
- Starting a service may require local administrator rights

## Configuration Values
| Item | Value |
|------|-------|
| Service name | `Twingate Service` |
| Management command | `services.msc` |

## Related Docs
- Twingate Client logs (referenced in troubleshooting path)
- Start Before Logon feature documentation
- Twingate Windows Client reinstall guide
- Main Windows troubleshooting guide