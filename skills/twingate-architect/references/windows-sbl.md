# Windows Start Before Logon (SBL)

## Summary
Windows SBL allows devices to connect to remote networks at the Windows logon prompt before user authentication. Twingate implements this via Device-only Resource Policies combined with session persistence in the Windows Client.

## Key Information
- SBL enables access to resources (e.g., domain controllers) before Windows user login
- Uses device authentication instead of user authentication for pre-login access
- Session persists across restarts unless user explicitly logs out
- Default session length: 30 days before re-authentication required

## Prerequisites
- Twingate Windows Client **v1.0.14 or later**
- Device-only Resource Policies configured
- (Recommended) Trusted Devices feature enabled
- (Recommended) Review Active Directory with Twingate docs if using AD/DC

## Step-by-Step Configuration

1. **Add Domain Controller addresses as Resources** — Follow Active Directory with Twingate guide
2. **Create a Group** — Add DC Resources and target Users to the group
3. **Create Resource Policy named "Windows SBL"** — Via Policies tab in Admin console
4. **Configure the policy** — Disable user authentication requirements; enable device requirements (restrict to Windows devices; allow trusted and/or untrusted devices as needed)
5. **Assign policy to Resources** — Modify each Resource's policy to use "Windows SBL" scoped to the Group
6. **Verify Minimum Authentication Requirements** — Confirm session length matches your requirements (default: 30 days)

## Configuration Values

| Setting | Value |
|---|---|
| User authentication | Disabled |
| Device requirements | Enabled (Windows only) |
| Session length (default) | 30 days |
| Min client version | v1.0.14 |

## Authentication Behavior

- **Device-only policies**: Accessible at logon screen as long as Minimum Authentication session is valid + device requirements met
- **Standard policies (incl. Default Policy)**: Require user authentication re-validation after every restart or Client relaunch — **not accessible at logon screen**

## Gotchas
- Users must sign into Twingate Client **at least once** before SBL works — session must be established
- Explicit logout breaks SBL; user must sign in again to restore pre-login access
- Session survives machine restarts only if user has **not** logged out of the Client
- Trusted Devices is recommended but untrusted devices can also be permitted depending on policy configuration

## Related Docs
- Active Directory with Twingate (use case guide)
- Trusted Devices
- Minimum Authentication Requirements
- Device-only Resource Policies