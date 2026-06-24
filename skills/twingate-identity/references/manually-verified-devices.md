# Manually Verified Devices

## Summary
Admins can manually verify devices to satisfy Trusted Profile requirements using serial number or device instance verification. Serial number verification matches any device with a specified serial number; device instance verification targets a specific user-device pair.

## Key Information
- Two verification methods: **serial number** (recommended) and **device instance**
- Serial numbers managed under **Devices > Serial Numbers** tab in Admin Console
- Serial numbers can be bulk-uploaded before or after devices sign in (supports pre-deployment verification)
- Device instance verification available on **Devices** tab or individual device detail page
- Both methods satisfy Trusted Profile requirements

## Prerequisites
- Admin Console access
- Trusted Profile configured to use manual verification

## Step-by-Step

### Serial Number Verification
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Upload serial numbers (bulk upload supported)
3. Any device matching an uploaded serial number is considered verified

### Device Instance Verification
1. Navigate to **Devices** tab or specific device detail page
2. Open device verification modal
3. Select the option to verify device instance (specific user-device combination)

## Configuration Values
- Manageable via Admin Console or API
- Bulk upload available for serial numbers

## Gotchas
- Devices without serial numbers **cannot** be serial number verified — use device instance verification instead
- Archived and blocked devices **can** be manually verified; verification status is retained after archiving/blocking
- If a serial number is added for a device already instance-verified → device reclassifies as **serial number verified**
- If that serial number is later **deleted** → device loses verified status entirely; it does **not** revert to device instance verified
- Serial number verification takes precedence over device instance verification; deleting the serial number does not restore prior instance verification state

## Related Docs
- Trusted Profiles
- Devices tab (Admin Console)