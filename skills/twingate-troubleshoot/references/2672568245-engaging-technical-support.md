---
source: https://help.twingate.com/articles/2672568245-engaging-technical-support
type: help
fetched: 2026-08-09
source_version: 1677f217810f0dd3126d5278d30327f33201bad2311e0fb8119fe6b2caaff754
---

# Engaging Technical Support

## Summary
Describes how Twingate Admins can open technical support tickets via the Twingate Customer Portal. End users must contact their own Twingate Admins—Twingate support works only with Admins directly. Requires an active subscription with ticketed support entitlement.

## Key Information
- **Who can engage support**: Twingate Admins only (not end users)
- **Community support**: Available to all subscriptions
- **Ticketed support**: Requires active subscription with that entitlement
- **Portal access**: Admin Console → Help → Support

## What Support Covers
**Supported:**
- Native Connector or Client faults/errors
- Twingate component/feature not working as expected
- Connectivity troubleshooting (after self-serve guide exhausted)

**Not Supported:**
- Billing (use Subscription Management)
- User account changes (2FA resets, role changes)
- Implementation or configuration assistance (contact sales)
- Third-party apps, OS, network issues
- Twingate CLI, custom API scripts, or deployment scripts

## Step-by-Step: Opening a Ticket
1. Sign into Twingate Customer Portal
2. Click **Create Ticket** (top right)
3. Select **Technical Assistance** from dropdown
4. Fill in required fields (see Configuration Values below)
5. Attach full log bundle (Client or Connector logs)
6. Click **Submit**

## Configuration Values (Ticket Fields)
| Field | Notes |
|-------|-------|
| Issue Type | Type of issue observed |
| Priority | Align to Priority Levels; P1/Urgent = full org production down only |
| Twingate Component | Optional; affected component |
| Subject | Brief issue statement |
| Description | See required details below |
| Attachments | Full log bundle required |

**Required Description Details:**
- Name/ID of affected Connector, Resource, User, or Device
- Results from Self-Serve Troubleshooting Guide
- Has this ever worked? Has anything changed?
- Timestamp of occurrence
- Frequency of issue
- Error messages
- Isolated vs. widespread

## Gotchas
- P1/Urgent priority is **only** for full production outages affecting the entire org—do not misuse
- Twingate cannot perform account recovery without proof-of-identity showing ownership of the email domain
- To view all organization tickets in portal, you must request **portal admin** access from Twingate Support
- Environmental configurations that break Twingate functionality are not supported

## Prerequisites
- Active subscription with ticketed support entitlement
- Self-serve troubleshooting already attempted
- Must be a Twingate Admin

## Related Docs
- Self-Service Resources
- Technical Support Entitlement
- Technical Support Coverage Hours
- Technical Support Priority Levels
- Self-Serve Troubleshooting Guide
- Client Logs / Connector Logs
- Signing into the Twingate Customer Portal
- Subscription Management