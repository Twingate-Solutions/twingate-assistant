---
source: https://www.twingate.com/docs/twingate-customer-data
type: docs
fetched: 2026-11-19
source_version: b8904087e92f9e3c50c36e7c9dc89c71968a5410ec8cbd41ed54a548301544a9
trust: official
---

# Twingate & Customer Data

## Summary
This page explains what customer data Twingate collects, stores, and uses across Private Access, Privileged Access Management (PAM), and DNS Filtering. It is aimed at privacy, legal, and security reviewers. Twingate separates control-plane data from data-plane content, which is end-to-end encrypted and not stored or inspected by Twingate.

## Key Information
- **Architecture:** Controllers, Relays, and the Admin Console are operated by Twingate in the cloud. Clients, Resources, Connectors (and PAM Gateways) are customer-operated.
- **Three data categories (Private Access and PAM):**
  1. **Services data** (control plane): user names and emails, groups, resource definitions, remote network names, security policies, network logs, access tokens, config, and support request content. User passwords are not stored; authentication is delegated to the identity provider (Okta, OneLogin, social logins). Stored on Controller infrastructure in the US (including vendors such as Google Cloud), mirrored across locations. Used to provide, maintain, support, and improve the service.
  2. **Content data** (data plane): payloads such as files, media, and commands. These are end-to-end encrypted. Twingate does not store, use, or decrypt them. Relays only route traffic when a peer-to-peer connection can't be established, and no data-carrying connections terminate at a Relay.
  3. **Usage data:** crash reports, UI interactions, bandwidth, telemetry. Stored with services data. Used for service improvement, and may be published if anonymized/de-identified or free of confidential information.
- **PAM:**
  - Requires a Private Access subscription.
  - Operates at the application layer.
  - Session recording (e.g. Kubernetes, SSH) is performed by customer-deployed Gateways in customer infrastructure. Twingate cannot access or decrypt these logs.
  - Session recording logs count as content data.
- **DNS Filtering:**
  - When enabled by an admin, it logs domain names accessed, time, user identity, and device details.
  - It applies only to users running the Twingate Client who aren't excluded by an admin.
  - Logs are stored on Twingate US infrastructure.
  - Used only to provide, maintain, support, and improve the service.
- **Workforce:** Twingate is US-based with a development subsidiary in Israel. Vendors and contractors are subject to due diligence and contractual requirements.

## Prerequisites
- None for reading. PAM requires a Private Access subscription. DNS Filtering must be enabled by an admin.

## Step-by-Step
Not applicable (conceptual/policy page).

## Configuration Values
None listed. Policies are defined through the Admin Console or Twingate API. DNS Filtering exclusions are admin-configurable per user.

## Gotchas
- Services data (including network logs and support request content) is stored in the US only. Consider this for data residency reviews.
- Twingate cannot recover or inspect session recordings because Gateways are customer-hosted. Retention and security of those logs is the customer's responsibility.
- DNS Filtering logs include user identity and device details, which may matter for privacy assessments.
- Usage data may be published in aggregate or anonymized form.
- Relays may be an intermediate hop but cannot read encrypted content.

## Related Docs
- Network logs
- Relays (and the technical conditions requiring relayed connections)
- DNS Filtering
- Privileged Access Management / Gateways
- Twingate vendors (subprocessors) list