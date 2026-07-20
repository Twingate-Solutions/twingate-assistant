# Windows Start Before Logon (SBL)

## Summary
Windows SBL enables network access at the Windows logon prompt before user authentication, replacing traditional VPN for domain controller access. Twingate implements this using device-only Resource Policies combined with session persistence in the Windows Client.

## Key Information
- Requires Twingate Windows Client v1.0.14+
- Uses device-only Resource Policies (no user auth requirement at resource access time)
- Session persists across reboots/restarts unless user explicitly logs out
- Default session length: 30 days (configurable via Minimum Authentication Requirements)
- Primary use case: Active Directory domain controller access at logon screen

## Prerequisites
- Twingate Windows Client v1.0.14 or later
- Trusted Devices feature (recommended)
- Domain Controller added as a Twingate Resource
- Admin access to Twingate Admin console

## Step-by-Step Configuration

1. **Add Domain Controller as Resource** — Follow Active Directory with Twingate guide
2. **Create a Group** — Add DC Resources and target Users to the group
3. **Create Resource Policy "Windows SBL"** — Admin console → Policies tab → Create Resource Policy
4. **Configure Policy** — Disable user authentication requirement; enable device requirements (restrict to Windows devices; allow trusted and/or untrusted as needed)
5. **Apply Policy to Resources** — Modify each DC Resource to use the Windows SBL policy scoped to the Group
6. **Verify session length** — Confirm Minimum Authentication Requirements session length meets your needs (default: 30 days)

## Configuration Values

| Setting | Value |
|---|---|
| Client minimum version | v1.0.14 |
| Default session length | 30 days |
| Policy type | Device-only (user auth disabled) |
| Recommended device filter | Windows only |

## Access Conditions at Logon Screen
All three must be true:
- Windows Client v1.0.14+
- Signed into Twingate Client within last 30 days, **not** logged out
- Device marked as trusted in Twingate

## Gotchas
- **Explicit logout breaks SBL** — Session persistence does NOT survive if user manually logs out of the Twingate Client
- **Two policy types behave differently**: Device-only policies remain accessible while session is valid; Standard/Default policies require re-authentication after every restart
- **Session ≠ Resource auth**: Minimum Authentication Requirements govern client sign-in session, not per-resource auth
- Trusted Devices is recommended but not strictly required (untrusted devices can be permitted)

## Related Docs
- Active Directory with Twingate (use case guide)
- Device-only Resource Policies
- Trusted Devices
- Minimum Authentication Requirements