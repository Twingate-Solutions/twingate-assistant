# Windows Start Before Logon (SBL)

## Summary
Windows SBL allows devices to connect to remote networks at the Windows logon prompt before user authentication. Twingate implements this using Device-only Resource Policies combined with session persistence, enabling domain controller access at the login screen.

## Key Information
- Requires Twingate Windows Client v1.0.14 or later
- Uses Device-only Resource Policies (no user auth requirement at access time)
- Session persists across restarts unless user explicitly logs out
- Default session length: 30 days (configurable via Minimum Authentication Requirements)
- Recommended to use with Trusted Devices for security

## Prerequisites
- Twingate Windows Client v1.0.14+
- Admin access to Twingate Admin Console
- Domain Controller addresses defined as Resources
- Users must have authenticated to Twingate Client at least once within session window

## Step-by-Step Configuration

1. **Add Domain Controller as Resource** — Follow Active Directory with Twingate guide
2. **Create Group** — Add DC Resources and target Users to the group
3. **Create Resource Policy** named "Windows SBL" — Via Policies tab in Admin Console
4. **Configure Policy settings:**
   - Disable user authentication requirements
   - Enable device requirements (restrict to Windows devices)
   - Optionally allow both trusted and untrusted devices
5. **Apply Policy to Resources** — Modify each Resource's policy to use the Windows SBL policy for the relevant Group
6. **Verify session length** — Confirm Minimum Authentication Requirements match your needs (default: 30 days)

## Configuration Values

| Setting | Value |
|---|---|
| Min client version | v1.0.14 |
| Default session length | 30 days |
| User auth on Device-only policy | Disabled |
| Device requirement | Windows (configurable) |

## How Authentication Works at Logon Screen

- **Device-only policies**: Accessible as long as Minimum Auth Requirements session is valid + device requirements met (no per-access user auth)
- **Standard/Default policies**: Require user auth re-validation after every restart or client relaunch — **not usable for SBL**

## Access Requirements at Login Screen
- Client v1.0.14+
- User signed in within last 30 days and **not logged out**
- Device marked as trusted in Twingate

## Gotchas
- User must not have explicitly logged out — logout invalidates the session even within the 30-day window
- Standard Resource Policies (including Default Policy) require re-auth after restarts — they **cannot** be used for SBL access
- Session length applies globally via Minimum Authentication Requirements, not per-policy
- Untrusted devices can be permitted but Trusted Devices are recommended for security

## Related Docs
- Active Directory with Twingate
- Device-only Resource Policies
- Trusted Devices