---
source: https://help.twingate.com/articles/2672568245-engaging-technical-support
type: help
fetched: 2026-08-06
source_version: 6a1171f7616bd89c8fa2b26db091f5b57810ec0ea6000fa6d4ac11376ea39214
---

# Engaging Technical Support

## Summary
Guide for Twingate Admins to open technical support requests via the Twingate Customer Portal. End users must contact their Twingate Admin directly; Twingate support only works with Admins. Requires an active subscription with ticketed support entitlement.

## Key Information
- **Who can engage support**: Twingate Admins only (not end users)
- **Community support**: Available for all subscription tiers
- **Ticketed support**: Requires active subscription entitlement
- **Portal access**: Admin Console → Help → Support

## What Support Covers
**In scope:**
- Native Connector or Client faults/errors
- Features not working as expected
- Connectivity troubleshooting (after self-serve steps exhausted)

**Out of scope:**
- Billing (use Subscription Management)
- Account/permission changes (2FA resets, role changes)
- Implementation or configuration assistance (contact sales)
- Third-party apps, OS, network issues
- Twingate CLI, custom API scripts, deployment scripts

## Prerequisites
- Active subscription with ticketed support entitlement
- Completed self-service troubleshooting steps
- Must be a Twingate Admin

## Step-by-Step: Opening a Ticket
1. Sign into the Twingate Customer Portal
2. Click **Create Ticket** (top right)
3. Select **Technical Assistance** from dropdown
4. Fill in required fields (see Configuration Values below)
5. Attach full log bundle (Client Logs or Connector Logs)
6. Click **Submit**

## Configuration Values (Ticket Fields)
| Field | Notes |
|-------|-------|
| Issue Type | Type of issue observed |
| Priority | Align to Technical Support Priority Levels; P1/Urgent = full org production down only |
| Twingate Component | Optional; affected component |
| Subject | Brief issue statement |
| Description | See required details below |
| Attachments | Full log bundle required |

**Required description details:**
- Name/ID of affected Connector, Resource, User, or Device
- Self-serve troubleshooting results
- Has this ever worked? Has anything changed?
- Timestamp of occurrence
- Frequency of issue
- Error messages
- Isolated vs. widespread impact

## Gotchas
- P1/Urgent priority is strictly for full production outages affecting the entire organization
- Account changes (2FA reset, role changes) are not performed by support; exceptions require proof-of-identity showing email domain ownership
- To view all organization tickets in the portal, request portal admin access from the support team
- CLI, custom API scripts, and deployment scripts are explicitly out of scope

## Related Docs
- Self-Service Resources / Self-Serve Troubleshooting Guide
- Technical Support Entitlement
- Technical Support Coverage Hours
- Technical Support Priority Levels
- Subscription Management
- Client Logs / Connector Logs
- Signing into the Twingate Customer Portal