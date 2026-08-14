---
source: https://www.twingate.com/docs/manually-verified-devices
type: docs
fetched: 2026-08-14
source_version: ab04e546eb70b45da46b4959149883eb7783aa88288b7f9918748646db0ac12e
---

# Manually Verified Devices

## Page Title
Manually Verified Devices

## Summary
Admins and Helpdesk admins can manually verify devices via the Admin Console or API to satisfy Trusted Profile requirements. Two verification methods exist: serial number (recommended) and device instance (for devices without unique serial numbers).

## Key Information
- **Serial number verification**: Any device matching a specified serial number is verified; managed under **Devices > Serial Numbers** tab
- **Device instance verification**: Verifies a specific user-device combination; available on the Devices tab or a device's detail page
- Bulk serial number upload supported before or after devices have signed into Twingate (enables pre-deployment verification)
- Manual verification is retained when a device is archived or blocked

## Prerequisites
- Admin or Helpdesk Admin role required
- Trusted Profile must be configured to use manual verification as a verification method

## Step-by-Step

### Serial Number Verification
1. Navigate to **Devices > Serial Numbers** tab in Admin Console
2. Upload serial numbers (individually or bulk)
3. Any device matching an uploaded serial number is considered verified

### Device Instance Verification
1. Navigate to **Devices** tab or a specific device's detail page
2. Open the device verification modal
3. Select the option to verify the device instance

## Configuration Values
- No specific env vars or CLI flags documented
- API access available (no specific endpoints listed on this page)

## Gotchas
- If a serial number is deleted after a device was reclassified from device instance → serial number verified, the device loses verification entirely and does **not** revert to device instance verified
- Devices with no serial number can **only** be device instance verified
- Verifying a serial number on a device that was previously device instance verified reclassifies it as serial number verified (prior state lost)
- Archived/blocked devices can be verified, but this may have unintended access implications depending on Trusted Profile rules

## Related Docs
- Trusted Profiles
- Devices (Admin Console)