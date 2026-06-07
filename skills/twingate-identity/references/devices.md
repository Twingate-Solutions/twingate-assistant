# Twingate Devices Overview

## Page Title
Devices — Twingate Client Installation and Device Management

## Summary
The Twingate Client runs on user devices to enable access to private Resources and Internet Security features. Devices are a core component of zero trust policy evaluation, with device posture and status used in access decisions.

## Key Information
- Client application intercepts network traffic and **requires administrator privileges** on end-user devices
- Supports MDM/EMM deployment for managed devices where users lack admin rights
- Device posture and status are evaluated as part of zero trust access control for Resources

## Prerequisites
- Administrator privileges on the device for standard installation
- MDM/EMM product required for managed/non-admin deployments

## Three Core Areas

| Area | Description | Reference |
|------|-------------|-----------|
| Client Application | Download and platform-specific setup | Twingate Client docs |
| Managed Devices | MDM/EMM deployment for non-admin users | Managed devices docs |
| Device Administration | Posture checks, status, access policy integration | Administering devices docs |

## Gotchas
- Users **without local admin rights** cannot self-install the Client — must use MDM/EMM deployment path
- Network traffic interception is why elevated privileges are required; this is by design, not optional
- Device posture is actively used in access evaluation — misconfigured posture policies can block legitimate access

## Related Docs
- Twingate Client application (platform-specific install guides)
- Deploying Twingate on managed devices (MDM/EMM)
- Administering devices in Twingate (posture, zero trust policy)