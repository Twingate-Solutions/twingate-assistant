## Device Administration

Reference for the Twingate Devices tab -- how device data is displayed, what attributes are tracked, and how to manage device state (active / archived / blocked).

### Where Devices Appear

- **User detail page** -- devices the user has connected from
- **Devices tab** (top-level) -- all devices in the org

### Device Attributes

| Attribute | Description | Platforms |
|---|---|---|
| **Name** | Friendly name set by user | Windows, macOS, iOS |
| **Hostname** | DNS hostname assigned by device | Windows, macOS, Linux |
| **Make** | Manufacturer | macOS, Linux, iOS |
| **Model** | Model name | macOS, Linux, iOS |
| **OS name** | Operating system name | All |
| **OS version** | OS version number | All |
| **Serial number** | Hardware serial | Windows, macOS, Linux |
| **Local username** | OS-level user running Twingate | Windows, macOS, Linux |
| **Client version** | Twingate Client version | All |
| **Active state** | active / archived / blocked | All |
| **Connection indicator** | Green dot if currently signed in | All |
| **Internet Security** | Internet Security configuration status | Windows, macOS, Linux |

### Device Active States

| State | Use Case | Admin Console Visibility | Resource Access |
|---|---|---|---|
| **Active** | Default; in-use devices | Visible | Yes (subject to Security Policy) |
| **Archived** | Old / deprecated devices; auto-archived after 90 days inactivity | Filtered out | Requires sign-in (re-auth restores active state) |
| **Blocked** | Lost, stolen, or deprecated | Filtered out | **No access** |

**Auto-archival**: any device that hasn't signed in or accessed a Resource for **90 days** is automatically archived.

**State Transitions:**
- **Active → Archived** (manual or automatic) -- signs the user out; re-auth restores active
- **Active → Blocked** (manual) -- signs the user out; user can NOT sign in again from this device
- **Archived → Active** (automatic) -- when the user re-authenticates
- **Blocked → ?** -- effectively permanent unless an admin manually restores

### Verified Devices

Devices can be verified via:
- EDR/MDM Trust Methods (CrowdStrike, Intune, Jamf, Kandji, SentinelOne, 1Password)
- **Manual verification** (per /docs/manually-verified-devices)

Verified status can be required by Security Policies (Trusted Profile or Custom device rule).

### Decision Notes

- Use **Block** for lost/stolen devices, NOT Archive -- Archive lets the user back in upon re-auth
- 90-day auto-archive is a useful housekeeping default; users with seasonal access patterns may bounce in/out
- The Connection Indicator (green dot) is real-time -- useful for quick triage when troubleshooting access issues
- Bulk operations (block all devices for a user) require API calls; the Admin Console is per-device

### Gotchas

- Manual archive logs the user out -- they don't get a notification, just a "please sign in again" prompt next time they connect
- Blocked + manually verified state is allowed (verification is retained) -- explicit unblock is needed to restore access
- Mobile (iOS/Android) attributes are sparser than desktop -- some fields just aren't reported by the platform

### Related Docs

- /docs/devices -- Devices overview
- /docs/manually-verified-devices -- Manual verification workflow
- /docs/device-security-guide -- Trusted Profiles
- /docs/managed-devices -- MDM-deployed Clients
- /docs/trusted-devices -- Trusted Devices policy rule
