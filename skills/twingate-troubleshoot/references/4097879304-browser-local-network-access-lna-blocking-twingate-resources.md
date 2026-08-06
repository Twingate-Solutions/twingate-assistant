---
source: https://help.twingate.com/articles/4097879304-browser-local-network-access-lna-blocking-twingate-resources
type: help
fetched: 2026-08-06
source_version: 4825422965cc9e1c4baf50a6701420f7faf9226255dacc1393f7572c46eab8cf
---

# Browser Local Network Access (LNA) Blocking Twingate Resources

## Summary
Chrome 142+ and Firefox (Beta/Nightly/Strict ETP) implement Local Network Access restrictions that treat Twingate Resources as local network traffic due to CGNAT/loopback routing. Users who deny LNA permission prompts lose browser access to Twingate Resources. Admins can pre-approve URLs via enterprise policy to prevent disruption.

## Key Information
- Twingate routes traffic via CGNAT over loopback → browsers classify Resources as "local network"
- Chrome LNA enabled by default in v142+; opt-out deprecation flag removed in v144
- Firefox: affects Beta, Nightly, and standard users with ETP set to Strict
- Symptoms: blocked Resources, elevated CORS errors, blocked images, "Not Secure" warnings

## Affected Platforms
- Chrome/Chromium 142+ (Mac, Windows, Linux)
- Firefox Beta, Nightly, and standard with Strict ETP

## Workaround (All Platforms)
Narrow Resource definitions to exclude public CDN endpoints not needed internally:
- `*.amazonaws.com`
- `*.microsoftonline.com`, `azureedge.net`, `*.azure.com`

## Chrome Solutions

### Unmanaged Users (Self-Service)
1. Click **Not Secure** in address bar
2. Toggle **Local Network Access** to Allow, OR go to **Site Settings → Local network access → Allow**

### Enterprise: Google Workspace
1. Configure managed profiles (see [Manage user profiles on Chrome browser](https://support.google.com/chrome/a/answer/7349337))
2. In Admin Console: **Chrome Browser → Custom Configurations**
3. Apply JSON policy to target OU:
```json
{
  "LocalNetworkAccessAllowedForUrls": [
    "https://your-internal-domain.int"
  ]
}
```
4. Verify via `chrome://policy` → **Reload policies**

### Enterprise: MDM Deployment
Deploy `LocalNetworkAccessAllowedForUrls` policy:
- **Windows (Intune):** OMA-URI via Windows registry path
- **macOS:** `.mobileconfig` plist format
- **Android:** Managed app configuration

### Disable LNA Entirely (Deprecated in v144)
- `LocalNetworkAccessRestrictionsEnabled`
- `LocalNetworkAccessRestrictionsTemporaryOptOut`

## Firefox Solutions

### Unmanaged Users (Self-Service)
1. Click permissions icon (far right of address bar)
2. Click **X** next to **Blocked** under "Access local network devices"
3. Refresh page → click **Allow** on prompt
4. Check **Remember my choice for this site** to persist

### Advanced: `about:config` Flags
| Preference | Default | Effect |
|---|---|---|
| `network.lna.enabled` | `true` | Set `false` to disable all LNA checks |
| `network.lna.blocking` | `true` | Set `false` to allow without prompts |
| `network.lna.skip-domains` | empty | Comma-separated domains to bypass LNA; supports `*` prefix wildcards |

### Enterprise: Firefox Policy
Use the `LocalNetworkAccess` policy — see [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/)

## Gotchas
- Users clicking **Block** on the initial prompt lose Resource access — proactive enterprise policy deployment is preferred
- Chrome opt-out flags (`chrome://flags/#local-network-access-check`) deprecated as of v144
- `about:config` changes are per-device and not manageable at scale without enterprise policy
- Firefox ETP Strict setting triggers LNA even on standard release builds

## Related Docs
- [Chrome Enterprise policy reference – LocalNetworkAccessAllowedForUrls](https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls)
- [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/)
- [Chrome Browser quick start (Mac)](https://support.google.com/chrome/a/answer/7650050)