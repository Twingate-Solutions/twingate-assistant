---
source: https://help.twingate.com/articles/4097879304-browser-local-network-access-lna-blocking-twingate-resources
type: help
fetched: 2026-10-04
source_version: ded64aa92f10038b682b01e8b7f566255e28714160c836fb0aaab3ac6f87f919
trust: official
---

# Browser Local Network Access (LNA) Blocking Twingate Resources

## Summary
Chrome 142+ and Firefox (Beta/Nightly/Strict ETP) apply Local Network Access restrictions that block Twingate Resources in the browser. Twingate routes traffic via CGNAT over loopback, causing browsers to treat Resources as local network addresses and trigger permission prompts or blocks. Denying these prompts breaks Resource access.

## Affected Platforms
- Chrome/Chromium 142+ (LNA enabled by default)
- Firefox Beta, Nightly, and standard releases with ETP set to Strict
- OS: Mac, Windows, Linux

## Symptoms
- Resources inaccessible after clicking "Block" on permission prompt
- Elevated CORS errors
- Blocked images
- Chrome: Resources show "Not Secure"

## Workarounds

### Admin-Side: Narrow Resource Scope
Exclude public CDN endpoints from Resource definitions if not explicitly required:
- `*.amazonaws.com`
- `*.microsoftonline.com`, `azureedge.net`, `*.azure.com`

---

## Chrome Fixes

### End User (Unmanaged)
1. Click **Not Secure** in address bar
2. Toggle **Local Network Access** → **Allow**  
   OR: **Site settings** → **Local network access** → **Allow**

### Advanced (chrome://flags)
- Flag: `chrome://flags/#local-network-access-check` — set to Disabled  
- ⚠️ Advanced users only; affects stability/security

### Enterprise: Google Workspace
Policy: `LocalNetworkAccessAllowedForUrls`

```json
{
  "LocalNetworkAccessAllowedForUrls": [
    "https://your-internal-domain.int"
  ]
}
```
**Path:** Admin Console → Chrome Browser → Custom Configurations → select OU → add JSON → Save  
**Verify:** `chrome://policy` → Reload policies

### Enterprise: MDM
Deploy `LocalNetworkAccessAllowedForUrls` via:
- **Windows (Intune):** OMA-URI / Windows registry
- **macOS:** `.mobileconfig` plist
- **Android:** Managed app configuration

See [Chrome Enterprise policy reference](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls) for format details.

### Disable LNA Entirely (deprecated as of Chrome 144)
- `LocalNetworkAccessRestrictionsEnabled`
- `LocalNetworkAccessRestrictionsTemporaryOptOut`

---

## Firefox Fixes

### End User (Unmanaged)
1. Click permissions icon (rightmost icon before address bar)
2. Find **Access local network devices** → click **X** next to **Blocked**
3. Refresh page → click **Allow** on prompt
4. Optionally check **Remember my choice for this site**

**To manage saved permissions:** Settings → Privacy & Security → Permissions → **Device apps and services** / **Local network devices** → Settings

### Advanced (about:config)
⚠️ Experienced users only.

| Preference | Type | Default | Action |
|---|---|---|---|
| `network.lna.enabled` | boolean | `true` | Set `false` to disable all LNA |
| `network.lna.blocking` | boolean | `true` | Set `false` to allow without prompts |
| `network.lna.skip-domains` | string | empty | Comma-separated domains/wildcards, e.g. `intranet.company.com,.devices.local` |

### Enterprise
Use the `LocalNetworkAccess` Firefox Enterprise Policy. See [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/).

---

## Gotchas
- Clicking **Block** once may persist; users must manually reset permissions
- Chrome LNA disable flags deprecated after v144
- Firefox LNA rollout is progressive; Strict ETP users affected before general release

## Related Docs
- [Chrome Enterprise Policy Reference](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls)
- [Manage Chrome user profiles](https://support.google.com/chrome/a/answer/7349337)
- [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/)