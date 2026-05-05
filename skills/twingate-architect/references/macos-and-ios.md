## macOS & iOS MDM Distribution

Guide for deploying the Twingate Client to managed macOS and iOS devices via MDM. Covers custom configuration profiles (.mobileconfig), available key/value configuration pairs, and Apple Business Manager distribution without personal Apple IDs.

**Key Information:**
- Both App Store and Standalone Clients can be deployed via MDM; Standalone recommended to access all features
- Configuration profiles (.mobileconfig XML) enable silent install, network name pre-population, and update control
- Clients older than 12 months cannot connect -- manage updates via MDM to prevent lockouts
- MDM-specific guides available for: Kandji, Jamf, Omnissa Workspace ONE

**Supported MDM Configuration Keys (PayloadType: com.twingate.macos):**
- `network` (String) -- pre-populate Twingate network name
- `PresentedDataPrivacy` (Boolean true) -- suppress privacy screen on first launch
- `PresentedEducation` (Boolean true) -- suppress education screen on first launch
- `automaticallyInstallSystemExtension` (Boolean true) -- auto-install system extension (standalone only)
- `LaunchApp` (Boolean) -- launch on login; set false if using launch daemon
- `SUEnableAutomaticChecks` (Boolean) -- enable automatic update checks (standalone only)
- `SUAutomaticallyUpdate` (Boolean) -- auto-download and prompt to install updates (standalone only)

**Apple Business Manager (ABM):**
1. Sign in to Apple Business Manager with company Apple ID
2. Search for "Twingate" and provision seats (free)
3. App seats appear in MDM -- deploy to devices without personal Apple IDs

**Gotchas:**
- Setting `LaunchApp: true` conflicts with the Twingate launch daemon -- set to false if using the daemon
- The system extension must be pre-approved in the configuration profile for fully silent deployment

**Related Docs:**
- /docs/macos -- macOS Client general setup
- /docs/macos-standalone-client -- Standalone Client details
- /docs/managed-devices -- Overview of managed device options
