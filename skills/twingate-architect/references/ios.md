## iOS Client

Install and setup guide for the Twingate iOS Client. Installed from the Apple App Store; authenticates via configured IdP.

**Key Information:**
- Install from Apple App Store (search "Twingate") or get.twingate.com
- Network name format: the subdomain portion of the Twingate URL (e.g., enter `autoco` for `autoco.twingate.com`; found in welcome email)
- After connecting, only traffic for configured Resources is intercepted; regular internet traffic is unaffected

**Step-by-Step:**
1. Install Twingate from App Store
2. Open app -- enter network name (e.g., `autoco`) -- tap "Join Network"
3. Tap "Sign in to Connect" -- authenticate via IdP in browser window
4. Browser closes; Client shows online

**Related Docs:**
- /docs/macos-and-ios -- macOS and iOS combined documentation
- /docs/clients -- Client overview
