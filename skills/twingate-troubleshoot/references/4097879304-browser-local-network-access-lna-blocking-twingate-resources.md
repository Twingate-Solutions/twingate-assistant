---
source: https://help.twingate.com/articles/4097879304-browser-local-network-access-lna-blocking-twingate-resources
type: help
fetched: 2026-11-08
source_version: 10a1cec624853f2618a4da52497fab2cf581e52aa45e11e579760571e8c0e71d
trust: official
---

# Browser Local Network Access (LNA) Blocking Twingate Resources

## Summary
Chrome 142+ and Firefox (Beta/Nightly/ETP Strict) include Local Network Access restrictions that treat Twingate Resources as local network endpoints, triggering permission prompts or blocks. If users deny these prompts, Twingate Resources become inaccessible in the browser. Admins must configure browser policies or instruct users to allow LNA access.

## Key Information
- Twingate routes traffic via CGNAT over loopback, causing browsers to classify Resources as local network
- Chrome: LNA enabled by default in 142+
- Firefox: LNA in Beta/Nightly by default; standard Firefox with ETP set to Strict
- Symptoms: Resources inaccessible, elevated CORS errors, blocked images, "Not secure" warnings

## Workaround (All Browsers)
Narrow Resource definitions to exclude public CDN endpoints (`*.amazonaws.com`, `*.microsoftonline.com`, `azureedge.net`, `*.azure.com`) unless explicitly required for private resolution.

## Chrome Configuration

### Unmanaged Users
- Click **Not Secure** in address bar → toggle **Local Network Access** to Allow
- Or: Site Settings → scroll to **Local network access** → set to **Allow**
- Advanced: `chrome://flags/#local-network-access-check` (use with caution)

### Enterprise – Google Workspace
1. Configure Managed Profiles (see [Manage user profiles on Chrome browser](https://support.google.com/chrome/a/answer/7532316))
2. In Google Admin Console → **Chrome Browser > Custom Configurations**
3. Select target OU, add JSON:
```json
{
  "LocalNetworkAccessAllowedForUrls": [
    "https://your-internal-domain.int"
  ]
}
```
4. Save, then verify via `chrome://policy` → **Reload policies**

### Enterprise – MDM
Deploy `LocalNetworkAccessAllowedForUrls` policy per platform:
- **Windows (Intune):** OMA-URI via Windows registry path
- **macOS:** `.mobileconfig` plist format
- **Android:** Managed app configuration

Reference: [Chrome Enterprise policy reference](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls)

### Disable LNA Entirely (Deprecated in Chrome 144)
- `LocalNetworkAccessRestrictionsEnabled`
- `LocalNetworkAccessRestrictionsTemporaryOptOut`

## Firefox Configuration

### Unmanaged Users
1. Click permissions icon (rightmost in address bar)
2. Under **Access local network devices**, click **X** next to Blocked
3. Refresh page → click **Allow** on prompt
4. Check **Remember my choice for this site** to persist

Manage saved permissions: **Settings → Privacy & Security → Permissions → Local network devices → Settings...**

### Advanced (`about:config`)
| Preference | Type | Default | Purpose |
|---|---|---|---|
| `network.lna.enabled` | boolean | `true` | Disable all LNA checks when set to `false` |
| `network.lna.blocking` | boolean | `true` | Allow access without prompts when set to `false` |
| `network.lna.skip-domains` | string | empty | Comma-separated domains/wildcards to skip LNA (e.g., `intranet.company.com,.devices.local`) |

### Enterprise
Use the `LocalNetworkAccess` policy via [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/).

## Gotchas
- Chrome LNA disable flags (`chrome://flags`) are **deprecated as of Chrome 144**
- Clicking **Block** on the prompt persists and blocks all future access until manually reset
- `about:config` changes in Firefox affect stability/security — not for general users
- Firefox ETP must be set to **Strict** to trigger LNA on standard releases

## Related Docs
- [Chrome Enterprise policy reference – LocalNetworkAccessAllowedForUrls](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls)
- [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/)
- [Manage Chrome user profiles](https://support.google.com/chrome/a