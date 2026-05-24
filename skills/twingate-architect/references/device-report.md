# Device Report

## Summary
Twingate Admin Console allows exporting device inventory as a CSV file. The report includes device metadata, Client version, and owner information. Reports are generated asynchronously and downloaded from the Reports page.

## Key Information
- Export format: CSV
- Two entry points: Devices page or Settings → Reports page
- Filter options: Active, Archived, Blocked, or All Devices
- Generation is async; notification sent via email when ready
- Most exports complete in seconds; large datasets may take minutes

## Prerequisites
- Access to Twingate Admin Console
- Appropriate admin permissions

## Step-by-Step

**Option 1 – From Devices page:**
1. Navigate to **Devices** tab
2. Click **Download** button above the device table
3. Select device filter (Active/Archived/Blocked/All Devices)
4. Click **Generate Report**

**Option 2 – From Reports page:**
1. Navigate to **Settings → Reports → Device List**
2. Click **Generate Device Report**
3. Select device filter (Active/Archived/Blocked/All Devices)
4. Click **Generate Report**

**Download:**
- Refresh the Reports page or wait for email notification
- Download completed report from the **Reports** page

## Report Schema (CSV Columns)

| Column | Values/Notes |
|---|---|
| Device ID | Twingate internal ID |
| Owner user ID | Twingate user ID |
| Owner name | Display name |
| Device name | Twingate device name |
| Device type | mobile, desktop, laptop |
| Active state | active, archived, blocked |
| Is manually trusted | boolean |
| Client version | Twingate Client version string |
| Hostname | Device hostname |
| Local username | OS-level username |
| Serial number | Hardware serial |
| Device manufacturer | Hardware vendor |
| Device model | Hardware model |
| OS platform | macOS, Windows, Linux, iOS, Android |
| OS version | OS version string |
| Last resource access time | Timestamp of last Resource access |

## Gotchas
- Report download only available from the **Reports** page, not the Devices page (even if generated from Devices page)
- No direct API reference mentioned; report generation is UI-only per this documentation
- Large device counts may delay generation by several minutes

## Related Docs
- [Devices](https://www.twingate.com/docs/devices)
- Reports page (Settings → Reports)