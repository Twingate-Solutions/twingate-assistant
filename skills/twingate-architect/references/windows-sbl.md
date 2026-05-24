# Windows Start Before Logon (SBL)

## Summary
Windows SBL enables Twingate to connect to remote networks at the Windows logon prompt before user authentication, replacing traditional VPN-based domain controller access. It combines Device-only Resource Policies with the Windows Twingate Client to allow pre-login network access while maintaining security controls.

## Key Information
- Requires Twingate Windows Client v1.0.14 or later
- Uses Device-only Resource Policies (no user auth required at logon screen)
- Session persists across restarts unless user explicitly logs out
- Default session length: 30 days (configurable via Minimum Authentication Requirements)
- Recommended use case: Active Directory Domain Controller access at logon prompt

## Prerequisites
- Twingate Windows Client v1.0.14+
- Trusted Devices feature (recommended)
- Admin access to Twingate Admin Console
- Domain Controller addresses added as Twingate Resources

## Step-by-Step Configuration

1. **Add Domain Controller as Resource** — Follow Active Directory with Twingate guide
2. **Create Group** — Add DC Resources and target Users to the group
3. **Create Resource Policy** — Name it "Windows SBL" via Admin Console → Policies tab → "Create Resource Policy"
4. **Configure Policy** — Disable user authentication requirements; enable device requirements (can restrict to Windows-only; allow trusted and/or untrusted devices)
5. **Assign Policy to Resources** — Modify each DC Resource to use the Windows SBL policy for the specific Group
6. **Verify Session Length** — Check Minimum Authentication Requirements matches your requirements (default: 30 days)

## Configuration Values

| Setting | Value |
|---|---|
| Min Client Version | v1.0.14 |
| Default session length | 30 days |
| User auth on Device-only Policy | Disabled |
| Device auth on Device-only Policy | Required |

## Runtime Behavior

- **Device-only policies**: Accessible as long as Minimum Auth session is valid + device requirements met
- **Standard/Default policies**: Require user re-authentication after every restart or Client relaunch
- SBL resources remain accessible across reboots without re-login (within session window)

## Access Requirements at Logon Screen
All three must be true:
1. Windows Client v1.0.14+
2. User signed into Twingate Client within last 30 days and **not** logged out
3. Device marked as trusted in Twingate

## Gotchas
- User must have signed in at least once and must **not** have manually logged out — logout invalidates SBL access
- Device-only policies bypass per-resource user auth but still require a valid Minimum Auth session
- Standard/Default policies will NOT work for SBL (require user auth on each restart)
- Trusted Devices is recommended but untrusted devices can be permitted if configured explicitly

## Related Docs
- Active Directory with Twingate
- Device-only Resource Policies
- Trusted Devices
- Minimum Authentication Requirements