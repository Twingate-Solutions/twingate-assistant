# Manually Verified Devices

## Summary
Twingate admins can manually verify devices via Admin Console or API using two methods: serial number verification (recommended) or device instance verification. Serial number verification applies to any device matching that serial number; device instance verification applies only to a specific user-device combination.

## Key Information
- **Serial number verification**: Verifies all devices sharing a serial number; recommended for most cases
- **Device instance verification**: Verifies only a specific user-device combination; use when device lacks a unique or any serial number
- Serial numbers can be bulk uploaded before or after devices sign in (pre-verification supported)
- Both archived and blocked devices can be manually verified; verification status persists through archive/block actions

## Configuration Locations
| Action | Location |
|--------|----------|
| Bulk upload serial numbers | Admin Console → Devices → Serial Numbers tab |
| Device instance verification | Admin Console → Devices tab (per device) or device details page |

## Behavior Rules / Gotchas
- If you serial-number-verify a device that was previously device-instance-verified, it becomes a **serial number verified** device (instance verification is replaced)
- If you later **delete** that serial number, the device loses verification entirely — it does **not** revert to device instance verified
- Devices with no serial number can only use device instance verification
- Verification is retained when a device is archived or blocked, but can still be manually applied to archived/blocked devices

## Step-by-Step: Serial Number Bulk Upload
1. Navigate to **Devices** → **Serial Numbers** tab in Admin Console
2. Upload serial numbers (CSV or similar bulk format)
3. Devices matching those serial numbers are marked verified immediately

## Step-by-Step: Device Instance Verification
1. Navigate to **Devices** tab in Admin Console
2. Select the target device or open its details page
3. Choose the device instance verification option

## Decision Guide
| Scenario | Use |
|----------|-----|
| Standard managed devices with serial numbers | Serial number verification |
| Device has no serial number | Device instance verification |
| Device has non-unique serial number | Device instance verification |
| Pre-provisioning before user enrollment | Serial number verification (bulk upload) |

## Related Docs
- Device Trust / Device Policies
- Admin Console – Devices tab
- Twingate API (for programmatic verification)