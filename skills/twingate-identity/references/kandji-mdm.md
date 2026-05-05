## Deploying Twingate Clients with Kandji

How to distribute the Twingate macOS and iOS Clients via Kandji.

**macOS -- Recommended: Twingate Auto App**
- Kandji has a first-class **Auto App** for Twingate
- Fastest deployment path -- no PKG upload, no custom config required
- Auto App handles automatically:
  - Notifications permission
  - VPN profile activation
  - System extension approval

**macOS -- Alternative: Custom App**
- Not recommended unless you need to pin a specific PKG version
- Upload the Twingate .pkg from the Twingate download page as a Kandji Custom App
- You'll need to manually configure VPN profile + system extension separately (see "Pre-configuring the macOS Client" below)

**iOS:**
- Add Twingate Client app to **Apple Business Manager** first
- Link Kandji to ABM (per Kandji's official docs)
- Then distribute the iOS app from Kandji

**Locating Twingate in Kandji:**
- Sign in to Kandji
- **Library** in the sidebar -> find "Twingate Client" for macOS / iOS

**Pre-Migration Step (Important):**
- If end users have manually installed Twingate previously, uninstall those Clients first via a temporary Kandji policy
- Why: manually-installed versions may differ from the MDM-distributed version, causing config drift
- Deactivate the cleanup policy before rolling out the MDM-managed Client

**Pre-Configuring the macOS Client (only needed for Custom App path):**
- Follow the Twingate **Configuration Profiles** guide (linked from this doc)
- Pre-populates: VPN configuration, system extension allowance, default Twingate network
- The **Auto App path automates all of this** -- skip this step if using Auto App

**Decision: Auto App vs. Custom App**

| Aspect | Auto App | Custom App |
|---|---|---|
| Setup time | Minutes | Hours |
| Auto-handles permissions | Yes | No (manual config profile) |
| Version pinning | Latest | You control |
| Recommended | Yes | Only if version pinning is required |

**Gotchas:**
- The Auto App auto-updates the Client -- if you need controlled rollouts, use Custom App + version-locked PKGs
- Custom App without the configuration profile leaves the Client unable to enable its system extension silently -- always pair them

**Related Docs:**
- /docs/macos-and-ios -- Configuration profile keys
- /docs/jamf-mdm -- Jamf equivalent (more manual)
- /docs/intune-configuration -- Intune for Windows fleets
- /docs/omnissa-workspace-one-mdm -- Workspace ONE equivalent
