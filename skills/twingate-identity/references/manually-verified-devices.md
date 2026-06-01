# Manually Verified Devices

## Summary
Admins can manually verify devices to satisfy Trusted Profile requirements using two methods: serial number verification (matches any device with that serial) or device instance verification (specific user-device pair). Both methods are manageable via Admin Console or API.

## Key Information
- **Serial number verification**: Recommended method; any device matching the serial number is verified
- **Device instance verification**: Use when device lacks a unique or any serial number; ties verification to a specific user-device combination
- Serial numbers managed at **Devices > Serial Numbers** tab in Admin Console
- Serial numbers can be bulk-uploaded before or after devices sign in (supports pre-deployment verification)
- Device instance verification accessed from **Devices** tab or individual device detail page

## Prerequisites
- Admin access to Twingate Admin Console
- Trusted Profile configured (manual verification is one of its verification methods)

## Step-by-Step

### Serial Number Verification
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Upload serial numbers (bulk upload supported)
3. Devices matching uploaded serials are automatically considered verified

### Device Instance Verification
1. Navigate to **Devices** tab or open a specific device's detail page
2. Open device verification modal
3. Select option to verify the device instance

## Configuration Values
- No specific env vars or CLI flags documented
- API available as alternative to Admin Console for both verification types

## Gotchas
- If a serial number is added to a device-instance-verified device, it is **reclassified** as serial number verified
- If that serial number is later **deleted**, the device loses verification entirely — it does **not** revert to device instance verified status
- Devices with no serial number can only use device instance verification
- Archived and blocked devices **can** be manually verified; verification is **retained** when a device is archived or blocked

## Related Docs
- [Trusted Profiles](https://www.twingate.com/docs/trusted-profiles)
- Devices tab (Admin Console)