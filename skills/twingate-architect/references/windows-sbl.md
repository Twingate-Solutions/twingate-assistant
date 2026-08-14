---
source: https://www.twingate.com/docs/windows-sbl
type: docs
fetched: 2026-08-14
source_version: 041f7fd5b9c11664f77d324f4c9bc91cf9974981303c75b4fa93f393f45f8e1b
---

# Windows Start Before Logon (SBL)

## Summary
Windows SBL allows devices to connect to remote networks at the Windows logon prompt before user authentication. Twingate implements this via Device-only Resource Policies combined with session persistence, enabling domain controller access without per-login user authentication.

## Key Information
- Requires Twingate Windows Client v1.0.14+
- Uses Device-only Resource Policies (no user auth requirement at resource access time)
- Session persists across restarts/client relaunches unless user explicitly logs out
- Default session length: 30 days (configurable via Minimum Authentication Requirements)
- Recommended alongside Trusted Devices feature for security
- Primary use case: Active Directory domain controller access at Windows logon screen

## Prerequisites
- Twingate Windows Client v1.0.14 or later
- Admin access to Twingate Admin console
- Domain Controller addresses defined as Twingate Resources
- (Recommended) Trusted Devices configured

## Step-by-Step Configuration

1. **Add Domain Controller as Resource** — Follow Active Directory with Twingate guide
2. **Create Group** — Add DC Resources and target Users to the group
3. **Create Resource Policy** — Name it "Windows SBL" via Policies tab in Admin console
4. **Configure Policy settings**:
   - Disable user authentication requirements
   - Enable device requirements
   - Set device filter (e.g., Windows only; trusted and/or untrusted)
5. **Apply Policy to Resources** — Modify each DC Resource to use the Windows SBL policy for the relevant Group
6. **Verify session length** — Check Minimum Authentication Requirements matches your tolerance (default: 30 days)

## Configuration Values
| Setting | Value |
|---|---|
| Minimum client version | v1.0.14 |
| Default session length | 30 days |
| User auth on resource | Disabled (Device-only policy) |
| Device requirement | Enabled (Windows; trusted recommended) |

## Access Conditions at Logon Screen
All three must be true:
- Client v1.0.14+
- User signed in within last 30 days and **has not logged out**
- Device marked as trusted in Twingate

## Gotchas
- **Explicit logout breaks SBL** — session does NOT persist if user logs out of Twingate Client
- **Standard/Default Policies require re-auth** after every restart or client relaunch — only Device-only policies bypass this
- Device-only policies are accessible solely based on session validity + device requirements; no per-access user auth prompt
- Session length applies globally via Minimum Authentication Requirements, not per-policy

## Related Docs
- [Active Directory with Twingate](https://www.twingate.com/docs/active-directory)
- Device-only Resource Policies documentation
- Trusted Devices documentation
- Minimum Authentication Requirements