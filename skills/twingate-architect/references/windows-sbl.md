# Windows Start Before Logon (SBL)

## Summary
Windows SBL enables network connectivity at the Windows logon prompt before user authentication, replacing traditional VPN for domain controller access. Twingate implements this via device-only Resource Policies combined with persistent session authentication. Users must have signed into the Twingate client at least once within the session window.

## Key Information
- SBL requires **device-only Resource Policies** (no user authentication requirement at access time)
- Session persists across restarts unless user explicitly logs out
- Default session length: **30 days** (configurable via Minimum Authentication Requirements)
- Device-only policies remain accessible as long as session is valid AND device requirements are met
- Standard/Default policies always require re-authentication after restart

## Prerequisites
- Twingate Windows Client **v1.0.14 or later**
- Trusted Devices feature (recommended)
- User must have signed into Twingate client at least once within session window

## Step-by-Step Configuration

1. **Add Domain Controller addresses as Resources** — follow Active Directory with Twingate guide
2. **Create a Group** — add DC Resources and target Users to the group
3. **Create a new Resource Policy** named "Windows SBL" — via Policies tab in Admin console
4. **Configure the policy**:
   - Disable user authentication requirements
   - Enable device requirements (e.g., restrict to Windows devices only)
   - Optionally allow trusted and/or untrusted devices
5. **Apply policy to Resources** — assign the Windows SBL policy to each DC resource for the target group
6. **Verify session length** — confirm Minimum Authentication Requirements match your re-auth window (default 30 days)

## Configuration Values
| Setting | Value |
|---|---|
| Policy type | Device-only (no user auth) |
| Default session length | 30 days |
| Minimum client version | v1.0.14 |
| Device restriction | Windows only (recommended) |

## Gotchas
- Users **must actively log out** to invalidate the session — restarts alone do not
- Standard Resource Policies (including Default Policy) **always require re-auth** after machine restart, even with SBL — only device-only policies bypass this
- SBL only works if the user has previously signed in within the session window; first-time setup requires an interactive login
- Trusted Devices is recommended but not strictly required — untrusted devices can be permitted if policy allows

## Related Docs
- [Active Directory with Twingate](https://www.twingate.com/docs/active-directory)
- Trusted Devices documentation
- Minimum Authentication Requirements / Session Length configuration
- Resource Policies documentation