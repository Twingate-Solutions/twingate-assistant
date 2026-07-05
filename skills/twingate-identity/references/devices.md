# Twingate Devices Overview

## Page Title
Devices — Twingate Client Installation and Device Management

## Summary
This page provides a practical overview of the Twingate Client application and device management options. It covers client installation, managed device deployment, and device administration within the Twingate zero trust framework.

## Key Information
- **Twingate Client** runs on end-user devices and enables access to private Resources and Internet Security features
- **Admin privileges required** — Client intercepts network traffic, so elevated permissions are needed on the device
- **MDM/EMM deployment** available for users without local admin access
- **Device posture** is a primary factor in zero trust access evaluation

## Three Core Areas

| Area | Purpose | Link |
|------|---------|-------|
| Client Application | Download and platform-specific setup | Twingate Client docs |
| Managed Devices | MDM/EMM deployment for non-admin users | Managed devices docs |
| Device Administration | Device posture, status, and access policies | Administering devices docs |

## Prerequisites
- Administrator privileges on the target device (for manual installation)
- MDM/EMM solution (e.g., Jamf, Intune, Kandji) for managed/enterprise deployments
- Twingate account with appropriate network configured

## Gotchas
- Users **without admin rights** cannot self-install — must use MDM/EMM deployment path
- Network traffic interception requires OS-level permissions; some platforms may trigger security prompts
- Device posture checks feed into zero trust policy decisions — misconfigured device policies can block legitimate access

## Related Docs
- Twingate Client application (platform-specific install guides)
- Deploying Twingate on managed devices (MDM/EMM)
- Administering devices in Twingate (posture and access evaluation)