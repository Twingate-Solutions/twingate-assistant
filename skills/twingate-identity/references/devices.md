# Twingate Devices Overview

## Page Title
Devices – Twingate Client Installation and Device Management

## Summary
This page provides a navigation hub for installing the Twingate Client application, deploying it to managed devices via MDM/EMM, and administering device posture within Twingate's zero trust access model. The Client intercepts network traffic to enable private Resource access and Internet Security features.

## Key Information
- Twingate Client runs on end-user devices to enable access to private Resources and Internet Security features
- Client **requires administrator privileges** on end-user devices due to network traffic interception
- Managed device deployment via MDM/EMM is available for users without local admin rights
- Devices are a primary component of zero trust policy evaluation
- Device posture and status can be used in access control decisions for Resources

## Prerequisites
- Admin privileges on end-user devices for direct installation
- MDM/EMM solution required for deploying to devices where users lack admin access

## Step-by-Step
This page links to three sub-sections:
1. **Client Installation** – Download and platform-specific setup via the Twingate Client docs
2. **Managed Device Deployment** – MDM/EMM deployment guide for enterprise-managed endpoints
3. **Device Administration** – Configure device posture checks and manage devices in the Twingate Admin Console

## Configuration Values
- None defined on this page; see linked sub-sections for platform-specific configuration

## Gotchas
- Users **cannot self-install** the Client without local admin rights — MDM deployment path must be planned for locked-down endpoints
- Device posture is integral to zero trust evaluation; misconfigured or unenrolled devices may fail access checks

## Related Docs
- Twingate Client application (installation and platform setup)
- Deploying Twingate on managed devices (MDM/EMM)
- Administering devices in Twingate (posture, status, access policy)