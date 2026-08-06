---
source: https://help.twingate.com/articles/4898142252-how-to-download-a-list-of-app-store-macos-clients-from-your-twingate-tenant
type: help
fetched: 2026-08-06
source_version: 55e60703ece4801701b39a0cc1fc7b6e5746cfce0db89fe70e00a2bafda97873
---

# How to Download a List of App Store macOS Clients from Your Twingate Tenant

## Summary
Generates a device report from the Twingate Admin Console and filters it to identify macOS clients installed via the App Store (as opposed to standalone clients). The distinction is made by examining the client version string suffix in the exported CSV.

## Key Information
- App Store clients do **not** have `+sa` suffix in version string
- Standalone clients have versions ending in `+sa`
- Report is delivered via email when ready, then downloaded from Admin Console

## Prerequisites
- Access to Twingate Admin Console with sufficient permissions to view Devices and Reports
- Spreadsheet tool (Excel, Google Sheets, or equivalent)

## Step-by-Step

1. **Generate Device Report**
   - Navigate to Admin Console → **Devices** tab → **Devices** page
   - Click **Download** at top of device table
   - Select Report Type: **Active**
   - Click **Generate Report**
   - Wait for email notification that report is ready

2. **Download Report**
   - Go to Admin Console → **Settings** → **Reports**
   - Download the generated report

3. **Prepare File**
   - Unzip the downloaded archive
   - Open CSV in spreadsheet tool
   - Add `.csv` extension manually if missing

4. **Filter for App Store Clients**
   - Filter **OS platform** column → `macOS` only
   - Filter **Client version** column → exclude values ending with `+sa`
   - Remaining rows = App Store macOS clients only

## Configuration Values

| Field | Value | Notes |
|-------|-------|-------|
| Report Type | `Active` | Selected during generation |
| OS Filter | `macOS` | Platform column |
| Version Suffix | `+sa` | Indicates standalone; exclude these |

## Gotchas
- Report is **not** instant — requires waiting for email before it's available to download
- File may lack `.csv` extension after unzip; add it manually before opening
- Filtering logic is **exclusion-based**: remove `+sa` versions rather than selecting a specific App Store identifier

## Related Docs
- Twingate Devices page (Admin Console)
- Twingate Reports section (Admin Console → Settings)