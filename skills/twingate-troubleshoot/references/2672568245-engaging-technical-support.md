---
source: https://help.twingate.com/articles/2672568245-engaging-technical-support
type: help
fetched: 2026-10-04
source_version: 24be2cb7d906fc7d06f02405d95f5a761374dd29529a9487330a2bbfbf572609
trust: official
---

# Engaging Technical Support

## Page Title
Engaging Technical Support

## Summary
Covers how Twingate Admins open technical support tickets via the Twingate Customer Portal. Defines scope of support, required ticket fields, and what to include for faster resolution. End users must go through their Twingate Admin; Twingate will not work directly with end users.

## Key Information
- Only **Twingate Admins** can open support tickets — not end users
- Community support available to all subscriptions; dedicated technical support requires an active subscription with Technical Support Entitlement
- Ticket type to select: **Technical Assistance**

## What Support Covers
**In scope:**
- Native Connector or Client faults/errors
- Twingate component not working as expected
- Connectivity troubleshooting (after self-serve guide exhausted)

**Out of scope:**
- Billing (use Subscription Management portal)
- Account/permission changes (2FA reset, role changes)
- Implementation or configuration assistance (contact sales)
- Third-party apps, OS, network issues
- Twingate CLI, custom API scripts, or deployment scripts

## Step-by-Step: Opening a Ticket
1. Sign into the Twingate Customer Portal
2. Click **Create Ticket** (top right)
3. Select **Technical Assistance** from dropdown
4. Fill in required fields (see Configuration Values below)
5. Attach full log bundle
6. Click **Submit**

## Configuration Values / Ticket Fields

| Field | Notes |
|---|---|
| Issue Type | Type of issue observed |
| Priority | Align to Priority Levels; P1/Urgent = full org production down only |
| Twingate Component | Optional; select impacted component |
| Subject | Brief description |
| Description | See required details below |
| Attachments | Full log bundle required |

**Required description details:**
- Name or ID of affected Connector, Resource, User, or Device
- Results from Self-Serve Troubleshooting Guide
- Has this ever worked? Has anything changed?
- Timestamp of occurrence
- Frequency of issue
- Error messages
- Isolated vs. widespread

## Log Collection
- **Client logs:** See "Client Logs" doc
- **Connector logs:** See "Connector Logs" doc
- Include full log bundle, not partial

## Gotchas
- P1/Urgent priority is **strictly** for full production outages affecting the entire org — do not misuse
- Twingate will **not** reset 2FA or change user roles except in extraordinary circumstances with proof of email domain ownership
- To view all org tickets in the portal, request **portal admin** access from Twingate Support
- Account recovery requires proof-of-identity showing ownership of the user account's email domain

## Accessing Existing Tickets
- Admin Console → **Help** → **Support** → Customer Portal
- Replies and attachments can be added to open requests

## Related Docs
- Self-Serve Troubleshooting Guide
- Technical Support Coverage Hours
- Technical Support Priority Levels
- Client Logs / Connector Logs
- Signing into the Twingate Customer Portal
- Subscription Management