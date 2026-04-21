## Client Application Overview

Index page for the Twingate Client covering all supported platforms, download URLs, minimum supported versions, and update policy. Clients older than 12 months cannot connect to Twingate.

**Key Information:**
- Supported platforms: macOS, Windows, Linux, iOS, Android & ChromeOS
- Organization subdomain (e.g., `autoco`) entered once on first use
- Client uses local VPN at 127.0.0.1 to intercept Resource traffic
- Clients older than 12 months are blocked from connecting

**Minimum Supported Versions (as of page date):**
- macOS: 2024.57, Windows: 2024.51, Linux: 2024.63, iOS: 2024.57, Android: 2024.85

**Direct Download Endpoints:**
- macOS PKG: `https://api.twingate.com/download/darwin?installer=pkg`
- Windows EXE: `https://api.twingate.com/download/windows`
- Windows MSI: `https://api.twingate.com/download/windows?installer=msi`
- iOS: `https://api.twingate.com/download/ios`
- Android: `https://api.twingate.com/download/android`
- Linux: convenience script from Twingate's public repositories

**Gotchas:**
- Clients over 12 months old are blocked -- enforce update policies in MDM to prevent user lockouts
- MSI deployments have additional prerequisites (e.g., .NET 8 runtime on Windows) -- see platform-specific docs

**Related Docs:**
- /docs/windows -- Windows Client setup
- /docs/macos -- macOS Client setup
- /docs/linux -- Linux Client setup
- /docs/managed-devices -- MDM/enterprise deployment
- /docs/endpoint-requirements -- Firewall and system requirements
