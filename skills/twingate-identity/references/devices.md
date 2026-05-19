# Twingate Devices Overview

## Page Title
Devices - Twingate Client Installation and Device Management

## Summary
This page provides a practical overview of the Twingate Client application, which runs on user devices to enable access to private Resources and Internet Security features. It covers three main areas: client installation, managed device deployment, and device administration for zero trust assessment.

## Key Information
- Twingate Client enables two core functions: access to private Resources and Internet Security features
- Client requires **administrator privileges** on end user devices due to network traffic interception
- Devices are a primary component in zero trust access evaluation
- Device posture and status can be used to evaluate access attempts to Resources

## Prerequisites
- Administrator privileges required on end user devices for standard installation
- For users without admin access: MDM/EMM product required for managed deployment

## Three Main Areas

### 1. Twingate Client Application
- Runs directly on user devices
- Handles private Resource access and Internet Security
- Platform-specific setup instructions available in linked client docs

### 2. Managed Device Deployment
- Use when end users lack administrative access on their devices
- Deployed via MDM/EMM products
- Bypasses need for individual users to have admin rights

### 3. Device Administration
- Configure device posture checks
- Use device status in zero trust access policy evaluation
- Rich options for integrating device health into access decisions

## Gotchas
- Client **cannot** be installed by standard (non-admin) users — requires elevation or MDM deployment
- Network traffic interception is why admin privileges are mandatory
- Device posture must be actively configured to participate in zero trust evaluation (not automatic)

## Related Docs
- Twingate Client application (installation and platform-specific setup)
- Deploying Twingate on managed devices (MDM/EMM deployment guide)
- Administering devices in Twingate (posture checks and device management)