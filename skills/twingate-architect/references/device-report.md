# Device Report

## Summary
Twingate allows admins to export device inventory data to CSV from the Admin Console. The report includes device metadata, Client version, and owner information. Reports can be filtered by device state and are generated asynchronously.

## Key Information
- Export format: CSV file
- Generated via Admin Console (two entry points)
- Supports filtering by device state: Active, Archived, Blocked, or All Devices
- Generation is asynchronous; notification sent via email when ready
- Most exports complete in seconds; large datasets may take a few minutes

## Prerequisites
- Access to Twingate Admin Console
- Appropriate admin permissions

## Step-by-Step

**Option 1 – From Devices page:**
1. Navigate to **Devices** tab in Admin Console
2. Click **Download** button above the device table

**Option 2 – From Reports page:**
1. Navigate to **Settings → Reports → Device List**
2. Click **Generate Device Report**

**Configure & Download:**
1. Select device filter: `Active`, `Archived`, `Blocked`, or `All Devices`
2. Click **Generate Report**
3. Wait for email notification or refresh the Reports page
4. Download completed report from the **Reports** page

## Report Schema (CSV Columns)

| Column | Description |
|--------|-------------|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of owner |
| Owner name | Owner's name |
| Device name | Twingate-assigned device name |
| Device type | `mobile`, `desktop`, or `laptop` |
| Active state | `active`, `archived`, or `blocked` |
| Is manually trusted | Whether device is manually trusted |
| Client version | Twingate Client version |
| Hostname | Device hostname |
| Local username | Owner's local OS username |
| Serial number | Device serial number |
| Device manufacturer | Hardware manufacturer |
| Device model | Hardware model |
| OS platform | `macOS`, `Windows`, `Linux`, `iOS`, or `Android` |
| OS version | OS version string |
| Last resource access time | Timestamp of last Resource access |

## Gotchas
- Report is generated in the background — not available for immediate download
- Must return to the **Reports** page to download, even if initiated from the Devices page
- No API-based export mentioned; Admin Console is required

## Related Docs
- Devices documentation
- Reports page (Settings → Reports)