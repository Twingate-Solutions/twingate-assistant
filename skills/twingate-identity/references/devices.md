---
source: https://www.twingate.com/docs/devices
type: docs
fetched: 2026-11-22
source_version: 4998abad33e5d2ea015bdea0380af7e7cfc8300863050994991f28e32e9cddfb
trust: official
---

# Devices

**Source:** https://www.twingate.com/docs/devices

## Summary
This page is an overview and index for installing the Twingate Client and managing devices. It points to separate pages for Client installation, deployment to managed devices via MDM/EMM, the Twingate CLI, and device administration within Twingate.

## Key Information
- The Twingate Client runs on user devices. It provides access to private Resources and Internet Security features.
- The Client requires administrator privileges on end-user devices because it intercepts network traffic on the device.
- For users without admin access, the Client can be deployed to managed devices through MDM/EMM products.
- The macOS, Windows, and Linux Clients include the `twingate` command-line interface (CLI). It can:
  - connect
  - check status
  - list Resources
  - manage accounts
  - change Client settings
  - run from a terminal or script
- Devices are a primary component of zero trust assessment. Twingate supports using device posture and status when evaluating access attempts to Resources.

## Prerequisites
- Administrator privileges on the device for a manual Client install.
- An MDM/EMM product for managed deployments where users lack admin rights.

## Step-by-Step
The page contains no procedures. It only links to the detailed pages below.

## Configuration Values
None on this page. CLI flags and settings are documented on the CLI page.

## Gotchas
- Users without admin rights cannot install the Client themselves. Plan MDM/EMM deployment for them.
- The CLI is bundled with the Client on macOS, Windows, and Linux only. The page does not mention it for other platforms.

## Related Docs
- Using the Twingate Client application (https://www.twingate.com/docs/clients): download locations and platform-specific setup
- Deploying Twingate on managed devices (https://www.twingate.com/docs/managed-devices): MDM/EMM deployment
- Using the Twingate CLI (https://www.twingate.com/docs/twingate-cli): `twingate` command reference
- Administering devices in Twingate (https://www.twingate.com/docs/managing-devices): device posture and status for access policy