---
source: https://help.twingate.com/articles/4097879304-browser-local-network-access-lna-blocking-twingate-resources
type: help
fetched: 2026-11-22
source_version: 10a1cec624853f2618a4da52497fab2cf581e52aa45e11e579760571e8c0e71d
trust: official
---

# Browser Local Network Access (LNA) Blocking Twingate Resources

## Summary
Chrome/Chromium and Firefox now enforce Local Network Access (LNA) restrictions. Twingate routes traffic over CGNAT via loopback to the virtual Twingate interface, so browsers treat Resources as local and may prompt or block. If users click Block, they can lose browser access to Resources.

## Key Information
- **Applies to:** Chrome/Chromium 142+ (LNA on by default), Firefox Beta/Nightly (on by default), and standard Firefox with ETP set to Strict (progressive rollout). Mac, Windows, Linux.
- **Symptoms:** Resources inaccessible after Block, elevated CORS errors, blocked images, "Not secure" label (Chrome).
- **General workaround:** Narrow Resource definitions that unnecessarily cover public CDN domains (e.g. `*.amazonaws.com`, `*.microsoftonline.com`, `azureedge.net`, `*.azure.com`) if they aren't required and can be resolved privately.

## Prerequisites
- Chrome managed policies: managed browser profiles (Google Workspace) or MDM.
- Firefox enterprise policy: an enterprise policy deployment mechanism.

## Step-by-Step

**Chrome, unmanaged (user self-serve)**
1. Click **Not Secure** in the address bar and toggle **Local Network Access**, or open **Site settings** > **Local network access** > **Allow**.

**Chrome, Google Workspace**
1. Admin console > **Chrome Browser > Custom Configurations**.
2. Select the target OU.
3. Add JSON: `{"LocalNetworkAccessAllowedForUrls": ["https://your-internal-domain.int"]}`
4. Save, then check `chrome://policy` and click **Reload policies**.

**Chrome, MDM**
- Deploy `LocalNetworkAccessAllowedForUrls` via Intune (OMA-URI/registry), macOS (.mobileconfig), or Android (managed app config). Formats are in the Chrome Enterprise policy reference (https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls).

**Firefox, unmanaged**
1. Click the permissions icon in the address bar; next to **Access local network devices**, click the X after **Blocked**.
2. Refresh, then click **Allow** (check **Remember my choice for this site** to persist).
3. Manage saved permissions in Settings > Privacy & Security > Permissions (**Device apps and services** / **Local network devices** > Settings...).

## Configuration Values
**Chrome**
- Policy: `LocalNetworkAccessAllowedForUrls`
- Opt-out policies: `LocalNetworkAccessRestrictionsEnabled`, `LocalNetworkAccessRestrictionsTemporaryOptOut` (deprecated as of Chrome v144)
- Flag: `chrome://flags/#local-network-access-check`

**Firefox (`about:config`)**
- `network.lna.enabled` (bool, default true): set false to disable LNA.
- `network.lna.blocking` (bool, default true): set false to allow without prompts.
- `network.lna.block_trackers` (bool, default false, experimental).
- `network.lna.skip-domains` (string, default empty): comma-separated domains to skip, with wildcard support, e.g. `intranet.company.com,*.devices.local`.
- Enterprise policy: `LocalNetworkAccess`.

## Gotchas
- Changing `chrome://flags` or `about:config` can affect browser stability and security; intended for advanced users.
- The Chrome disable/opt-out policies are deprecated as of v144, so prefer the allow-list policy.
- Managed Chrome profiles must be configured for Workspace policies to apply.
- Firefox "Don't ask again" remembers the decision, including Block.

## Related Docs
- Chrome Enterprise policy reference (https://chromeenterprise.google/policies/#LocalNetworkAccessAllowedForUrls)
- Manage user profiles on Chrome browser (https://support.google.com/chrome/a/answer/9025411?hl=en)
- Custom Chrome policies in Workspace (https://support.google.com/chrome/a/answer/14749672)
- Chrome Browser quick start (Mac) (https://support.google.com/chrome/a/answer/9020077)
- Mozilla LNA permissions (https://support.mozilla.org/en-US/kb/control-personal-device-local-network-permissions-firefox)
- Firefox Enterprise Policy Documentation (https://mozilla.github.io/policy-templates/)