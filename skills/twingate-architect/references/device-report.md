# Device Report

## Summary
Twingate's device report exports detailed device inventory data to CSV from the Admin Console. It includes device metadata, Client version, and owner information. Reports can be filtered by device state and are generated asynchronously.

## Key Information
- Export format: CSV file
- Two entry points: Devices page or Reports page
- Filter options: Active, Archived, Blocked, or All Devices
- Generation is asynchronous; notification via email or page refresh
- Large exports may take a few minutes

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

**Complete report generation:**
1. Select device filter: `Active`, `Archived`, `Blocked`, or `All Devices`
2. Click **Generate Report**
3. Wait for email notification or refresh the Reports page
4. Download completed report from the **Reports** page

## Report Schema (CSV Columns)

| Column | Description |
|--------|-------------|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of owner |
| Owner name | Device owner's name |
| Device name | Twingate device name |
| Device type | `mobile`, `desktop`, or `laptop` |
| Active state | `active`, `archived`, or `blocked` |
| Is manually trusted | Boolean: manual trust status |
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
- Report generates in background — not immediately available after clicking
- Download link only appears on the **Reports** page, regardless of which method initiated generation
- Large device counts can extend generation time to several minutes

## Related Docs
- [Devices](https://www.twingate.com/docs/devices)
- [Reports](https://www.twingate.com/docs/reports)