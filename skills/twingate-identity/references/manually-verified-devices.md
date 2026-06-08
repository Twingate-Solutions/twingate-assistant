# Manually Verified Devices

## Summary
Admins can manually verify devices to satisfy Trusted Profile requirements using either serial number or device instance verification. Serial number verification applies to any device matching a serial number; device instance verification applies to a specific user-device pair.

## Key Information
- Two verification types: **serial number** (recommended) and **device instance**
- Serial number verification: any device with a matching serial number is verified
- Device instance verification: a specific user+device combination is verified
- Serial numbers managed in **Devices > Serial Numbers** tab in Admin Console
- Bulk upload supported for serial numbers (pre-deployment or post-deployment)
- Both methods satisfy Trusted Profile requirements

## Prerequisites
- Admin Console access
- Trusted Profiles configured (manual verification is a method within Trusted Profiles)

## Step-by-Step

### Serial Number Verification
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Upload serial numbers (bulk upload supported via CSV or API)

### Device Instance Verification
1. Navigate to **Devices** tab or a specific device's detail page
2. Open the device verification modal
3. Select the option to verify the device instance (specific user-device combination)

## Configuration Values
- Verification methods available via: Admin Console or API
- Bulk upload location: **Devices > Serial Numbers** tab

## Gotchas
- Devices with **no serial number** can only use device instance verification
- Archived/blocked devices **can** be manually verified; verification is retained when archived or blocked
- If a serial number is added for a device that was previously device instance verified → device is **reclassified** as serial number verified
- If that serial number is later **deleted** → device loses verified status entirely; does **not** revert to device instance verified state
- Serial number takes precedence over device instance verification; deletion of the serial number does not restore the prior state

## Related Docs
- Trusted Profiles
- Devices tab (Admin Console)