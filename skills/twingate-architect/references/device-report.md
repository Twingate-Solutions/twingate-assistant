# Device Report

## Summary
Twingate Admin Console can export a CSV report of all devices on an account. The report includes device metadata, Client version, and owner information. Reports are generated asynchronously and downloaded from the Reports page.

## Key Information
- Export format: CSV file
- Generated via Admin Console (not API)
- Two entry points: Devices page or Reports page
- Report scope options: Active, Archived, Blocked, or All Devices
- Generation is asynchronous; notification sent via email when ready

## Prerequisites
- Access to Twingate Admin Console
- Sufficient admin permissions to view Devices/Reports sections

## Step-by-Step

**Option 1 — From Devices page:**
1. Navigate to **Devices** tab in Admin Console
2. Click **Download** button above the device table

**Option 2 — From Reports page:**
1. Navigate to **Settings → Reports → Device List**
2. Click **Generate Device Report**

**Complete the report:**
3. Select device filter: `Active`, `Archived`, `Blocked`, or `All Devices`
4. Click **Generate Report**
5. Wait for email notification or refresh the Reports page
6. Download the completed report from the **Reports** page

## Configuration Values
No environment variables or API parameters — UI-only feature.

## Report Schema (CSV Columns)

| Column | Description |
|---|---|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of owner |
| Owner name | Owner's display name |
| Device name | Twingate-assigned device name |
| Device type | `mobile`, `desktop`, or `laptop` |
| Active state | `active`, `archived`, or `blocked` |
| Is manually trusted | Boolean — manual trust status |
| Client version | Twingate Client version string |
| Hostname | Device hostname |
| Local username | Owner's local OS username |
| Serial number | Device serial number |
| Device manufacturer | Hardware manufacturer |
| Device model | Hardware model |
| OS platform | `macOS`, `Windows`, `Linux`, `iOS`, or `Android` |
| OS version | OS version string |
| Last resource access time | Timestamp of last Resource access |

## Gotchas
- Large device counts may take several minutes to generate
- Download link only appears on the **Reports** page, not the Devices page — even if initiated from Devices
- No real-time progress indicator; must refresh page or wait for email

## Related Docs
- [Devices](https://www.twingate.com/docs/devices)
- [Reports](https://www.twingate.com/docs/reports)