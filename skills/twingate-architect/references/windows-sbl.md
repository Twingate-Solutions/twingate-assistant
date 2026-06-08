# Windows Start Before Logon (SBL)

## Summary
Windows SBL enables network connectivity at the Windows logon prompt before user authentication, replacing traditional VPN for domain controller access. Twingate implements this using Device-only Resource Policies combined with session persistence in the Windows client.

## Key Information
- Requires Twingate Windows Client v1.0.14+
- Uses Device-only Resource Policies (no user auth requirement at resource access time)
- Session persists across restarts unless user explicitly logs out
- Default session length: 30 days (configurable via Minimum Authentication Requirements)
- Recommended companion: Trusted Devices feature

## Prerequisites
- Twingate Windows Client v1.0.14 or later
- Admin access to Twingate Admin console
- Domain Controller addresses configured as Resources
- (Recommended) Trusted Devices configured

## Step-by-Step Configuration

1. **Add Domain Controller as Resource** — Follow Active Directory with Twingate guide
2. **Create Group** — Add DC Resources and target Users to the group
3. **Create Resource Policy named "Windows SBL"** — Via Policies tab in Admin console
4. **Configure Policy settings:**
   - Disable user authentication requirements
   - Enable device requirements (restrict to Windows devices; choose trusted and/or untrusted)
5. **Apply Policy to each DC Resource** — Scope policy to the specific Resources and Users in the group
6. **Verify Minimum Authentication Requirements** — Confirm session length matches your needs (default: 30 days)

## Configuration Values

| Setting | Value |
|---|---|
| Client minimum version | v1.0.14 |
| Default session length | 30 days |
| User auth on Device-only Policy | Disabled |
| Device requirement | Windows only (trusted recommended) |

## How Authentication Works

- **Device-only policies**: Accessible as long as Minimum Auth Requirements session is valid + device requirements met
- **Standard/Default policies**: Require user auth re-validation on every restart or client relaunch
- Session survives machine restarts and client relaunches unless user explicitly logs out

## End-User Requirements for SBL to Work
- Windows Client v1.0.14+
- Signed into Twingate Client within last 30 days
- Have **not** logged out of the Twingate Client
- Device marked as trusted in Twingate (if trusted device policy applied)

## Gotchas
- Users must authenticate at least once before SBL works — the 30-day session must be established
- Explicit logout breaks SBL until user signs in again
- Default Policy includes user auth requirements and will **not** work at logon screen
- Untrusted devices can be permitted, but Trusted Devices is recommended for security

## Related Docs
- Active Directory with Twingate (use case guide)
- Trusted Devices documentation
- Minimum Authentication Requirements configuration
- Device-only Resource Policies