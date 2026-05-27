# Manually Verified Devices

## Summary
Twingate admins can manually verify devices via Admin Console or API using two methods: serial number verification (recommended) or device instance verification. Serial number verification matches any device with a given serial number; device instance verification is scoped to a specific user-device pair.

## Key Information
- **Serial number verification**: Any device matching the serial number is verified; supports bulk upload; can pre-verify devices before first login
- **Device instance verification**: Only the specific user-device combination is verified; use when device lacks a unique or any serial number
- Serial numbers managed under **Devices > Serial Numbers** tab
- Device instance verification set via **Devices** tab or individual device details page

## Prerequisites
- Admin Console access or API credentials
- Device serial numbers (for serial number verification)

## Step-by-Step

### Serial Number Verification
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Upload serial numbers individually or via bulk upload
3. Devices matching uploaded serial numbers are automatically considered verified

### Device Instance Verification
1. Navigate to **Devices** tab or open a specific device's details page
2. Select the option to verify the device instance
3. Verification applies only to that user-device combination

## Configuration Values
- No environment variables or CLI flags documented on this page
- API support mentioned but no parameters specified here

## Gotchas
- Devices with **no serial number** can only be device instance verified
- If you serial-number-verify a previously device-instance-verified device, it converts to serial number verification — the instance verification is not retained
- If you later **delete** that serial number, the device loses verification entirely — it does **not** revert to device instance verified status
- Archived or blocked devices can be manually verified; verification status persists through archive/block actions
- Bulk upload works both before and after devices have signed in (pre-verification is supported)

## Related Docs
- Device management (Devices tab)
- Device Trust / verification policies
- Twingate API reference (for programmatic verification)