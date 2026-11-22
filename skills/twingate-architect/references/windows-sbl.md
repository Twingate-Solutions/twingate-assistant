---
source: https://www.twingate.com/docs/windows-sbl
type: docs
fetched: 2026-11-22
source_version: 265b42bc65f42b9c775a27a725900d815414fd2d0bd4aab59ddbe7d8348573be
trust: official
---

# How Windows Start Before Logon Works

## Summary
Windows Start Before Logon (SBL) lets a device reach a remote network at the Windows logon prompt, before the user authenticates on the machine. Twingate supports this by combining device-only Resource Policies with device requirements (such as Trusted Devices). A typical use is reaching an Active Directory domain controller for authentication or group policy.

## Key Information
- SBL is a Windows-specific workflow, usually done with a traditional VPN.
- Twingate uses Device-only Resource Policies (recommended) and Trusted Devices.
- Device-only policies have no user authentication requirement. Resources stay accessible while the Minimum Authentication Requirements session is valid and the device requirements are met.
- Standard Resource Policies, including the Default Policy, require user authentication. It must be re-validated after machine restarts or Client relaunches, so they will not work at the logon prompt.
- The Minimum Authentication Requirements session length defaults to 30 days. It persists across restarts and Client relaunches unless the user logs out of the Client.

## Prerequisites
- Domain controller addresses defined as Twingate Resources (see the Active Directory with Twingate guide).
- Windows devices running the Twingate Client.
- Devices marked as trusted in Twingate, if you require trust.
- A user who has signed in to the Client within the session window.

## Step-by-Step: Domain Controller Access via SBL
1. Add your Domain Controller addresses as Resources, following the Active Directory with Twingate example.
2. Create a Group, then add the Domain Controller Resources and the Users who need access.
3. In the Admin console, go to the Policies tab and select "Create Resource Policy". Name it "Windows SBL".
4. Disable user authentication requirements and enable device requirements. The example restricts access to Windows devices and allows both trusted and untrusted devices. Add a trust requirement if you want trusted devices only.
5. Modify the Resource Policy for each Resource so the device-only policy applies to the Resources and Users in this Group.
6. Verify the Minimum Authentication Requirements session length matches your needs.

## Configuration Values
- Minimum Authentication Requirements session length: default 30 days.
- Policy name used in the example: "Windows SBL".
- Policy settings: user authentication disabled, device requirements enabled, OS restricted to Windows.

## Gotchas
- Resources are reachable at the logon screen only if the user signed in to the Client within the last 30 days and has not signed out.
- Resources on standard policies will not be reachable at logon, because they need user re-authentication after a restart.
- The page's described outcome says devices must be trusted. The example policy as written permits untrusted devices too, so check the device requirement settings if you need trust enforced.
- Logging out of the Client ends the SBL capability until the user signs in again.

## Related Docs
- Device-only Resource Policies (https://www.twingate.com/docs/device-only-resource-policies)
- Trusted Devices / Device Security Guide (https://www.twingate.com/docs/device-security-guide)
- Active Directory with Twingate (https://www.twingate.com/docs/using-active-directory-with-twingate)
- Managing Devices, trusted devices section (https://www.twingate.com/docs/managing-devices#trusted-devices)