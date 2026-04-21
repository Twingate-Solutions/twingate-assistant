## macOS Client

Install and setup guide for the Twingate macOS Client. Available via Mac App Store (preferred) or standalone installer; requires VPN configuration and (for standalone) a system extension.

**Key Information:**
- Two install options: Mac App Store or standalone client (for environments without Apple ID)
- Apple Silicon (M-series) natively supported
- Enabling notifications is strongly recommended -- used for additional authentication prompts on sensitive Resources
- VPN configuration is required; system extension is additionally required for the standalone client
- After connecting, only traffic for configured Resources is intercepted

**Step-by-Step:**
1. Install from Mac App Store or get.twingate.com (or standalone installer)
2. Run the app -- complete onboarding: allow notifications, add VPN configuration, enable system extension (standalone only)
3. Enter network name (e.g., `autoco`) -- click "Join Network"
4. Use dropdown to connect -- authenticate via IdP in browser -- click "Open Twingate.app" when prompted
5. Browser closes; Client shows online

**Gotchas:**
- After IdP authentication in browser, clicking "Open Twingate.app" is required to activate the Client -- missing this step leaves the Client offline
- System extension approval requires macOS security settings access and may need admin approval in MDM-managed environments

**Related Docs:**
- /docs/macos-standalone-client -- Standalone (non-App-Store) macOS Client details
- /docs/macos-and-ios -- Combined macOS/iOS documentation
- /docs/clients -- Client overview
