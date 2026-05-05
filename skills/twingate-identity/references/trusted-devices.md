## Trusted Devices Rule

A Security Policy rule that requires the device to be **marked as trusted** before allowing sign-in or Resource access. Applied to MAR and Resource Policies.

**Functionality:**
- When enabled on a policy, only devices that meet a Trusted Profile are allowed
- Untrusted devices attempting to sign in (MAR) or access a Resource (Resource Policy) are blocked
- Enforced for any device running the Twingate Client, regardless of platform or location

**What Makes a Device "Trusted":**
A device is considered trusted if it meets the requirements of a **Trusted Profile** -- defined in the Admin Console under Device Security settings.

A Trusted Profile combines:
- **Verification method**: automated (CrowdStrike, SentinelOne, Jamf, Kandji, Intune, etc.) or manual (admin marks the device verified)
- **Device posture checks**: HD encryption, screen lock, firewall, antivirus, biometric configuration, etc.

A device must satisfy **all** elements of at least one Trusted Profile to be considered trusted.

**Setup Pattern:**
1. Configure EDR/MDM integration in Admin Console (Device Settings)
2. Create one or more Trusted Profiles per (OS, verification method) combination
3. Add posture checks (encryption, screen lock, etc.) to each Profile as required
4. Apply the **Trusted Devices** rule to MAR or Resource Policies

**Common Profile Layouts:**

| Profile | OS | Verification |
|---|---|---|
| Corporate Mac | macOS | CrowdStrike (automatic) |
| Corporate Windows | Windows | CrowdStrike or SentinelOne (automatic) |
| Contractor Windows | Windows | Manual verification (Twingate Serial Number) |
| Contractor Mac (BYOD) | macOS | None -- native posture only |

**Decision Notes:**
- Most production environments require Trusted Devices on most Resource Policies
- For BYOD users without EDR: create a Profile with native posture checks only (Screen Lock, Disk Encryption, Biometrics)
- "Any Device" is appropriate only for very-low-risk Resources or for the IdP Resource accessed by the Everyone Group

**Gotchas:**
- A device's trust status is evaluated per policy -- the same device can satisfy one Profile and not another
- Devices verified manually by an admin can be marked untrusted at any time -- the device immediately loses access on the next policy evaluation
- Posture checks (encryption, screen lock) are evaluated by the Twingate Client locally -- some checks may not be available on all platforms

**Related Docs:**
- /docs/device-security-guide -- Device Security settings + Trusted Profiles
- /docs/manually-verified-devices -- Manual verification flow
- /docs/managed-devices -- EDR/MDM integration
- /docs/device-posture-checks -- Posture check reference
- /docs/security-policies -- Policy types overview
- /docs/security-policies-best-practices -- Worked example with Trusted Profiles
