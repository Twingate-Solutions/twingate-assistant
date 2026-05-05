## SentinelOne Configuration (Trust Method)

Integrate SentinelOne with Twingate -- gates Twingate access on SentinelOne EDR signal for macOS and Windows.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### How It Works

- Twingate uses the SentinelOne API to pull the list of managed devices
- Twingate Client returns the device serial number; matched against SentinelOne's list
- A device is **SentinelOne-verified** when ALL of:
  - Its serial is in the SentinelOne managed list
  - It has reported to SentinelOne **within the past hour** (much tighter than Intune/Jamf/Kandji's 7 days)
  - Is **not infected**
  - Is **not decommissioned**
  - Does **not** require a threat reboot
  - Operational state is `na` (agent not disabled or corrupted)

### Supported Platforms

- **macOS** and **Windows**

### Setup

**Stage 1: Generate SentinelOne Service User + API Token**

1. SentinelOne Management Console -> **Settings** (left panel)
2. **Users** in the top bar
3. **Service Users** tab
4. **Actions -> Create New Service User**
5. Name + expiration date
6. Choose the site/account Twingate should access
7. Permission: **Viewer** (or higher)
8. Save the **API token** -- needed in Stage 2

**Stage 2: Connect in Twingate**

1. Twingate Admin Console -> **Settings -> Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter:
   - **Management URL** -- just the subdomain (e.g., `abcd` for `https://abcd.sentinelone.net/web/api`)
   - API token from Stage 1
4. Save

Device Settings page shows current sync status.

### Add to Trusted Profiles

- Device Security -> Trusted Profiles
- Create/edit Trusted Profile for **macOS** or **Windows**
- Add **SentinelOne** as a Trust Method
- Apply via Resource Policies requiring Trusted Devices

### Troubleshooting

**"Waiting to sync"**: initial sync takes a few minutes -- normal

**"SentinelOne not verified"** reasons:
- Not managed by SentinelOne
- Hasn't reported in the past hour (very tight window!)
- SentinelOne marks the device as: infected, decommissioned, requires reboot, agent disabled, agent corrupted
- Couldn't read serial from device
- Couldn't fetch SentinelOne data

**Recoverable errors**: shows last success + last failure; auto-resolves
**Unrecoverable errors** (credentials revoked): integration stops; admins emailed

### Decision Notes

- **The 1-hour reporting window is much tighter than other Trust Methods** (Intune/Jamf/Kandji use 7 days). Devices that go offline briefly may temporarily fail verification.
- Use SentinelOne if your org already runs S1 -- excellent EDR signal for security-conscious deployments
- Service User with Viewer permission is sufficient -- minimum-privilege approach
- Set the API token expiration generously but rotate periodically -- expired token = silent integration failure

### Gotchas

- The 1-hour reporting requirement is unforgiving -- communicate to users that going offline overnight may delay morning access until S1 phones home
- "Operational state na" wording is unintuitive -- it actually means "not disabled/corrupted" (i.e., healthy)
- The Management URL must be just the subdomain, NOT the full URL -- common configuration error
- API token expiration breaks the integration silently -- monitor admin email for unrecoverable error notifications

### Related Docs

- /docs/device-security-guide -- Trusted Profiles model
- /docs/trusted-devices -- Trusted Devices policy rule
- /docs/managed-devices -- Trust Methods overview
- /docs/crowdstrike-configuration -- Alternative EDR Trust Method (sibling pattern)
