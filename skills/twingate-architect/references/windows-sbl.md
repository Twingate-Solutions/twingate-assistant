# Windows Start Before Logon (SBL)

## Summary
Windows SBL enables network access at the Windows logon prompt before user authentication, replacing traditional VPN for domain controller access. Twingate implements this using Device-only Resource Policies combined with persistent session authentication. Users must have signed into the Twingate client at least once within the session validity period.

## Key Information
- SBL works by using device-only policies (no per-session user auth required)
- Session persists across restarts unless user explicitly logs out
- Default session length: 30 days
- Device-only policies bypass user auth requirement; standard/default policies do not
- Recommended for Active Directory domain controller access scenarios

## Prerequisites
- Twingate Windows Client **v1.0.14 or later**
- Device-only Resource Policy configured
- (Recommended) Trusted Devices feature enabled
- User must have authenticated at least once within session window (default 30 days)

## Step-by-Step Configuration

1. **Add Domain Controller as Resource** — Follow Active Directory with Twingate guide
2. **Create a Group** — Add DC resources and target users to the group
3. **Create Resource Policy** named "Windows SBL" — Via Admin Console → Policies tab → "Create Resource Policy"
4. **Configure Policy** — Disable user authentication requirement; enable device requirements (restrict to Windows devices; allow trusted and/or untrusted as needed)
5. **Apply Policy to Resources** — Modify each DC resource to use the new SBL policy scoped to the group
6. **Verify session length** — Check Minimum Authentication Requirements match your needs (default: 30 days)

## Configuration Values

| Setting | Value |
|---|---|
| Client minimum version | v1.0.14 |
| Default session length | 30 days |
| User auth on Device-only Policy | Disabled |
| User auth on Standard/Default Policy | Required (re-validates on restart) |

## Behavior by Policy Type

| Policy Type | Requires user re-auth on restart? | SBL compatible? |
|---|---|---|
| Device-only (SBL policy) | No | Yes |
| Standard / Default | Yes | No |

## Gotchas
- Users **must not log out** of the Twingate client — logout invalidates the session and breaks SBL until they re-authenticate
- Standard/Default policies always re-require user auth after restart; only device-only policies support SBL
- Session persists across reboots automatically if user stays signed in
- SBL access fails if session has expired (>30 days since last login) even if device is trusted

## Related Docs
- [Active Directory with Twingate](https://www.twingate.com/docs/active-directory)
- Device-only Resource Policies documentation
- Trusted Devices documentation
- Minimum Authentication Requirements configuration