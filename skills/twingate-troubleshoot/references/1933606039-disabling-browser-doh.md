---
source: https://help.twingate.com/articles/1933606039-disabling-browser-doh
type: help
fetched: 2026-11-01
source_version: 0cd3e2b6a93e320925a5819dba43b0c4dac80f7c3d24c4d509e747a71cc394a8
trust: official
---

# Disabling Browser DoH for Twingate

## Page Title
Disabling Browser DNS-over-HTTPS (DoH)

## Summary
Browsers increasingly enable DoH by default, encrypting DNS requests in a way that bypasses Twingate's DNS proxy. This prevents private DNS Resources from being accessible through the Twingate Client. DoH must be disabled per-browser to restore Twingate DNS interception.

## Key Information
- **Affected browsers**: Google Chrome (v83+), Microsoft Edge, Mozilla Firefox
- **Root cause**: DoH encrypts DNS lookups, bypassing Twingate's local DNS proxy
- **Symptom**: Private DNS Resources become inaccessible to users
- **MDM note**: These settings can typically be pushed centrally via MDM solutions — preferred for org-wide rollout

## Prerequisites
- Twingate Client installed and running
- Admin or user access to browser settings (or MDM for fleet management)

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
2. Search `Secure DNS` in top-right search bar
3. Under **Enable secure DNS using** → select **Off**

### Mozilla Firefox (pre-v116)
1. Menu → **Settings**
2. Scroll to **Network Settings** → click **Settings**
3. Uncheck **Enable DNS over HTTPS**
4. Click **OK**

## Configuration Values
- No CLI flags or env vars; settings are UI-only per browser
- For MDM/GPO deployment, reference browser vendor policy docs for the equivalent policy keys (e.g., Chrome's `DnsOverHttpsMode` policy)

## Gotchas
- Chrome v83+ enables DoH **by default** — must be explicitly disabled
- Firefox also enables DoH by default; UI path differs between v116+ and earlier versions
- Edge does not enable DoH by default but can have it enabled by users or policy
- Disabling DoH is per-browser; each browser used on the device must be configured individually unless MDM is used

## Related Docs
- Twingate Client documentation
- Twingate DNS Resource configuration
- Browser vendor MDM/GPO policy references for fleet-wide DoH disablement