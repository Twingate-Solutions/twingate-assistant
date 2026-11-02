---
source: https://help.twingate.com/articles/4097879304-browser-local-network-access-lna-blocking-twingate-resources
type: help
fetched: 2026-11-01
source_version: d78c9671c67395f3a50f90bd32ff5f411a78c6a9d556016165fb4d1ff16b6222
trust: official
---

# Browser Local Network Access (LNA) Blocking Twingate Resources

## Summary
Chrome 142+ and Firefox (Beta/Nightly/ETP Strict) include Local Network Access restrictions that block Twingate Resources in the browser. Twingate routes traffic via CGNAT over loopback, causing browsers to treat Resources as local network endpoints and trigger LNA permission prompts or blocks.

## Key Information
- **Chrome**: LNA enabled by default in Chrome/Chromium 142+
- **Firefox**: LNA in Beta/Nightly by default; standard Firefox users with ETP set to Strict are progressively affected
- Symptoms: resource inaccessibility, elevated CORS errors, blocked images, "Not Secure" warnings
- Root cause: Twingate's CGNAT/loopback routing causes browsers to classify Resources as local

## Workaround (All Browsers)
Narrow Resource definitions to exclude public CDN endpoints not explicitly needed privately:
- `*.amazonaws.com`
- `*.microsoftonline.com`, `azureedge.net`, `*.azure.com`

---

## Chrome Fixes

### Unmanaged (End User Self-Service)
1. Click **Not Secure** in the address bar
2. Toggle **Local Network Access** to Allow, OR navigate to **Site Settings > Local Network Access > Allow**

### Advanced (chrome://flags)
- Flag: `chrome://flags/#local-network-access-check` — set to Disabled
- ⚠️ Warning: affects browser stability/security

### Enterprise — Google Workspace
1. Set up Managed Profiles ([docs](https://support.google.com/chrome/a/answer/7349337))
2. In Google Admin Console: **Chrome Browser > Custom Configurations**
3. Select target OU, add JSON:
```json
{
  "LocalNetworkAccessAllowedForUrls": [
    "https://your-internal-domain.int"
  ]
}
```
4. Save and verify at `chrome://policy` → **Reload policies**

### Enterprise — MDM
Deploy `LocalNetworkAccessAllowedForUrls` policy per platform:
- **Windows (Intune)**: OMA-URI using Windows registry path from [Chrome Enterprise policy reference](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls)
- **macOS**: `.mobileconfig` plist format
- **Android**: Managed app configuration

### Disable LNA Entirely (Deprecated as of Chrome 144)
- `LocalNetworkAccessRestrictionsEnabled`
- `LocalNetworkAccessRestrictionsTemporaryOptOut`

---

## Firefox Fixes

### Unmanaged (End User Self-Service)
1. Click the permissions icon in the address bar (rightmost icon)
2. Find **Access local network devices** → click **X** next to Blocked
3. Refresh the page → click **Allow** when prompted
4. Optionally check **Remember my choice for this site**

To manage saved permissions: **Settings > Privacy & Security > Permissions > Device apps and services / Local network devices**

### Advanced (about:config)
Navigate to `about:config` and modify:

| Preference | Type | Default | Effect |
|---|---|---|---|
| `network.lna.enabled` | boolean | `true` | Set `false` to disable all LNA restrictions |
| `network.lna.blocking` | boolean | `true` | Set `false` to allow without prompts |
| `network.lna.skip-domains` | string | empty | Comma-separated domains/wildcards to exempt (e.g., `intranet.company.com,.devices.local`) |

### Enterprise
Use the Firefox `LocalNetworkAccess` policy — see [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/).

---

## Gotchas
- Clicking **Block** on the LNA prompt causes persistent loss of browser access to Twingate Resources until manually reversed
- Chrome LNA disable flags are deprecated as of v144 — enterprise policy is the preferred long-term solution
- `about:config` and `chrome://flags` changes affect stability and security

## Related Docs
- [Chrome Enterprise Policy Reference — LocalNetworkAccessAllowedForUrls](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls)
- [