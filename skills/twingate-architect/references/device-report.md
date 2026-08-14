---
source: https://www.twingate.com/docs/device-report
type: docs
fetched: 2026-08-14
source_version: 11fe21e14f522641df17026edfd32b586d491011c05eacf1fd5b61cc5d87d0d6
---

# Device Report

## Summary
Twingate's device report exports detailed device inventory data to CSV from the Admin Console. The report includes device metadata, Client version, and owner information. Reports are generated asynchronously and downloaded from the Reports page.

## Key Information
- Export format: CSV file
- Two generation paths: Devices page or Settings → Reports page
- Filter options: Active, Archived, Blocked, or All Devices
- Generation is asynchronous; notification via email or manual page refresh
- Typical generation time: seconds; large datasets may take minutes

## Prerequisites
- Access to Twingate Admin Console
- Sufficient admin permissions to view Devices/Reports sections

## Step-by-Step

**Option 1 – From Devices page:**
1. Navigate to **Devices** tab
2. Click **Download** button above the device table

**Option 2 – From Reports page:**
1. Navigate to **Settings → Reports → Device List**
2. Click **Generate Device Report**

**Complete report generation:**
1. Select device filter: `Active`, `Archived`, `Blocked`, or `All Devices`
2. Click **Generate Report**
3. Wait for email notification or refresh the Reports page
4. Download completed report from **Reports** page

## Report Schema (CSV Columns)

| Column | Description |
|---|---|
| Device ID | Twingate device ID |
| Owner user ID | Twingate user ID of device owner |
| Owner name | Device owner's name |
| Device name | Twingate-assigned device name |
| Device type | `mobile`, `desktop`, or `laptop` |
| Active state | `active`, `archived`, or `blocked` |
| Is manually trusted | Boolean — manual trust status |
| Client version | Twingate Client version installed |
| Hostname | Device hostname |
| Local username | Owner's local OS username |
| Serial number | Device serial number |
| Device manufacturer | Hardware manufacturer |
| Device model | Hardware model |
| OS platform | `macOS`, `Windows`, `Linux`, `iOS`, or `Android` |
| OS version | Operating system version |
| Last resource access time | Timestamp of last Resource access |

## Gotchas
- Report download is only available from the **Reports** page, not the Devices page (even if generated from there)
- No real-time generation — must wait for background processing before downloading
- No API or CLI method documented; Admin Console UI only

## Related Docs
- Devices documentation
- Reports page (Settings → Reports)