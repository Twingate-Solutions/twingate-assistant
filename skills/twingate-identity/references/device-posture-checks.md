## Device Security Posture Checks

Per-platform checks the Twingate Client performs to assess device posture. Used as building blocks in Trusted Profiles and Minimum OS Requirements.

### Checks by Platform

**Windows** (10, 11, Server 2022)
- **HD Encryption** -- BitLocker on system disk and other disks
- **Screen Lock** -- password required after screen saver (via WinAPI `LogonUser`)
- **Firewall** -- Windows or third-party firewall enabled (via Windows Security Center)
- **Antivirus** -- AV installed (via Windows Security Center)
- **Minimum OS Version** -- OS meets configured minimum

**macOS** (12-15)
- **Screen Lock** -- password required after sleep / screen saver
- **Biometric Configuration** -- Touch ID or Face ID configured
  - Note: in clamshell mode (lid closed), biometric **always** reports as disabled regardless of actual config
- **Firewall** -- native firewall enabled
  - Standalone Client only
  - Note: "Block all incoming connections" causes the device to report firewall as **disabled** (counterintuitive but documented)
- **HD Encryption** -- FileVault enabled
  - Standalone Client only
- **Minimum OS Version**

**Linux** (Debian/Ubuntu, CentOS/Fedora, Arch)
- **Firewall** -- UFW, firewalld, or iptables enabled
- **HD Encryption** -- all partitions except `/boot` encrypted via LUKS (uses `libcryptsetup`)

**iOS** (15-18)
- **Screen Lock** -- password required
- **Biometric Configuration** -- Touch ID or Face ID configured
- **Minimum OS Version**

**Android**
- **Screen Lock** -- any screen lock configured (PIN, pattern, biometric)
- **Biometric Configuration** -- fingerprint or facial recognition configured
- **HD Encryption** -- File-Based Encryption (FBE) enabled

### Gotchas

- **macOS firewall + "Block all incoming"**: counterintuitive — system reports firewall **disabled** in this mode. If your fleet uses Block-all-incoming, don't enforce the Firewall posture check on macOS.
- **macOS clamshell**: biometric reports disabled when the laptop lid is closed -- accommodates this in policy if your users dock laptops with lids closed
- **macOS Firewall + HD Encryption**: only available in the **standalone Client**, not the App Store version. If you mandate these checks, deploy the standalone Client via MDM.
- **Linux HD Encryption**: only LUKS is recognized -- other disk encryption schemes (eCryptfs, native distro tools without LUKS) won't satisfy the check
- **Windows Screen Lock**: relies on `WinAPI LogonUser` -- password complexity isn't checked, just that *some* password is required

### Decision Notes

- Use posture checks in **Minimum OS Requirements** for the broad baseline (e.g., "all devices must have screen lock + encryption")
- Use posture checks in **Trusted Profiles** when combined with verification methods (CrowdStrike + posture, Manual + posture)
- Don't enforce checks that aren't available on the deployed Client variant -- e.g., HD Encryption on macOS App Store Client will always fail

### Related Docs

- /docs/device-security-guide -- How posture checks fit into Trusted Profiles + Minimum OS Requirements
- /docs/trusted-devices -- Trusted Devices policy rule
- /docs/device-only-resource-policies -- Skip user auth, evaluate posture only
- /docs/macos-standalone-client -- Standalone macOS Client (required for some macOS checks)
- /docs/security-policies -- Policy types overview
