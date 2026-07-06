# Device Report

## Summary
Twingate Admin Console allows exporting device inventory as a CSV file. The report includes device metadata, Client version, and owner information. Reports are generated asynchronously and downloaded from the Reports page.

## Key Information
- Export format: CSV file
- Two entry points: Devices page or Settings → Reports page
- Filter options: Active, Archived, Blocked, or All Devices
- Generation is async; notification sent via email when ready
- Most exports complete in seconds; large datasets may take minutes

## Prerequisites
- Admin Console access
- Sufficient permissions to view Devices/Reports sections

## Step-by-Step

**Option 1 – From Devices page:**
1. Navigate to **Devices** tab in Admin Console
2. Click **Download** button above device table

**Option 2 – From Reports page:**
1. Navigate to **Settings → Reports → Device List**
2. Click **Generate Device Report**

**Complete report generation:**
1. Select device filter: `Active`, `Archived`, `Blocked`, or `All Devices`
2. Click **Generate Report**
3. Wait for email notification or refresh the Reports page
4. Download completed report from the **Reports** page

## Configuration Values
| Filter Option | Description |
|---|---|
| `Active` | Currently active devices only |
| `Archived` | Archived devices only |
| `Blocked` | Blocked devices only |
| `All Devices` | All devices regardless of state |

## Report Schema (CSV Columns)
| Column | Description |
|---|---|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of owner |
| Owner name | Owner's display name |
| Device name | Twingate device name |
| Device type | `mobile`, `desktop`, or `laptop` |
| Active state | `active`, `archived`, or `blocked` |
| Is manually trusted | Boolean: manual trust status |
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
- Report is **not** generated in real-time; must be downloaded from Reports page after generation completes
- No API or CLI method documented for report generation—Admin Console UI only
- Download link appears on Reports page, not at the original generation entry point

## Related Docs
- Devices documentation
- Reports page (Settings → Reports)