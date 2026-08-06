---
source: https://help.twingate.com/articles/2110427262-windows-checking-network-interfaces
type: help
fetched: 2026-08-06
source_version: a4f0d48fd187b09ffd647c06919ad4eee363f424787211c835dfe64c7214c212
---

# [Windows] Checking Network Interfaces

## Summary
The Twingate Client installs its own network adapter on Windows devices during installation. If this adapter is disabled, the client will not function. This guide covers verifying the adapter is enabled.

## Key Information
- Twingate creates a dedicated network adapter named **"Twingate"** on the host device
- Adapter is created automatically during client installation
- A disabled adapter will prevent the Twingate Client from functioning

## Prerequisites
- Twingate Client installed on Windows device
- Access to Windows network settings

## Step-by-Step

1. Open **Network and Sharing Center** (Control Panel → Network and Internet → Network and Sharing Center)
2. Click **Change adapter settings** (left sidebar) to open **Network Connections**
3. Locate the adapter named **"Twingate"**
4. Verify the adapter is **not disabled** (disabled adapters appear grayed out)
5. If disabled, right-click the adapter → select **Enable**

## Gotchas
- The adapter can be accidentally disabled by users or system policies
- Disabled state is visually distinct (grayed out icon) in Network Connections view
- If the adapter is missing entirely (not just disabled), reinstalling the Twingate Client may be required

## Related Docs
- Twingate Windows Troubleshooting Guide