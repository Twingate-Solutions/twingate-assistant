# Twingate Devices Overview

## Page Title
Devices - Twingate Client Installation and Device Management

## Summary
This page provides a high-level overview of the Twingate Client application and device management options. The Client runs on user devices to enable private Resource access and Internet Security features, requiring admin privileges to intercept network traffic.

## Key Information
- Twingate Client enables two core functions: access to private Resources and Internet Security features
- Client **requires administrator privileges** on end-user devices (intercepts network traffic)
- Supports MDM/EMM deployment for managed devices where users lack admin access
- Devices are a primary component in zero trust access evaluation
- Device posture and status can be used in Resource access decisions

## Three Main Topic Areas

| Topic | Purpose |
|-------|---------|
| Twingate Client Application | Download locations and platform-specific setup |
| Managed Device Deployment | MDM/EMM deployment for non-admin users |
| Device Administration | Device posture, status, zero trust assessment config |

## Prerequisites
- Administrator privileges on device for standard Client installation
- MDM/EMM product required if deploying to devices where users lack admin rights

## Related Docs
- Twingate Client application (platform-specific installation guides)
- Deploying Twingate on managed devices (MDM/EMM deployment)
- Administering devices in Twingate (posture checks, access policies)

## Gotchas
- Users **cannot self-install** the Client without local admin rights — requires MDM deployment path
- Device posture integration is available but requires separate configuration under device administration