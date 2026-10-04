---
source: https://help.twingate.com/articles/1933606039-disabling-browser-doh
type: help
fetched: 2026-10-04
source_version: 8a7f8fb1ca531d77a28dd706e31ab9343ed79f09638693644a22662ac18ec22c
trust: official
---

# Disabling Browser DoH for Twingate

## Page Title
Disabling Browser DNS-over-HTTPS (DoH)

## Summary
Browsers with DNS-over-HTTPS (DoH) enabled bypass Twingate's DNS proxy, preventing access to private DNS Resources. DoH must be disabled in each browser so Twingate can intercept DNS lookups for protected resources. MDM solutions can push these settings centrally across managed devices.

## Key Information
- Affected browsers: Google Chrome (v83+), Microsoft Edge, Mozilla Firefox
- DoH encrypts DNS requests, bypassing Twingate's DNS proxy entirely
- Private DNS Resources will be inaccessible when DoH is active on the client browser
- MDM deployment recommended for enterprise-wide enforcement

## Prerequisites
- Twingate Client installed and running
- Admin access to browser settings (or MDM policy management for fleet deployment)

## Step-by-Step

### Google Chrome (v83+)
1. Menu → **Settings**
2. **Privacy and security** → **Security**
3. Scroll to **Use Secure DNS** → uncheck
4. Restart browser

### Microsoft Edge
1. Menu → **Settings**
2. Search: `Secure DNS`
3. Uncheck **Use secure DNS to specify how to lookup the network address for websites**
4. Restart browser

### Mozilla Firefox (v116+)
1. Menu → **Settings**
2. Search: `Secure DNS`
3. Under **Enable secure DNS using** → select **Off**

### Mozilla Firefox (pre-v116)
1. Menu → **Settings**
2. Scroll to **Network Settings** → click **Settings**
3. Uncheck **Enable DNS over HTTPS**
4. Click **OK**

## Configuration Values
- No CLI flags or API parameters — browser UI settings only
- For MDM/GPO deployment, reference each browser vendor's policy documentation for the corresponding policy key (e.g., Chrome: `DnsOverHttpsMode`, Firefox: `DNSOverHTTPS`)

## Gotchas
- Chrome enables DoH by default starting at **version 83** — older deployments may not be affected
- Firefox enables DoH by default; the settings UI changed significantly at **version 116**
- Disabling at the OS/network level alone is insufficient if browsers have DoH independently configured
- Without disabling DoH, symptom is silent: private Resources simply fail to resolve with no clear error indicating DoH is the cause

## Related Docs
- Twingate Client documentation
- Twingate DNS Resource configuration
- Browser vendor MDM/GPO policy references for fleet-wide enforcement