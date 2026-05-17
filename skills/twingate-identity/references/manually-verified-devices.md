# Manually Verified Devices

## Summary
Twingate admins can manually verify devices via the Admin Console or API using two methods: serial number verification (recommended) or device instance verification. Serial number verification applies to any device matching that serial number; device instance verification is scoped to a specific user-device combination.

## Key Information
- **Serial number verification**: Any device matching the serial number is verified; recommended for most cases
- **Device instance verification**: Only the specific user-device combination is verified; use when device has no unique/no serial number
- Serial numbers can be bulk uploaded before or after devices sign in (pre-verify or retroactive)
- Archived and blocked devices can be manually verified; verification status persists through archive/block actions

## Prerequisites
- Admin Console access or API access
- Admin role in Twingate

## Step-by-Step

### Serial Number Verification
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Upload serial numbers (individually or bulk CSV)

### Device Instance Verification
1. Navigate to **Devices** tab, select the target device
2. Choose verify option on the device listing or device details page
3. Select device instance verification

## Configuration Values
- Managed via Admin Console UI or Twingate API (no CLI flags/env vars documented on this page)

## Gotchas
- If you serial-number-verify a previously device-instance-verified device, it becomes a **serial number verified device** (instance verification is replaced, not stacked)
- If you then **delete that serial number**, the device becomes **unverified** — it does **not** revert to device instance verified status
- Devices with no serial number can only use device instance verification
- Bulk upload works for both pre-existing and not-yet-enrolled devices

## Related Docs
- Device Management
- Device Trust / Device Policy
- Twingate API reference (for programmatic verification)