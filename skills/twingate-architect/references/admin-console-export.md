# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows administrators to export audit logs from the Admin Console Reports page. Exports are generated asynchronously in GZIP-compressed JSON format, with each line representing a single admin action event.

## Key Information
- Exports available under **Settings → Reports**
- Time range selector uses local timezone display, but exported timestamps are in **UTC**
- Export runs in background; completion notification sent via **email**
- Most exports complete in minutes; large exports may take **a few hours**
- Output format: **GZIP-compressed JSON** (one event per line)

## Prerequisites
- Admin Console access
- Access to Settings → Reports page
- Email access to receive completion notification

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click **Generate Audit Logs Report**
3. Select **time range** and **category**
4. Wait for email notification (background processing)
5. Return to **Reports page** to download completed report

## Export File Format

Each JSON line contains:
- `when` — event timestamp (UTC)
- `actor` — who performed the action
- `action` — what action occurred
- `final state` — resulting state (includes before-state if applicable)

Full JSON schema available in Twingate docs (linked from source page).

## Configuration Values
- None (UI-only operation, no CLI flags or API parameters documented on this page)

## Gotchas
- **Safari users**: Safari's auto-unpack feature may cause the file to appear empty. Fix: Go to **Safari → Preferences → General** and **uncheck** "Open 'safe' files after downloading" before downloading
- Time range display is in **local timezone**, but exported data uses **UTC** — don't confuse the two when filtering
- Large exports can take **hours**, not minutes — plan accordingly for large time ranges

## Related Docs
- [Twingate Audit Log JSON Schema](https://www.twingate.com/docs/) *(linked from source page)*
- Twingate Reports/Settings documentation