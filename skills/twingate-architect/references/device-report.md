# Device Report

## Summary
Twingate allows admins to export device inventory data as a CSV file from the Admin Console. The report includes device metadata, Client version, and owner information. Reports can be filtered by device state and are generated asynchronously.

## Key Information
- Export format: CSV file
- Access via: Admin Console → Devices tab OR Settings → Reports → Device List
- Filter options: Active, Archived, Blocked, or All Devices
- Generation is asynchronous; notification sent via email when ready
- Download completed reports from the Reports page

## Prerequisites
- Admin Console access
- Appropriate admin permissions on the Twingate network

## Step-by-Step

**Option 1 – From Devices page:**
1. Navigate to Admin Console → **Devices** tab
2. Click **Download** button above the device table
3. Select device filter (Active/Archived/Blocked/All Devices)
4. Click **Generate Report**

**Option 2 – From Reports page:**
1. Navigate to Admin Console → **Settings** → **Reports** → **Device List**
2. Click **Generate Device Report**
3. Select device filter (Active/Archived/Blocked/All Devices)
4. Click **Generate Report**

**Retrieve report:**
- Refresh the Reports page or wait for email notification
- Download from the Reports page once ready

## Report Schema (CSV Columns)

| Column | Description |
|---|---|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of owner |
| Owner name | Owner's display name |
| Device name | Twingate device name |
| Device type | mobile, desktop, or laptop |
| Active state | active, archived, or blocked |
| Is manually trusted | Boolean: manual trust status |
| Client version | Twingate Client version installed |
| Hostname | Device hostname |
| Local username | Owner's local OS username |
| Serial number | Device serial number |
| Device manufacturer | Hardware manufacturer |
| Device model | Hardware model |
| OS platform | macOS, Windows, Linux, iOS, or Android |
| OS version | OS version string |
| Last resource access time | Timestamp of last Resource access |

## Gotchas
- Large device counts may take several minutes to generate
- Must return to the Reports page to download; report is not immediately available inline
- No direct API or CLI method described — UI-only workflow

## Related Docs
- [Devices](https://www.twingate.com/docs/devices)
- [Reports](https://www.twingate.com/docs/reports)