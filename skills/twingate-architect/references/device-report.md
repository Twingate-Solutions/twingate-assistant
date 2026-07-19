# Device Report

## Summary
Twingate Admin Console allows exporting device inventory data as a CSV file. Reports can be filtered by device state and include hardware, software, and ownership details. Generation happens asynchronously with email notification on completion.

## Key Information
- Export format: CSV file
- Two entry points: Devices page or Settings → Reports page
- Filter options: Active, Archived, Blocked, or All Devices
- Generation is asynchronous; email sent when ready
- Download completed reports from the Reports page

## Prerequisites
- Access to Twingate Admin Console
- Appropriate admin permissions

## Step-by-Step

### Option 1: From Devices Page
1. Navigate to **Devices** tab in Admin Console
2. Click **Download** button above device table
3. Select device filter (Active/Archived/Blocked/All Devices)
4. Click **Generate Report**
5. Wait for email notification or refresh page
6. Download from **Settings → Reports**

### Option 2: From Reports Page
1. Navigate to **Settings → Reports → Device List**
2. Click **Generate Device Report**
3. Select device filter (Active/Archived/Blocked/All Devices)
4. Click **Generate Report**
5. Wait for email notification or refresh page
6. Download from the same Reports page

## Report Schema (CSV Columns)

| Column | Description |
|--------|-------------|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of owner |
| Owner name | Device owner's name |
| Device name | Twingate-assigned device name |
| Device type | `mobile`, `desktop`, or `laptop` |
| Active state | `active`, `archived`, or `blocked` |
| Is manually trusted | Boolean: manually trusted status |
| Client version | Twingate Client version |
| Hostname | Device hostname |
| Local username | Owner's local system username |
| Serial number | Device serial number |
| Device manufacturer | Hardware manufacturer |
| Device model | Hardware model |
| OS platform | `macOS`, `Windows`, `Linux`, `iOS`, or `Android` |
| OS version | Operating system version |
| Last resource access time | Timestamp of last Resource access |

## Gotchas
- Large device inventories may take **several minutes** to generate (not just seconds)
- Report is not instantly available — must be downloaded from Reports page after generation, not immediately after clicking Generate
- No direct download from Devices page; final download always from **Settings → Reports**

## Related Docs
- Devices documentation
- Twingate Admin Console Settings