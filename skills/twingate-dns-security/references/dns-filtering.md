## DNS Filtering

Twingate-native DNS filtering -- blocks malicious / unwanted domains at the DNS layer for any user running the Twingate Client. **Business / Enterprise add-on**.

### Platform Support

- **macOS, Windows, Linux** Clients only
- Mobile Clients NOT supported for DNS Filtering at this time

### How It Works

When DNS Filtering is enabled:
- Twingate Client routes all DNS queries through Twingate's DNS servers
- Twingate evaluates each query against the user's filtering profile
- Blocked queries return no IP -> client sees connection failure
- HTTP-blocked sites get redirected to a **block page** explaining why
- For HTTPS-blocked sites, deploy the **Twingate Browser Extension** to show block pages

### Enabling DNS Filtering

1. Admin Console -> **Internet Security** tab
2. If Secure DNS is disabled: enable Secure DNS, choose **Twingate DNS Filtering** as resolver
3. If already enabled: change DoH resolver to **Twingate DNS Filtering**

### DNS Filtering Profiles

**Each profile has rules + Group assignments.** A user belongs to a profile via Group membership:

- Multiple profiles ranked top-to-bottom -- top profile wins for users in multiple Groups
- Default: one profile assigned to **Everyone** Group
- Users in no assigned Group = no filtering
- **Limit: 10 profiles max**
- **Recommended pattern**: lowest-ranked default profile assigned to Everyone (catch-all); higher-ranked profiles for specific Groups

**Exception Groups**: Groups in an exception list bypass DNS Filtering entirely. Exception Groups take precedence over enrolled Groups.

**When a device is configured for always-on Internet Security and signed out**: it uses the **lowest-ranked profile**.

### Configurable Rules per Profile

**Allowlist / Denylist:**
- Add/remove specific domains
- TLDs supported in denylist (e.g., `.zip` blocks all `.zip` domains)
- **Allowlist takes precedence over all other rules**

**Security Categories** (default: all enabled except Newly Registered):
- Threat Intelligence Feeds (malware, phishing)
- Google Safe Browsing
- DNS Rebinding (private IPs in public responses)
- IDN Homograph Attacks (Cyrillic-Latin lookalikes)
- Typosquatting
- Domain Generation Algorithms (DGA)
- Newly Registered Domains (last 30 days)
- Parked Domains

**Content Categories** (off by default; enable per profile):
- Gambling, Dating, Adult Content, Piracy, Social Media, Games, Streaming Sites
- Force Safe Search (major search engines)
- YouTube Safe Mode

**Privacy Protection:**
- Block disguised third-party trackers
- Block affiliate & tracking links (warning: may break unsubscribe links)
- Block ads and trackers (general)

### Logging

**Filtering Analytics** (90/30/7-day): total queries, blocked count, block %

**Recent DNS Activity**: real-time event feed; filter by allowed/blocked. Events show device hostname, IP, profile used, block reason.

**S3 Sync**: DNS Filtering logs can sync to AWS S3 for SIEM ingestion. Format: JSON, one event per line. Schema includes:
- `event_type`: `dns_filtering`
- `event.time`: UTC datetime
- `event.domain`, `event.root`: queried domain + root
- `event.device.id`, `event.device.name`: Twingate device info
- `event.connection.client_ip`, `event.connection.protocol`
- `event.status`: `default` (allowed by default), `blocked`, or `allowed` (allowlist match)
- `event.reasons[]`: array of category/rule IDs that matched

### Signed-Out Device Handling

For devices with always-on Internet Security:
- Never signed in: hostname shown in logs
- Signed in once, single user: Twingate device name shown
- Multi-user device: name of most recently signed-in user

Older Clients (pre-macOS 2024.311 / Windows 2024.351) show "No hostname" / "No device" -- upgrade for full attribution.

### FAQ

- **Domain wrongly blocked?** Add to allowlist (takes precedence).
- **Always-on filtering?** Set up /docs/internet-security-client-configuration with Machine Keys.
- **Disable for some users?** Add their Group to the **Exception Group** list.

### Decision Notes

- For most production use: enable Threat categories + Privacy Protection + Force Safe Search; treat Content Categories as optional based on org policy
- Default Everyone-Group profile is the safety net -- always have one
- S3 sync is essential for compliance/audit use cases -- enable from day one to build retention
- Browser Extension is required for HTTPS block pages -- without it, users just see "site can't be reached"

### Gotchas

- Tracking link blocking can break unsubscribe / account verification flows in emails -- communicate to users
- Mobile devices have NO DNS filtering -- be explicit about this gap
- Users in NO assigned Group skip filtering entirely -- always have an Everyone-assigned default profile
- Allowlist > Categories -- a category-blocked domain on the allowlist will pass through

### Related Docs

- /docs/dns-security -- DoH foundation
- /docs/internet-security -- IS overview
- /docs/internet-security-client-configuration -- Always-on (Machine Key)
- /docs/browser-security -- Browser Extension for HTTPS block pages
- /docs/syncing-data-to-s3 -- S3 log sync
- /docs/nextdns-configuration, /docs/doh-cloudflare -- Third-party DNS filtering alternatives
