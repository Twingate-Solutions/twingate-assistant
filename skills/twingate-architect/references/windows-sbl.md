# Windows Start Before Logon (SBL)

## Summary
Windows SBL enables Twingate to connect to remote networks at the Windows logon prompt before user authentication. It uses Device-only Resource Policies combined with the Windows Twingate Client to allow access to resources (e.g., domain controllers) without requiring user credentials at login time.

## Key Information
- SBL requires Device-only Resource Policies, not standard user-authenticated policies
- Session persists across reboots unless user explicitly logs out of Twingate Client
- Default session length: 30 days (configurable via Minimum Authentication Requirements)
- Standard/Default Resource Policies **will not work** for SBL — they require re-authentication after each restart

## Prerequisites
- Twingate Windows Client **v1.0.14 or later**
- Trusted Devices feature (recommended)
- Users must authenticate to Twingate Client at least once before SBL works

## Step-by-Step Configuration

1. **Add Domain Controller addresses as Resources** in Twingate (see Active Directory with Twingate guide)
2. **Create a Group** containing:
   - The Domain Controller Resources
   - Users who need SBL access
3. **Create a Resource Policy** named "Windows SBL" (via Admin Console → Policies tab)
4. **Configure the policy**:
   - Disable user authentication requirements
   - Enable device requirements
   - Optionally restrict to Windows devices only (trusted and/or untrusted)
5. **Apply the policy** to each Domain Controller Resource for the SBL Group
6. **Verify Minimum Authentication Requirements** session length meets your needs (default: 30 days)

## Configuration Values

| Setting | Value | Notes |
|---|---|---|
| Client minimum version | v1.0.14 | Windows only |
| Default session length | 30 days | Configurable in Minimum Authentication Requirements |
| Device requirement | Windows only (recommended) | Trusted or untrusted selectable |
| User auth requirement | Disabled | Required for SBL to function |

## Access Conditions at Windows Logon Screen
All three must be true:
- Windows Client v1.0.14+
- Signed into Twingate Client within last 30 days and **not** logged out
- Device marked as trusted in Twingate

## Gotchas
- Users must log in to Twingate Client **at least once** before SBL is available — SBL does not work on first-time setup
- Explicit logout from the Twingate Client breaks SBL until re-authentication occurs
- Standard Resource Policies (including Default Policy) require re-validation after every restart — do not use for SBL resources
- Device-only policies bypass user auth entirely; access control relies solely on device trust status

## Related Docs
- Active Directory with Twingate (use case guide)
- Trusted Devices
- Minimum Authentication Requirements
- Device-only Resource Policies