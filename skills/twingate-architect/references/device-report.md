# Device Report

## Summary
Twingate's device report exports detailed information about all devices on an account as a CSV file. Reports are generated via the Admin Console and include device metadata, Client version, and owner information. Reports can be filtered by device state before export.

## Key Information
- Export format: CSV file
- Two entry points: Devices page or Reports page (Settings → Reports → Device List)
- Filter options: Active, Archived, Blocked, or All Devices
- Report generates in background; notification sent via email when ready
- Download completed reports from the Reports page

## Prerequisites
- Access to Twingate Admin Console

## Step-by-Step

**Option 1 – From Devices page:**
1. Navigate to the **Devices** tab in Admin Console
2. Click **Download** button above the device table

**Option 2 – From Reports page:**
1. Navigate to **Settings → Reports → Device List**
2. Click **Generate Device Report**

**Complete report generation:**
3. Select device filter: `Active`, `Archived`, `Blocked`, or `All Devices`
4. Click **Generate Report**
5. Wait for email notification or refresh the Reports page
6. Download completed report from the Reports page

## Configuration Values
No CLI flags, API params, or environment variables — UI-only workflow.

## Report Schema (CSV Columns)

| Column | Description |
|---|---|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of owner |
| Owner name | Device owner's name |
| Device name | Twingate device name |
| Device type | `mobile`, `desktop`, or `laptop` |
| Active state | `active`, `archived`, or `blocked` |
| Is manually trusted | Boolean |
| Client version | Twingate Client version |
| Hostname | Device hostname |
| Local username | Owner's local username |
| Serial number | Device serial number |
| Device manufacturer | Manufacturer name |
| Device model | Device model |
| OS platform | `macOS`, `Windows`, `Linux`, `iOS`, or `Android` |
| OS version | OS version string |
| Last resource access time | Timestamp of last Resource access |

## Gotchas
- Large device lists may take several minutes to generate
- Must navigate to the Reports page to download even if triggered from the Devices page
- No direct API export documented here — admin UI required

## Related Docs
- Devices overview
- Reports page (Settings → Reports)