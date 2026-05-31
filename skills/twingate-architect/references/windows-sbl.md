# Windows Start Before Logon (SBL)

## Summary
Windows SBL allows devices to connect to remote networks at the Windows logon prompt before user authentication. Twingate implements this via Device-only Resource Policies combined with session persistence in the Windows Client.

## Key Information
- SBL enables access to domain controllers at Windows logon screen (before user login)
- Uses device-only authentication (no per-session user auth required)
- Session persists across restarts unless user explicitly logs out
- Default session length: 30 days
- Recommended for Active Directory domain controller access

## Prerequisites
- Twingate Windows Client **v1.0.14 or later**
- Device-only Resource Policy configured
- (Recommended) Trusted Devices feature enabled
- Users must have signed into Twingate Client at least once within session window

## Step-by-Step Configuration

1. **Add Domain Controller as Resource** — Follow Active Directory with Twingate guide
2. **Create a Group** — Add DC Resources and target Users to the group
3. **Create Resource Policy** — Name it "Windows SBL" via Admin console → Policies tab → "Create Resource Policy"
4. **Configure Policy settings**:
   - Disable user authentication requirements
   - Enable device requirements
   - Restrict to Windows devices (trusted and/or untrusted per your requirements)
5. **Assign Policy to Resources** — Apply the SBL policy to each DC resource for the target group
6. **Verify session length** — Check Minimum Authentication Requirements; default is 30 days

## Configuration Values

| Setting | Value |
|---|---|
| Min client version | v1.0.14+ |
| Default session length | 30 days |
| Auth type for SBL policy | Device-only (no user auth) |
| Platform restriction | Windows only |

## Gotchas
- **Device-only policies** skip user auth but still require valid Minimum Authentication Requirements session — user must have logged in within 30 days
- **Standard/Default policies** require user auth re-validation on every restart or Client relaunch — these will NOT work for SBL
- Session is invalidated if user explicitly logs out of Twingate Client (not just machine restart)
- Trusted device requirement is recommended but optional — untrusted devices can be permitted if needed

## Access Requirements at Logon Screen
All three must be true:
1. Windows Client v1.0.14+
2. Signed into Twingate within last 30 days, not logged out
3. Device marked as trusted (if trusted device requirement enabled)

## Related Docs
- [Active Directory with Twingate](https://www.twingate.com/docs/active-directory)
- Device-only Resource Policies
- Trusted Devices
- Minimum Authentication Requirements