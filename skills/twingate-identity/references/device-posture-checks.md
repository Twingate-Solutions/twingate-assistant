# Device Posture Checks

## Page Title
Device Posture Checks

## Summary
Twingate Client collects native device posture data used by Device Profiles to evaluate devices against Approved Operating Systems or Trusted Profiles. Available checks vary by platform (Windows, macOS, Linux, iOS, Android).

## Key Information

### Windows Checks
- **HD encryption** – BitLocker status on system/other disks
- **Screen lock** – Password required on screen saver return
- **Firewall** – Windows or third-party firewall via Windows Security Center
- **Antivirus** – Windows or third-party AV via Windows Security Center
- **Minimum OS version** – Windows 10, 11, Windows Server 2022

### macOS Checks
- **Screen lock** – Password required after sleep/screen saver
- **Biometric** – Touch ID/Face ID configured (clamshell mode always reports disabled)
- **Firewall** – Native firewall only; standalone Client required
- **HD encryption** – FileVault status; standalone Client required
- **Minimum OS version** – macOS 14–26

### Linux Checks
- **Firewall** – UFW, firewalld, or iptables; Debian/Ubuntu, CentOS/Fedora, Arch Linux
- **HD encryption** – LUKS encryption via `libcryptsetup`; all partitions except `/boot`

### iOS Checks
- **Screen lock** – Passcode required
- **Biometric** – Touch ID/Face ID configured
- **Minimum OS version** – iOS 18–26

### Android Checks
- **Screen lock** – Any screen lock type configured
- **Biometric** – Fingerprint or facial recognition configured
- **HD encryption** – File-Based Encryption status

## Prerequisites
- Twingate Client installed on device
- macOS Firewall and FileVault checks require **macOS standalone Client** (not browser/extension)
- Linux HD encryption requires `libcryptsetup` library present

## Gotchas
- **macOS clamshell mode**: Biometric always reports as disabled when lid is closed, regardless of actual setting
- **macOS Firewall**: If "Block all incoming connections" is enabled, firewall reports as **disabled**
- **Linux HD encryption**: Only LUKS-encrypted partitions checked; `/boot` partition exclusion is expected behavior
- **Android screen lock**: Reports any lock type (PIN, pattern, etc.) — not specifically a strong password
- Firewall check on Windows reflects Security Center reporting, so third-party firewalls must register with Security Center to be detected

## Configuration Values
- Minimum OS version ranges:
  - Windows: 10, 11, Server 2022
  - macOS: 14–26
  - iOS: 18–26

## Related Docs
- Device Profiles
- Approved Operating Systems
- Trusted Profiles
- macOS standalone Client setup