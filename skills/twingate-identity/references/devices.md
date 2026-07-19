# Twingate Devices Overview

## Page Title
Devices — Twingate Documentation

## Summary
Overview page for the Twingate Client application and device management. The Client runs on user devices to enable access to private Resources and Internet Security features, requiring admin privileges due to network traffic interception. Provides navigation to three core sub-topics.

## Key Information
- Twingate Client handles both **private Resource access** and **Internet Security features**
- Client requires **administrator privileges** on end-user devices (intercepts network traffic)
- Devices are a **primary component** in zero trust access evaluation
- Device posture and status are used in evaluating Resource access attempts

## Three Core Sub-Topics

| Topic | Purpose |
|-------|---------|
| Twingate Client Application | Download locations and platform-specific setup |
| Deploying to Managed Devices | MDM/EMM deployment for users without admin rights |
| Device Administration | Device posture, status, and zero trust policy configuration |

## Prerequisites
- Administrator privileges required for Client installation on end-user devices
- MDM/EMM product needed for managed device deployments (when users lack admin access)

## Gotchas
- Users **without local admin rights** cannot self-install the Client — must use MDM/EMM deployment path
- Network traffic interception is why elevated privileges are required (not optional)

## Related Docs
- `/docs/client` — Twingate Client application details and platform setup
- `/docs/managed-devices` — MDM/EMM deployment guide
- `/docs/device-administration` — Device posture and zero trust policy administration