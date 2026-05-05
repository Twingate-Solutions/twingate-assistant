## Device Report

CSV export of all devices registered in a Twingate account. Useful for auditing device inventory, trust status, client versions, and ownership in bulk.

**Step-by-Step:**
1. (Option A) Devices tab → Download button above the device table
2. (Option B) Settings → Reports → Device List → Generate Device Report
3. Select device scope: Active, Archived, Blocked, or All Devices
4. Click Generate Report; export runs in background; email notification sent when ready
5. Download from the Reports page

**Device Report CSV Schema:**
- `Device ID` -- Twingate device ID
- `Owner user ID` -- device owner's Twingate user ID
- `Owner name` -- device owner's display name
- `Device name` -- Twingate device name
- `Device type` -- mobile, desktop, or laptop
- `Active state` -- active, archived, or blocked
- `Is manually trusted` -- whether the device is manually trusted
- `Client version` -- installed Twingate Client version
- `Hostname` -- device hostname
- `Local username` -- owner's local OS username
- `Serial number` -- device serial number
- `Device manufacturer` -- hardware manufacturer
- `Device model` -- hardware model
- `OS platform` -- macOS, Windows, Linux, iOS, or Android
- `OS version` -- OS version string
- `Last resource access time` -- last time device accessed a Resource

**Related Docs:**
- /docs/analytics -- Analytics and reporting overview
- /docs/user-activity -- User activity report
