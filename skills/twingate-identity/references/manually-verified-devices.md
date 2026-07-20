# Manually Verified Devices

## Summary
Admins can manually verify devices to satisfy Trusted Profile requirements using two methods: serial number verification (recommended) or device instance verification. Serial numbers can be bulk-uploaded pre- or post-deployment; device instance verification targets specific user-device combinations.

## Key Information
- **Serial number verification**: Any device matching a specified serial number is verified — recommended for most cases
- **Device instance verification**: Verifies a specific user-device pair — use when device lacks a unique or any serial number
- Serial numbers managed under **Devices > Serial Numbers** tab in Admin Console
- Bulk upload of serial numbers supported before or after devices have signed into Twingate
- Both methods satisfy Trusted Profile requirements

## Prerequisites
- Admin access to Twingate Admin Console
- Trusted Profile configured to use manual verification as a verification method

## Step-by-Step

### Serial Number Verification
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Bulk-upload serial numbers (CSV or similar)
3. Devices matching uploaded serial numbers are automatically considered verified

### Device Instance Verification
1. Navigate to **Devices** tab or a specific device's detail page
2. Open the device verification modal
3. Select option to verify the device instance

## Configuration Values
- No environment variables or API parameters documented on this page
- API-based verification available (referenced but not detailed here)

## Gotchas
- Devices with **no serial number** can only be device instance verified
- Archived and blocked devices **can** be manually verified; verification status is retained through archive/block actions
- If a serial number is applied to an already device-instance-verified device, it is **reclassified** as serial number verified
- If that serial number is later **deleted**, the device loses verified status entirely — it does **not** revert to device instance verified state
- Serial number and device instance verification are mutually exclusive per device at any given time

## Related Docs
- Trusted Profiles (verification method configuration)
- Devices tab (Admin Console)