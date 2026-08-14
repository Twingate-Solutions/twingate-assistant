---
source: https://www.twingate.com/docs/devices
type: docs
fetched: 2026-08-14
source_version: 96b5c2e0bf508bc4f34ffc4b4919758ca0460f0ae3f98b0e113a9e909265b63f
---

# Twingate Devices Overview

## Page Title
Devices — Practical Overview

## Summary
This page serves as a navigation hub for Twingate device-related documentation. It covers three main areas: installing the Twingate Client, deploying to managed devices via MDM/EMM, and administering device posture for zero trust access control.

## Key Information
- **Twingate Client**: Runs on end-user devices; enables access to private Resources and Internet Security features
- **Admin privileges required**: Client intercepts network traffic, so it requires administrator privileges on the device
- **MDM/EMM support**: For users without local admin rights, Client can be deployed via managed device management platforms
- **Device posture**: Devices are a primary factor in zero trust access evaluation; Twingate provides posture checks and status monitoring

## Three Core Topic Areas

| Topic | Purpose |
|---|---|
| Twingate Client Application | Download locations and platform-specific setup |
| Deploying to Managed Devices | MDM/EMM deployment for non-admin users |
| Device Administration | Posture checks, device status, access policy integration |

## Prerequisites
- Administrator privileges on the device (for manual Client install)
- MDM/EMM platform (for managed deployments without user admin rights)

## Gotchas
- Users **without** local admin access cannot self-install; must use MDM/EMM deployment path
- Device posture is actively used in access decisions — misconfigured posture policies can block legitimate access

## Related Docs
- Twingate Client application (platform-specific install guides)
- Managed device deployment (MDM/EMM setup)
- Administering devices in Twingate (posture, status, policy configuration)