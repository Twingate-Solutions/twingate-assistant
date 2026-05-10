# Trusted Devices

## Summary
Trusted Devices is a policy rule in Twingate that restricts access to resources or network sign-in based on whether a device is marked as trusted. It can be applied at both the network sign-in and resource access levels, blocking untrusted devices regardless of platform or location.

## Key Information
- Enforces device trust status as an access condition
- Works across all platforms and locations where the Twingate Client app runs
- Blocking is enforced at access time — untrusted devices are denied, not just warned
- Two enforcement scopes: sign-in level and per-resource level

## Prerequisites
- Twingate Client app installed on the device being evaluated
- Device must be enrolled/visible in Twingate for trust status to be assigned
- Admin access to configure Network Sign In Policies or Resource Policies

## Applicability
| Policy Type | Supported |
|---|---|
| Network Sign In Policies | ✅ |
| Resource Policies | ✅ |

## Step-by-Step (Policy Configuration)
1. Navigate to the relevant **Network Sign In Policy** or **Resource Policy** in the Twingate Admin Console
2. Add a **Trusted Devices** rule to the policy
3. Save and apply the policy to the target resource or network
4. Mark devices as trusted via the Devices section in the Admin Console
5. Test access from a trusted vs. untrusted device to verify enforcement

## Configuration Values
- No CLI flags or environment variables specific to this rule
- Trust status is set per-device in the Admin Console (not via client-side configuration)

## Gotchas
- A device must have the Twingate Client app installed to be evaluated — devices without the client cannot be assessed for trust status
- If a resource policy requires trusted devices, the user is **blocked entirely** from that resource on an untrusted device — there is no fallback or degraded access mode
- Trust status is admin-assigned; users cannot self-designate their device as trusted
- Applies regardless of network location (on-prem or remote), so trusted device requirements apply even to users on corporate networks

## Related Docs
- Network Sign In Policies
- Resource Policies
- Device Management