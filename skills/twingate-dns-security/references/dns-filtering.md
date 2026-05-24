# DNS Filtering - Twingate

## Summary
Twingate provides native DNS filtering via DNS-over-HTTPS (DoH) for macOS, Windows, and Linux clients. It blocks domains at the DNS layer using configurable profiles assigned to Groups, with rules covering security threats, content categories, and privacy protection.

## Key Information
- **Availability**: Business and Enterprise plans (add-on); mobile not supported
- **Protocol**: DNS-over-HTTPS (DoH); no client config changes required beyond running Twingate Client
- **Profile limit**: 10 DNS filtering profiles
- **Log retention**: 90-day analytics; real-time activity logs
- **Block pages**: HTTP by default; HTTPS requires Twingate Browser Extension deployed
- **Priority**: Allowlist > profile ranking (top = highest priority) > lower-ranked profiles

## Prerequisites
- Business or Enterprise plan with DNS filtering add-on
- Twingate Client on macOS, Windows, or Linux
- Secure DNS enabled in Admin Console
- For HTTPS block pages: Twingate Browser Extension deployed

## Step-by-Step: Enable DNS Filtering
1. Navigate to **Internet Security** tab in Admin Console
2. If Secure DNS disabled → enable it → select **Twingate DNS Filtering**
3. If Secure DNS already enabled → change DoH resolver to **Twingate DNS Filtering**
4. Create/configure DNS filtering profiles; assign Groups to profiles
5. Optionally configure security categories, content restrictions, privacy protection

## Configuration Values

**Profile Rules:**
- `allowlist` — overrides all other rules
- `denylist` — supports TLDs (e.g., `.zip` blocks all `.zip` domains)

**Security Categories (all enabled by default except newly registered):**
- Threat Intelligence Feeds, Google Safe Browsing, DNS rebinding, IDN homograph attacks, Typosquatting, Domain generation algorithms, Newly registered domains, Parked domains

**Content Categories:** Gambling, Dating, Adult content, Piracy, Social media, Games, Streaming sites, Force Safe Search, YouTube safe mode

**Privacy Protection:** Block disguised third-party trackers, Block affiliate & tracking links, Block ads and trackers

**S3 Export JSON fields:** `event_type`, `time`, `domain`, `root`, `device.id`, `device.name`, `connection.client_ip`, `connection.protocol`, `status` (`default`/`blocked`/`allowed`), `reasons[]`

## Gotchas
- Users in multiple Groups: highest-ranked profile wins
- Exception Groups override Enrolled Groups — user in both = DNS filtering disabled
- Signed-out devices use **lowest-ranked** profile (requires "always run" Internet Security config)
- Client versions before macOS 2024.311 / Windows 2024.351 show generic device info when signed out
- Blocking tracking links may break email unsubscribe flows
- Groups can only be assigned to **one** profile at a time; cannot be both assigned and excluded simultaneously
- If a user belongs to no Group with a profile assigned, their traffic is **not filtered**

## Related Docs
- DNS-over-HTTPS (DoH) documentation
- Internet Security Client Configuration (always-on mode)
- Exception Groups
- Syncing data to S3
- Twingate Browser Extension deployment