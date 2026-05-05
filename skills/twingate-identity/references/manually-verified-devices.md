## Manually Verified Devices

How to mark devices as Trusted via Admin Console or API when no MDM/EDR Trust Method is available -- e.g., for contractor BYOD or test devices.

### Two Verification Modes

**Serial Number Verification** (recommended for most cases)
- Any device matching that serial number is considered verified
- Useful for company-issued hardware where the serial is the canonical identifier
- Bulk-uploadable via the Devices > Serial Numbers tab in Admin Console
- Can be uploaded **before or after** the device first signs in to Twingate -- pre-verification is supported

**Device Instance Verification** (for edge cases)
- Verifies a specific user-device combination only
- Other devices with the same serial number are NOT considered verified
- Use when:
  - Device has no serial number
  - Device has a non-unique serial (rare; mostly virtual machines)

### Workflow

**Bulk Upload Serial Numbers:**
- Admin Console -> Devices -> Serial Numbers tab -> upload (CSV/list)

**Verify a Specific Device:**
- Devices tab -> select the device -> Verify
- OR: device's detail page -> Verify
- Choose serial number verification or device instance verification

### State Interactions

| Action | Effect |
|---|---|
| Verify a serial number that's also a device instance verified device | Becomes serial-number-verified (more permissive) |
| Verify the serial then **delete** it | Device loses verification -- **does NOT** revert to instance-verified |
| Archive or block a verified device | Manual verification is **retained** through state changes |
| Manually verify an archived/blocked device | Allowed -- verification persists for future activation |

### Decision Notes

- **Always prefer serial number verification** unless the device genuinely lacks a unique serial
- For BYOD contractors: serial number verification works as long as you can collect serials at onboarding
- For VMs / cloud workstations without unique serials: device instance verification is the right answer
- Pre-verification (uploading serials before first sign-in) speeds up onboarding -- new hires can sign in and immediately satisfy Trusted Profiles

### Gotchas

- Deleting a serial doesn't restore the previous instance-verified state -- you'd have to re-verify the instance manually
- Manual verification is **per device**, not per user -- if the device passes to another user (rare), it remains verified
- Archived/blocked + manually verified devices retain their verification -- be deliberate about delete-vs-archive

### Related Docs

- /docs/trusted-devices -- Trusted Devices policy rule
- /docs/device-security-guide -- Trusted Profiles model with Manual Trust as a Trust Method
- /docs/managing-devices -- Devices tab + active/archived/blocked states
- /docs/api-overview -- API for programmatic verification
