## Windows Start Before Logon (SBL)

Enables Twingate-authenticated access to domain controllers (or other resources) at the Windows logon screen, before user authentication, using device-only Resource Policies. Replaces VPN-based SBL for Active Directory connectivity.

**Key Information:**
- Requires Twingate Windows Client v1.0.14 or later
- Uses device-only Resource Policies -- no user authentication requirement for SBL resources
- Default session length is 30 days; users must re-authenticate at least once every 30 days
- Session persists across reboots and Client restarts unless the user explicitly logs out
- Domain controller Resources are accessible at the Windows logon screen only when the above conditions are met
- Device must be marked as Trusted in Twingate (recommended)

**Prerequisites:**
- Twingate Windows Client v1.0.14+
- Domain Controller Resources already defined in Twingate (see `/docs/active-directory`)
- Admin access to Twingate Admin Console

**Step-by-Step:**
1. Add domain controller addresses as Resources in Twingate (follow Active Directory guide)
2. Create a Group, add the domain controller Resources and target users
3. Create a Resource Policy named `Windows SBL` (Policies tab → Create Resource Policy)
4. In the policy: disable user authentication requirements; enable device requirements (Windows devices; optionally restrict to Trusted only)
5. Apply the Windows SBL policy to each domain controller Resource for the target Group
6. Verify Minimum Authentication Requirements session length meets your needs (default: 30 days)

**Configuration Values:**
- Minimum session length: 30 days (default)
- SBL Client version minimum: v1.0.14
- Device restriction: Windows only (optionally Trusted devices)

**Gotchas:**
- Standard Resource Policies (including the Default Policy) require user authentication re-validated after every reboot -- SBL only works for Resources with device-only policies
- If the user logs out of the Twingate Client, SBL access is lost until they log in again
- Trusted device requirement is recommended but optional -- untrusted Windows devices can also be allowed

**Related Docs:**
- /docs/active-directory -- Configuring Active Directory resources with Twingate
- /docs/resource-policies -- Device-only policy configuration
- /docs/device-trust -- Trusted device setup
- /docs/minimum-authentication -- Session length configuration
