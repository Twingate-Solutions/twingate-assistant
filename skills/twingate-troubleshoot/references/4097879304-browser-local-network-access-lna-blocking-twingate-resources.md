---
source: https://help.twingate.com/articles/4097879304-browser-local-network-access-lna-blocking-twingate-resources
type: help
fetched: 2026-09-06
source_version: fa378902f775cc25c584e8c50886fcf6d9f237193f18f494d730120855e054a7
---

# Browser Local Network Access (LNA) Blocking Twingate Resources

## Summary
Chrome 142+ and Firefox (Beta/Nightly/Strict ETP) implement Local Network Access restrictions that block Twingate Resources because CGNAT routing over loopback causes resources to appear as local network endpoints. Users who deny LNA permission prompts lose browser access to Twingate Resources.

## Key Information
- Chrome LNA enabled by default starting v142; disable/opt-out policies deprecated in v144
- Firefox LNA active in Beta/Nightly and standard releases with ETP set to Strict
- Symptoms: CORS errors, blocked images, "Not Secure" warnings, inaccessible Resources
- Root cause: Twingate routes via CGNAT over loopback → browser treats destinations as local

## Prerequisites
- Chrome 142+ or Firefox Beta/Nightly/Strict ETP users affected
- Enterprise fixes require Google Workspace managed profiles or MDM enrollment
- For Chrome enterprise policy: confirm managed profile setup via `chrome://policy`

## Workarounds & Solutions

### Quick Mitigation (All Admins)
- Narrow Resource definitions to exclude public CDN endpoints not requiring private resolution:
  - `*.amazonaws.com`, `*.microsoftonline.com`, `azureedge.net`, `*.azure.com`

### Chrome — End User Self-Service
1. Click **Not Secure** in address bar
2. Toggle **Local Network Access** → Allow  
   OR: Site settings → Local network access → Allow

### Chrome — Enterprise (Google Workspace)
1. Configure managed profiles (see Workspace docs)
2. Admin Console → **Chrome Browser > Custom Configurations**
3. Select target OU, add JSON:
```json
{
  "LocalNetworkAccessAllowedForUrls": [
    "https://your-internal-domain.int"
  ]
}
```
4. Verify via `chrome://policy` → Reload policies

### Chrome — MDM Deployment
Deploy `LocalNetworkAccessAllowedForUrls` policy per platform:
- **Windows (Intune):** OMA-URI via Windows registry path
- **macOS:** `.mobileconfig` plist format
- **Android:** Managed app configuration

### Firefox — End User Self-Service
1. Click permissions icon in address bar → find **Access local network devices** → click **X** next to Blocked
2. Refresh page → click **Allow** when prompted
3. Check **Remember my choice for this site** to persist

### Firefox — Advanced (`about:config`)

| Preference | Default | Action |
|---|---|---|
| `network.lna.enabled` | `true` | Set `false` to disable all LNA checks |
| `network.lna.blocking` | `true` | Set `false` to allow without prompts |
| `network.lna.skip-domains` | empty | Comma-separated domains/wildcards to exempt (e.g., `.company.com`) |

### Firefox — Enterprise
Use `LocalNetworkAccess` policy via Firefox Enterprise Policy Documentation.

## Configuration Values
- **Chrome policy:** `LocalNetworkAccessAllowedForUrls`
- **Chrome disable flags (deprecated v144):** `LocalNetworkAccessRestrictionsEnabled`, `LocalNetworkAccessRestrictionsTemporaryOptOut`
- **Chrome advanced flag:** `chrome://flags/#local-network-access-check`

## Gotchas
- Chrome disable/opt-out policies (`LocalNetworkAccessRestrictionsEnabled`, `TemporaryOptOut`) are deprecated as of Chrome v144
- Users clicking **Block** on initial prompt lose access; requires manual remediation per site
- Firefox LNA rollout is progressive — not all standard users affected yet

## Related Docs
- [Chrome Enterprise Policy Reference](https://chromeenterprise.google/policies/)
- [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/)
- [Manage Chrome user profiles in Workspace](https://support.google.com/chrome/a/answer/7349337)