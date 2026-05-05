## Windows Managed Devices (MDM Deployment)

How to distribute the Twingate Windows Client through MDM (Intune, third-party MDM, Chocolatey) and silent install / pre-config patterns.

### Package Formats

| Format | Includes .NET 8 Runtime? | Recommended? |
|---|---|---|
| **EXE** | Yes -- auto-installs the runtime | **Yes** -- preferred for MDM deployment |
| **MSI** | No -- you must distribute .NET 8 Desktop Runtime separately | Use only if EXE doesn't fit your MDM workflow |

Both formats accept the same command-line parameters. .NET 8 Desktop Runtime x64 must be present for the Client to run.

**.NET requirement**: November 2024+ Client versions require .NET Desktop Runtime 8.0 (x64) or higher.

### Command-Line Options (EXE and MSI)

| Option | Effect |
|---|---|
| `/qn` | Silent install -- suppresses dialog, accepts ToS |
| `network=<subdomain>` | Pre-configure Twingate Network -- user doesn't have to enter it |
| `auto_update=true` | After update, auto-reconnect using existing session (no re-login) |
| `no_optional_updates=true` | Disable user-triggered updates |
| `ncsi_global_dns=true` | Enables NCSI_GlobalDns -- fixes false "No internet" indicator while Twingate is running |
| `TUN_DRIVER=Wintun` | Use Wintun driver instead of TunTap (default) |

### Example Silent-Install Command

```
TwingateWindowsInstaller.exe /qn network=beamreach.twingate.com no_optional_updates=true auto_update=true
```

This: silent install, pre-set network, disable user updates, auto-reconnect after updates. Re-running on a system with Twingate already installed performs an in-place update.

### `no_optional_updates` -- When to Use

**Local admin rights granted to users:**
- Leave default (`no_optional_updates=false`)
- Users get update prompts and can update when admin auth available

**No local admin rights:**
- Set `no_optional_updates=true`
- Reason: users would see the prompt but couldn't act on it -- bad UX
- You must update via MDM push instead

**Important**: Clients older than 12 months are not supported by the Twingate service. Without user-triggered updates, your MDM **must** push updates regularly.

### MDM Solutions

**Microsoft Intune / Endpoint Manager:**
- Detailed walkthrough at /docs/intune-configuration
- Custom PowerShell script support: download .NET runtime + MSI, run installer (template available)

**Third-Party MDMs (Workspace ONE, Jamf-for-Windows, etc.):**
- Standard EXE/MSI deployment + command-line options
- Use the example command above as a starting point

**Chocolatey** (Early Access):
- `choco install twingate`
- Note: Chocolatey package is **not** updated by Twingate's automated release pipeline -- expect a delay vs. official releases

### Decision Notes

- **Always use EXE for new deployments** -- bundled .NET avoids dependency drift
- **Always set `no_optional_updates=true` for non-admin users** -- avoids broken update UX
- **Always enable `auto_update=true`** -- preserves user session across updates, removes friction
- For MSI: pin a known-good .NET 8 version in your MDM and update both packages together

### Gotchas

- MSI without .NET 8 Runtime fails silently -- no obvious error to the user
- 12-month support window means non-update fleets break Twingate access -- automate updates one way or another
- Wintun vs. TunTap: only switch if you have a specific reason; default TunTap is the maintained path
- Chocolatey lag: don't rely on it for security-critical version updates

### Related Docs

- /docs/managed-devices -- Cross-platform MDM overview
- /docs/intune-configuration -- Microsoft Intune walkthrough
- /docs/jamf-mdm, /docs/kandji-mdm, /docs/omnissa-workspace-one-mdm -- macOS/iOS MDM
- /docs/windows -- Standalone Windows Client docs
