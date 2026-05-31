# Device Report

## Summary
Twingate allows admins to export device inventory data as a CSV file from the Admin Console. The report includes device metadata, Client version, and owner information. Reports are generated asynchronously and downloaded from the Reports page.

## Key Information
- Export format: CSV
- Generation locations: Devices page or Settings → Reports → Device List
- Filter options: Active, Archived, Blocked, or All Devices
- Delivery: Background generation; email notification sent when ready
- Generation time: Seconds for small datasets, minutes for large datasets

## Prerequisites
- Admin Console access
- Appropriate admin permissions on the Twingate network

## Step-by-Step

**Option 1 – From Devices page:**
1. Navigate to the **Devices** tab in Admin Console
2. Click **Download** above the device table
3. Select device filter (Active/Archived/Blocked/All Devices)
4. Click **Generate Report**

**Option 2 – From Reports page:**
1. Navigate to **Settings → Reports → Device List**
2. Click **Generate Device Report**
3. Select device filter (Active/Archived/Blocked/All Devices)
4. Click **Generate Report**

**Download:**
1. Wait for email notification or refresh the Reports page
2. Download completed report from the **Reports** page

## Report Schema (CSV Columns)

| Column | Description |
|--------|-------------|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of device owner |
| Owner name | Device owner's name |
| Device name | Twingate-assigned device name |
| Device type | `mobile`, `desktop`, or `laptop` |
| Active state | `active`, `archived`, or `blocked` |
| Is manually trusted | Boolean – manual trust status |
| Client version | Installed Client version |
| Hostname | Device hostname |
| Local username | Owner's local OS username |
| Serial number | Device serial number |
| Device manufacturer | Hardware manufacturer |
| Device model | Hardware model |
| OS platform | `macOS`, `Windows`, `Linux`, `iOS`, or `Android` |
| OS version | OS version string |
| Last resource access time | Timestamp of last Resource access |

## Gotchas
- Report generates in the background — do not expect immediate download
- Must return to the **Reports** page to download; cannot download directly from the generation dialog
- Large networks may experience multi-minute delays before the report is available

## Related Docs
- Devices overview
- Reports page documentation
- Device trust configuration