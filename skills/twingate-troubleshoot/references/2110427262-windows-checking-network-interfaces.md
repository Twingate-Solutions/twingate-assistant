---
source: https://help.twingate.com/articles/2110427262-windows-checking-network-interfaces
type: help
fetched: 2026-09-06
source_version: fbc82515b40f5f07808ef882ef9d07ef8417b9e765a90dfdd4c3f6c257e5992e
---

# [Windows] Checking Network Interfaces

## Summary
The Twingate Client installs its own network adapter on Windows devices during installation. If this adapter is disabled, the client will not function. This guide covers how to verify the adapter is enabled.

## Key Information
- Twingate creates a dedicated network adapter named **"Twingate"** on the host device
- The adapter is configured automatically during client installation
- A disabled adapter will prevent the Twingate Client from functioning

## Prerequisites
- Twingate Client installed on Windows
- Access to Windows Network Connections settings

## Step-by-Step

1. Open **Network and Sharing Center** (Control Panel → Network and Internet → Network and Sharing Center)
2. Click **Change adapter settings** (left sidebar) to open **Network Connections**
3. Locate the adapter named **"Twingate"**
4. Verify the adapter is **not disabled** (disabled adapters appear grayed out)
5. If disabled, right-click the adapter → select **Enable**

## Gotchas
- The adapter can be accidentally disabled by users or system policies
- If the adapter is missing entirely (not just disabled), reinstalling the Twingate Client may be required
- Group Policy or endpoint management tools may disable non-standard adapters automatically

## Related Docs
- Twingate Windows Troubleshooting Guide