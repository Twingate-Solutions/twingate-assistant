---
source: https://help.twingate.com/articles/4097879304-browser-local-network-access-lna-blocking-twingate-resources
type: help
fetched: 2026-08-30
source_version: 461ba2407490c30416889a76c5262684b274390df0a9560ffbf163e2414866c0
---

# Browser Local Network Access (LNA) Blocking Twingate Resources

## Summary
Chrome 142+ and Firefox (Beta/Nightly/ETP Strict) implement Local Network Access restrictions that block Twingate Resources because Twingate routes traffic via CGNAT over loopback, causing browsers to treat Resources as local network addresses. Users who deny LNA permission prompts lose browser access to Twingate Resources.

## Key Information
- Chrome: LNA enabled by default in Chrome/Chromium 142+
- Firefox: LNA in Beta/Nightly by default; standard Firefox with ETP set to Strict
- Symptoms: CORS errors, blocked images, "Not secure" warnings, inaccessible Resources
- Chrome `LocalNetworkAccessRestrictionsEnabled` / `TemporaryOptOut` policies deprecated as of Chrome v144

## Prerequisites
- Enterprise Chrome: Google Workspace with managed profiles OR MDM (Intune, macOS MDM)
- Enterprise Firefox: Firefox Enterprise Policy deployment capability

## Workarounds

### Quick Fix (All Users)
Narrow Twingate Resource definitions to exclude public CDN endpoints not needed privately:
- `*.amazonaws.com`, `*.microsoftonline.com`, `azureedge.net`, `*.azure.com`

### Chrome — Unmanaged Users
1. Click **Not Secure** in address bar → toggle **Local Network Access** to Allow
2. Or: Site Settings → scroll to **Local network access** → select **Allow**
3. Advanced: `chrome://flags/#local-network-access-check` (disable flag)

### Chrome — Enterprise (Google Workspace)
1. Configure managed profiles (see Google docs)
2. Admin Console → **Chrome Browser > Custom Configurations** → select OU
3. Add JSON:
```json
{
  "LocalNetworkAccessAllowedForUrls": [
    "https://your-internal-domain.int"
  ]
}
```
4. Verify via `chrome://policy` → **Reload policies**

### Chrome — Enterprise (MDM)
Deploy `LocalNetworkAccessAllowedForUrls` policy:
- **Windows/Intune**: OMA-URI via Windows registry path (see Chrome Enterprise policy reference)
- **macOS**: `.mobileconfig` plist format
- **Android**: Managed app configuration

### Firefox — Unmanaged Users
1. Click permissions icon (right of address bar) → find **Access local network devices** → remove block → refresh
2. Click **Allow** on prompt; optionally check **Remember my choice**
3. Manage saved permissions: Settings → Privacy & Security → Permissions → **Local network devices**

### Firefox — Advanced (`about:config`)

| Preference | Type | Default | Action |
|---|---|---|---|
| `network.lna.enabled` | boolean | `true` | Set `false` to disable all LNA |
| `network.lna.blocking` | boolean | `true` | Set `false` to allow without prompts |
| `network.lna.skip-domains` | string | empty | Comma-separated domains/wildcards to skip (e.g., `.company.com`) |

### Firefox — Enterprise
Use the `LocalNetworkAccess` Firefox Enterprise Policy (see Firefox Enterprise Policy Documentation).

## Configuration Values
- Chrome policy: `LocalNetworkAccessAllowedForUrls`
- Chrome legacy (deprecated v144+): `LocalNetworkAccessRestrictionsEnabled`, `LocalNetworkAccessRestrictionsTemporaryOptOut`
- Firefox flag: `network.lna.enabled`, `network.lna.blocking`, `network.lna.skip-domains`

## Gotchas
- Chrome disable/opt-out policies deprecated in Chrome v144 — `LocalNetworkAccessAllowedForUrls` is the preferred path
- Users clicking **Block** on prompts lose access; must be manually remediated per-site
- `chrome://flags` changes affect stability/security — not recommended for general users

## Related Docs
- [Chrome Enterprise Policy Reference](https://chromeenterprise.google/policies/)
- [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/)
- Twingate: CGNAT routing behavior