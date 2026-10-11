---
source: https://help.twingate.com/articles/2672568245-engaging-technical-support
type: help
fetched: 2026-10-11
source_version: dfb9ca4be95404dded7de629115b9512ccb9831b9876fef62e724663b8855468
trust: official
---

# Engaging Technical Support

## Summary
Covers how Twingate Admins open and manage technical support requests via the Twingate Customer Portal. End users must contact their own Twingate Admin — Twingate support works only with Admins. An active subscription with Technical Support Entitlement is required for formal support.

---

## Key Information
- **Who can open tickets:** Twingate Admins only (not end users)
- **Community support** is available for all subscription tiers
- **Paid support** requires a subscription with Technical Support Entitlement
- Portal admin visibility: Request portal admin status from support to view all org tickets

---

## Prerequisites
- Active subscription with Technical Support Entitlement
- Completed self-service troubleshooting steps before opening a ticket
- Signed into the Twingate Customer Portal (via Admin Console → Help → Support)

---

## What Support Covers / Does Not Cover

| ✅ Covered | ❌ Not Covered |
|---|---|
| Connector or Client faults/errors | Billing (use Subscription Management) |
| Features not working as expected | Access/permissions changes (e.g., 2FA reset, role changes) |
| Connectivity troubleshooting (post self-serve) | Implementation or configuration assistance |
| | Third-party apps, OS, network issues |
| | Twingate CLI, custom API/deployment scripts |

---

## Step-by-Step: Opening a Technical Assistance Request

1. Sign in to the **Twingate Customer Portal**
2. Click **Create Ticket** (top right)
3. Select **Technical Assistance** from the dropdown
4. Fill in required fields:
   - **Issue Type** — category of issue
   - **Priority** — align to Priority Levels (P1/Urgent = full org production outage only)
   - **Twingate Component** *(optional)* — affected component
   - **Subject** — brief description
   - **Description** — include:
     - Name/ID of affected Connector, Resource, User, or Device
     - Self-serve troubleshooting results
     - Has this ever worked? Has anything changed?
     - Timestamp of occurrence
     - Frequency and scope (isolated vs. widespread)
     - Relevant error messages
   - **Attachments** — attach full log bundle (Client Logs or Connector Logs)
5. Click **Submit**

---

## After Submission
- Email confirmation sent on ticket creation
- Twingate responds via email for follow-up or next steps
- View/update open tickets in the Customer Portal
- Add replies or attachments directly to the open request

---

## Gotchas
- P1/Urgent priority is **strictly** for full production outages affecting the entire org — misuse is discouraged
- Twingate **cannot** make user account changes (2FA resets, role changes) except in extraordinary account recovery cases requiring proof-of-identity
- Environmental configurations that break Twingate functionality are **not supported**
- CLI and custom scripts are explicitly out of scope

---

## Related Docs
- Self-Serve Troubleshooting Guide
- Technical Support Coverage Hours
- Technical Support Priority Levels
- Client Logs / Connector Logs
- Signing into the Twingate Customer Portal
- Subscription Management