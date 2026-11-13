---
source: https://www.twingate.com/docs/internet-security-use-case
type: docs
fetched: 2026-11-13
source_version: 480d4f2cdcc0c12973b00e601987b8b83537246778506f10f42be4584d1ac537
trust: official
---

# Page Title
Internet Security Use Case (Twingate Docs)

## Summary
This overview page describes how Twingate secures public internet traffic on employee devices using DNS filtering and DNS-over-HTTPS (DoH). It lists the benefits and links to guides for enabling each capability. The page contains no setup steps itself.

## Key Information
- **Threat blocking:** DNS filtering blocks domains known to host malware, phishing sites, and command-and-control servers.
- **Content control:** Can block categories such as adult content and gambling. Also gives visibility into shadow IT usage and where employee traffic is going.
- **Privacy on untrusted networks:** Encrypted DNS requests (DoH) keep browsing history private on hotel or coffee shop Wi-Fi.
- **BYOD and travel:** DNS-level filtering is managed centrally and can apply to personal (BYOD) devices.
- **Single client:** One Twingate Client handles both private Resource access and public internet security.
- **Exit Networks:** Can be used to route all traffic through Twingate.
- **Third-party integrations:** Guides exist for AnyConnect (with Umbrella) and Cloudflare (DoH and DNS filtering).

## Prerequisites
Not stated on this page. Presumably a Twingate account and the Twingate Client installed on target devices; check the individual guides to confirm.

## Step-by-Step
None on this page. Follow the linked guides:
1. Enable DNS filtering in Twingate
2. Enable DNS-over-HTTPS in Twingate
3. Route all traffic through Twingate with Exit Networks
4. Configure AnyConnect (with Umbrella) to work with Twingate
5. Configure Cloudflare for DoH and DNS filtering in Twingate

## Configuration Values
None listed (no env vars, CLI flags, or API parameters).

## Gotchas
- This is an overview page only. Implementation details, requirements, and settings are in the linked guides.
- If another security client is already deployed (e.g., AnyConnect/Umbrella), use the dedicated compatibility guide rather than enabling features blindly.

## Related Docs
- How to enable DNS filtering in Twingate
- How to enable DNS-over-HTTPS in Twingate
- How to route all traffic through Twingate with Exit Networks
- How to configure AnyConnect (with Umbrella) to work with Twingate
- How to configure Cloudflare for DNS-over-HTTPS and DNS Filtering in Twingate