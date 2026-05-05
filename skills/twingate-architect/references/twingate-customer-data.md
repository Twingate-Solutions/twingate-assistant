## Twingate & Customer Data

Technical and legal reference for what customer data Twingate collects and how it is handled across Private Access, Identity Firewall, and DNS Filtering.

**Three Data Categories (Private Access):**
- **Services Data** -- control plane data: user details (name/email, not passwords), groups, resource definitions, remote networks, security policies, network logs, access tokens, configuration; stored on Twingate Controller infrastructure in the US; used to provide, maintain, and improve services
- **Content Data** -- data plane payloads between Clients and Resources; end-to-end encrypted; Twingate Relays route but do not store or decrypt it; not stored by Twingate
- **Usage Data** -- operational/diagnostic data (crash reports, telemetry, bandwidth stats); stored alongside services data; may be published in anonymized/aggregated form

**Identity Firewall:**
- Handles the same three data categories
- Session recording logs (captured by the customer-deployed Gateway) are content data — Twingate has no access to them; end-to-end encryption means Twingate cannot decrypt session contents

**DNS Filtering:**
- When enabled: collects domain names accessed, timestamps, user identity, and device details for users running the Twingate Client who are not excluded by admin
- Stored on Twingate infrastructure in the US
- Used only to provide and improve the service

**Infrastructure Locations:**
- Twingate operates from the US; development subsidiary in Israel
- Data stored on GCP-based infrastructure in the US, mirrored for resiliency

**Related Docs:**
- /docs/twingate-security -- Security architecture
- /docs/dora-locations -- DORA-specific location list
- /docs/gdpr-compliance -- GDPR data processing addendum
