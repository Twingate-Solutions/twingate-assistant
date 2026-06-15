# Manually Verified Devices

## Summary
Admins can manually verify devices to satisfy Trusted Profile requirements using two methods: serial number verification (recommended) or device instance verification. Verification can be done via Admin Console or API.

## Key Information
- **Serial number verification**: Any device matching a specified serial number is verified — recommended for most cases
- **Device instance verification**: Verifies a specific user-device combination — use when device lacks a unique or any serial number
- Serial numbers managed under **Devices > Serial Numbers** tab in Admin Console
- Serial numbers can be bulk-uploaded before or after devices sign in (supports pre-deployment verification)
- Device instance verification available on **Devices** tab or individual device detail page

## Configuration Values
- No env vars or CLI flags documented; management via Admin Console UI or API

## Behavior / Edge Cases (Gotchas)
- Devices with **no serial number** can only use device instance verification
- Archived or blocked devices **can** be manually verified; verification is retained through archive/block actions
- If a serial number is added for a device instance-verified device → device is **reclassified** as serial number verified (instance verification dropped)
- If that serial number is then **deleted** → device loses verified status entirely and does **not** revert to device instance verified state
- Deletion of a serial number is a one-way action regarding verification state — previous instance verification is not restored

## Prerequisites
- Admin role in Twingate Admin Console
- Trusted Profile configured to use manual verification as a verification method

## Step-by-Step

**Serial Number Verification (Bulk Upload):**
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Upload serial numbers (CSV or similar bulk method)
3. Devices matching those serial numbers are considered verified

**Device Instance Verification:**
1. Navigate to **Devices** tab or a specific device's detail page
2. Open the device verification modal
3. Select the option to verify the device instance

## Related Docs
- Trusted Profiles (verification method configuration)
- Devices tab (Admin Console)