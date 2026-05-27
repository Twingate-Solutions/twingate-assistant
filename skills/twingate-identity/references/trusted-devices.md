# Trusted Devices

## Summary
Trusted Devices is a policy rule in Twingate that restricts access to Resources or Network Sign In based on whether the device is marked as trusted. Users on untrusted devices are blocked from accessing protected Resources when this rule is enforced.

## Key Information
- Applies to both **Network Sign In Policies** and **Resource Policies**
- Enforcement is platform-agnostic (works on any OS/platform)
- Enforcement is location-agnostic
- Requires the Twingate Client app to be installed on the device
- Blocking is enforced at access time, not just authentication time

## Prerequisites
- Twingate Client app installed on end-user devices
- Device must be enrolled/registered in Twingate
- Admin access to configure Network Sign In Policies or Resource Policies

## Configuration
1. Navigate to the target **Resource Policy** or **Network Sign In Policy**
2. Add the **Trusted Devices** rule to the policy
3. Mark specific devices as trusted within Twingate admin console
4. Apply policy to relevant Resources or network sign-in flows

## Gotchas
- A device must be explicitly **marked as trusted** — enrollment alone does not make a device trusted
- Users will be **silently blocked** (not prompted to remediate) if accessing from an untrusted device
- Policy applies regardless of network location — being on a corporate network does not bypass the requirement
- All platforms are subject to enforcement; no platform exceptions

## Related Docs
- Network Sign In Policies
- Resource Policies
- Device Management