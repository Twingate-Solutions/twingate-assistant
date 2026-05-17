# Windows Start Before Logon (SBL)

## Summary
Windows SBL enables network connectivity at the Windows logon prompt before user authentication, replacing traditional VPN for domain controller access. Twingate implements this via device-only Resource Policies combined with session persistence. Users must authenticate to Twingate at least once within the session window (default 30 days).

## Key Information
- SBL works by creating device-only policies that don't require re-validation between restarts
- Standard/Default policies require user authentication re-validation after each restart — they do NOT support SBL
- Session length defaults to 30 days; configurable via Minimum Authentication Requirements
- Session persists across reboots unless user explicitly logs out of Twingate Client

## Prerequisites
- Twingate Windows Client v1.0.14 or later
- Trusted Devices feature (recommended)
- Domain Controller resources already added to Twingate (see Active Directory with Twingate docs)

## Step-by-Step Configuration

1. **Add Domain Controller as Resource** — Follow Active Directory with Twingate guide
2. **Create a Group** — Add DC Resources and target Users to the group
3. **Create Resource Policy** — Name it (e.g., "Windows SBL"); create via Admin Console → Policies tab
4. **Configure Policy settings**:
   - Disable user authentication requirements
   - Enable device requirements (restrict to Windows devices)
   - Optionally restrict to trusted devices only
5. **Apply Policy to Resources** — Modify each DC Resource to use the new SBL policy, scoped to the Group
6. **Verify session length** — Confirm Minimum Authentication Requirements session length meets your needs (default: 30 days)

## Configuration Values
| Setting | Value |
|---|---|
| Min Client version | v1.0.14+ |
| Default session length | 30 days |
| User auth requirement | Disabled (device-only policy) |
| Device type restriction | Windows (recommended) |

## Gotchas
- **Logout breaks SBL**: If a user manually logs out of the Twingate Client, the session is invalidated and SBL will not work until they log in again
- **Standard/Default Policy does NOT support SBL**: User auth requirement is always re-validated on restart — only device-only policies skip this
- **Trusted vs. untrusted devices**: Example config allows both, but production deployments should restrict to trusted devices for security
- **Session expiry**: After 30 days without re-authentication, SBL access stops until user logs in again

## Related Docs
- Active Directory with Twingate (use case guide)
- Device-only Resource Policies
- Trusted Devices
- Minimum Authentication Requirements