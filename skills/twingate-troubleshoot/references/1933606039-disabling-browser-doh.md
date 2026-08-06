---
source: https://help.twingate.com/articles/1933606039-disabling-browser-doh
type: help
fetched: 2026-08-06
source_version: ddeece8a9199f93478997336b050e97ea54b66b3904f11cbf970dde22189b72f
---

# Disabling Browser DNS-over-HTTPS (DoH)

## Page Title
Disabling Browser DOH

## Summary
Browsers with DNS-over-HTTPS (DoH) enabled bypass Twingate's DNS proxy, preventing access to private DNS Resources. DoH must be disabled in each browser to allow Twingate's Client to intercept DNS lookups correctly.

## Key Information
- **Affected component**: Twingate Client / Resources
- **Affected browsers**: Google Chrome (v83+), Microsoft Edge, Mozilla Firefox
- **Root cause**: DoH encrypts DNS requests, bypassing Twingate's local DNS proxy
- **MDM note**: Settings can be centrally deployed via MDM solutions

## Prerequisites
- Administrative or user access to browser settings
- (Optional) MDM solution for fleet-wide deployment

## Step-by-Step

### Google Chrome (v83+)
1. Menu → **Settings**
2. **Privacy and security** → **Security**
3. Uncheck **Use Secure DNS**
4. Restart browser

### Microsoft Edge
1. Menu → **Settings**
2. Search for `Secure DNS`
3. Uncheck **Use secure DNS to specify how to lookup the network address for websites**
4. Restart browser

### Mozilla Firefox (v116+)
1. Menu → **Settings**
2. Search `Secure DNS`
3. Set **Enable secure DNS using** to **Off**

### Mozilla Firefox (pre-v116)
1. Menu → **Settings**
2. Scroll to **Network Settings** → click **Settings**
3. Uncheck **Enable DNS over HTTPS**
4. Click **OK**

## Configuration Values
| Browser | Setting Name |
|---------|-------------|
| Chrome | Use Secure DNS |
| Edge | Use secure DNS |
| Firefox | Enable secure DNS using |

## Gotchas
- Chrome enables DoH by default starting with **version 83**
- Firefox enables DoH by default (version unspecified as initial rollout)
- DoH bypass is silent — users won't get an error message indicating why private resources are unreachable
- Fix must be applied per-browser; disabling in one browser does not affect others

## Related Docs
- Twingate Client documentation
- Twingate DNS Resources configuration
- MDM policy deployment guides (vendor-specific)