---
source: https://help.twingate.com/articles/2672568245-engaging-technical-support
type: help
fetched: 2026-09-27
source_version: aabf728270496fe7d1f93947918f292dd3ce751302579a7fb4bfe9451b26b54d
---

# Engaging Technical Support

## Summary
Guide for Twingate Admins to open technical support requests via the Twingate Customer Portal. End users must contact their Twingate Admin directly; Twingate support only works with Admins. Requires an active subscription with Technical Support Entitlement.

## Key Information
- **Who can engage support**: Twingate Admins only (not end users)
- **Community support**: Available for all subscription tiers
- **Paid support**: Requires Technical Support Entitlement on subscription
- Portal admin status (to view all org tickets) must be requested from Twingate Support

## What Support Covers
**In scope:**
- Native Connector or Client faults/errors
- Twingate features not working as expected
- Connectivity troubleshooting (after self-serve steps exhausted)

**Out of scope:**
- Billing (use Subscription Management)
- Account/permission changes (2FA resets, role changes)
- Implementation or configuration assistance (contact sales)
- Third-party apps, OS, network issues
- Twingate CLI, custom API scripts, deployment scripts

## Prerequisites
- Complete [Self-Service Troubleshooting Guide](https://help.twingate.com) steps first
- Active subscription with Technical Support Entitlement
- Access to Twingate Admin Console

## Step-by-Step: Opening a Support Ticket

1. Sign into Twingate Customer Portal (via Admin Console → **Help** → **Support**)
2. Click **Create Ticket** (top right)
3. Select **Technical Assistance** from dropdown
4. Fill required fields:
   - **Issue Type**: Category of issue
   - **Priority**: Align to Priority Levels (P1/Urgent = full production down, entire org impacted)
   - **Twingate Component** *(optional)*: Affected component
   - **Subject**: Brief description
5. In **Description**, include:
   - Name/ID of affected Connector, Resource, User, or Device
   - Self-serve troubleshooting results
   - Has this worked before? What changed?
   - Timestamp of occurrence
   - Frequency of issue
   - Error messages
   - Scope: isolated vs. widespread
6. **Attachments**: Include full log bundle (Client Logs or Connector Logs)
7. Click **Submit**

## After Submission
- Email confirmation sent on ticket creation
- Twingate responds via email for follow-up or next steps
- View/update open tickets in Customer Portal → select ticket → add replies or attachments

## Gotchas
- P1/Urgent priority is **only** for full production outages affecting the entire organization
- Account recovery (e.g., 2FA reset) requires proof-of-identity showing ownership of the email domain
- Environmental configurations that break Twingate functionality are not supported
- To view all org tickets in portal, you must be enabled as a **portal admin** — request this from Twingate Support

## Related Docs
- Self-Serve Troubleshooting Guide
- Client Logs / Connector Logs
- Technical Support Priority Levels
- Technical Support Coverage Hours
- Signing into the Twingate Customer Portal
- Subscription Management