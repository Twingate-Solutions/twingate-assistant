## Browser Security (Twingate Browser Extension)

The **Twingate Browser Extension** restricts which browsers can access sensitive Resources, applies enterprise application controls (block copy/paste/download/etc.), and shows DNS Filtering block pages on HTTPS sites.

**Status: Early Access** -- contact your Twingate account manager to enable.

### Three Use Cases

| Use Case | What It Does | Plan |
|---|---|---|
| **App Gating with Browser Restriction** | Force users to access certain Resources from a specific managed browser | Enterprise |
| **Enterprise Application Controls** | Block copy / paste / download / upload / print on sensitive Resources | Enterprise |
| **HTTPS Block Pages for DNS Filtering** | Show informative block page for HTTPS sites blocked by DNS Filtering | Any plan with DNS Filtering |

### How It Works

- Browser extension communicates with the local Twingate Client
- When a Resource has an **Application Control Policy**:
  - Traffic to that Resource is routed through Twingate **only if** it originates from a browser running the extension
  - Traffic from other browsers is **NOT** routed through Twingate -> Resource is unreachable
  - Application controls (copy/paste/etc.) apply within the running browser

### Compatible Clients

- macOS standalone Client 2024.238+
- Windows Client 2024.351+

### Compatible Browsers

- **Native**: Google Chrome, Microsoft Edge, Arc Browser
- **Other Chromium browsers**: supported with advanced configuration (contact Twingate)
- Firefox / Safari: NOT supported

### Distribution

**Chrome Web Store ID**: `jfkgjobgdomomdkjlndhpolcbbfbfdbp`

**Distribution methods:**
- **Google Workspace**: follow Google's force-install policy; search by extension ID
- **MDM / `ExtensionInstallForceList` policy**: works for Chrome Enterprise, Edge, other managed Chromium
- **Manual**: Chrome Web Store install (one-off only)

**Force-install + pin** is strongly recommended -- prevents users from disabling.

**Disable Developer Tools on the extension** (default for force-installed): prevents users from inspecting/modifying the extension. Optionally disable DevTools globally to prevent source-view bypass of UI restrictions.

### Configuring Application Control Policies

Admin Console -> **Admin -> Policies -> App Control Policies**:

**Block actions:**
- Copy
- Paste
- Upload
- Download
- Print

**Content Restrictions:**
- Show watermark on sensitive Resources

Apply Application Control Policies to Resources just like Resource Policies.

**Important**: Once applied, the Resource is ONLY reachable from a browser running the extension. **Test on a single Resource before fleet rollout** -- premature application breaks user workflows.

### DNS Filtering Block Pages

No additional config required. Once the extension is installed alongside DNS Filtering:
- HTTP-blocked sites: standard block page (works without extension)
- HTTPS-blocked sites: extension shows the block page instead of "site can't be reached"
- The extension does this **without breaking SSL** -- no MITM / cert injection needed

### Analytics

Blocked actions reported in Twingate analytics:
- When the action happened
- What action was blocked (copy, download, etc.)
- The domain the action was performed on

Exportable via S3 sync (per /docs/syncing-data-to-s3).

### Decision Notes

- The browser extension is a **strong** lockdown -- only use Application Control Policies on Resources where users genuinely need browser-only access
- For most SaaS gating: prefer SaaS App Gating with IdP (per /docs/saas-app-gating-best-practices) which doesn't require an extension
- Block-action policies (copy/paste/download) are user-visible nudges -- don't expect them to be cryptographically enforced
- Test thoroughly before applying to production Resources -- premature deployment breaks workflows

### Gotchas

- Firefox/Safari users locked out of Resources with Application Control Policies -- communicate this fleet-wide
- Force-install + pin is necessary -- without it, users can disable the extension and bypass controls
- The extension is in early access -- expect feature evolution

### Related Docs

- /docs/dns-filtering -- DNS Filtering (extension shows HTTPS block pages)
- /docs/security-policies -- Application Control Policies fit here
- /docs/saas-app-gating-best-practices -- IdP-based gating (often a better fit)
- /docs/internet-security -- IS overview
