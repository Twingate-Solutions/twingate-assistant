---
source: https://help.twingate.com/articles/1933606039-disabling-browser-doh
type: help
fetched: 2026-09-06
source_version: d72e1cf9e928f74ea7c0b6585b4ee784dde469d4086373702762bee39dd0e319
---

# Disabling Browser DoH

## Page Title
Disabling Browser DNS-over-HTTPS (DoH)

## Summary
Browsers increasingly enable DNS-over-HTTPS by default, which encrypts DNS requests and bypasses Twingate's DNS proxy. This prevents users from accessing private DNS Resources protected by Twingate. DoH must be disabled in each browser to restore Twingate DNS interception.

## Key Information
- Affected browsers: Google Chrome (v83+), Microsoft Edge, Mozilla Firefox
- Twingate uses a DNS proxy to intercept traffic for private DNS Resources
- DoH encrypts DNS requests, preventing Twingate from resolving private resources
- MDM solutions can push these settings centrally to all managed devices

## Prerequisites
- Admin/MDM access recommended for fleet-wide deployment
- Per-user browser access for individual configuration

## Step-by-Step

### Google Chrome (v83+)
1. Menu → **Settings**
2. **Privacy and security** → **Security**
3. Scroll to **Use Secure DNS** → uncheck
4. Restart browser

### Microsoft Edge
1. Menu → **Settings**
2. Search `Secure DNS`
3. Uncheck **Use secure DNS to specify how to lookup the network address for websites**
4. Restart browser

### Mozilla Firefox (v116+)
1. Menu → **Settings**
2. Search `Secure DNS`
3. Set **Enable secure DNS using** → **Off**

### Mozilla Firefox (pre-v116)
1. Menu → **Settings**
2. Scroll to **Network Settings** → click **Settings**
3. Uncheck **Enable DNS over HTTPS**
4. Click **OK**

## Configuration Values
- No env vars or API params; all settings are browser UI toggles
- MDM-deployable via browser policy management (organization-specific)

## Gotchas
- Chrome enables DoH by default starting at **version 83** — older installs may not be affected
- Firefox changed the settings UI location at **version 116**; use the correct steps for your version
- Failure to disable DoH results in private DNS Resources being **silently inaccessible**, not just slow
- Browser updates may re-enable DoH; MDM enforcement is strongly recommended over manual configuration

## Related Docs
- Twingate Client documentation
- Twingate DNS Resources configuration
- MDM integration guides (organization-specific)