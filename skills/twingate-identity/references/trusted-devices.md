# Trusted Devices

## Summary
Trusted Devices is a policy rule in Twingate that restricts access to resources or network sign-in based on whether the device is marked as trusted. Devices not marked as trusted are blocked from accessing protected resources regardless of platform or location.

## Key Information
- Can be applied to **Network Sign In Policies** and **Resource Policies**
- Enforcement is platform-agnostic (works on all platforms)
- Enforcement is location-agnostic
- Requires Twingate Client app to be installed on the device
- Untrusted devices are blocked entirely from accessing protected resources

## Prerequisites
- Twingate Client app installed on the device
- Device must be marked as "Trusted" in Twingate admin settings before policy allows access

## Configuration
- Apply as a rule condition within:
  - **Network Sign In Policies** — controls sign-in access
  - **Resource Policies** — controls per-resource access

## Step-by-Step (Policy Setup)
1. Navigate to the relevant Network Sign In Policy or Resource Policy in the Twingate admin console
2. Add a "Trusted Device" rule condition to the policy
3. Save/publish the policy
4. Ensure target devices are marked as trusted via device management settings

## Gotchas
- A user on an untrusted device will be **blocked** even if all other policy conditions are met
- Marking a device as trusted must be done separately (in device management) — policy enforcement and trust assignment are distinct steps
- No exceptions based on platform or network location — enforcement is absolute when the rule is active

## Related Docs
- Network Sign In Policies
- Resource Policies
- Device Management