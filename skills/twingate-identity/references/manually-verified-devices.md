# Manually Verified Devices

## Summary
Admins can manually verify devices to satisfy Trusted Profile requirements using serial numbers or device instance verification. Serial number verification applies to any device matching a serial number; device instance verification applies to a specific user-device pair.

## Key Information
- Two verification methods: **serial number** (recommended) and **device instance**
- Serial numbers managed under **Devices > Serial Numbers** tab in Admin Console
- Serial numbers can be bulk-uploaded before or after devices sign in (supports pre-deployment verification)
- Device instance verification available on the Devices tab or a device's detail page
- Both methods can be configured via Admin Console or API

## Prerequisites
- Admin access to Twingate Admin Console
- Trusted Profile configured to use manual verification

## Step-by-Step

### Serial Number Verification
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Upload serial numbers (bulk upload supported)
3. Any device matching an uploaded serial number is verified

### Device Instance Verification
1. Navigate to **Devices** tab or a specific device's detail page
2. Open the device verification modal
3. Select the option to verify the device instance (specific user-device combination)

## Configuration Values
- No specific env vars or CLI flags documented
- API access available for both verification methods (refer to Twingate API docs)

## Gotchas
- Devices with **no serial number** can only use device instance verification
- Archived and blocked devices **can** be manually verified; verification persists through archive/block actions
- If a serial number is added for a device that was previously device instance verified → device is **reclassified** as serial number verified
- If that serial number is later **deleted** → device loses verified status entirely; it does **not** revert to device instance verified state
- Serial number deletion is destructive with no rollback to prior verification state

## Related Docs
- Trusted Profiles
- Devices tab (Admin Console)
- Twingate API documentation