---
source: https://help.twingate.com/articles/2672568245-engaging-technical-support
type: help
fetched: 2026-09-13
source_version: 4c38c00d77207d919914e48c3fb53e932ddb94e704d18195778ab556d2065520
---

# Engaging Technical Support

## Summary
Guide for Twingate Admins to open technical support requests via the Twingate Customer Portal. End users must contact their Twingate Admin directly—Twingate support only works with Admins. Requires an active subscription with Technical Support Entitlement.

## Key Information
- **Only Twingate Admins** can open support tickets; end users must go through their Admin
- Community support available for all subscription tiers; technical support requires entitlement
- Responses and updates delivered via email; tickets managed through Customer Portal

## Prerequisites
- Active subscription with Technical Support Entitlement
- Review Self-Service Resources and Self-Serve Troubleshooting Guide before submitting
- Sign-in access to Twingate Customer Portal (via Admin Console → Help → Support)

## What Support Covers
**In scope:**
- Native Connector or Client faults/errors
- Twingate features not working as expected
- Connectivity troubleshooting (after self-serve steps exhausted)

**Out of scope:**
- Billing (use Subscription Management)
- Account/permission changes (2FA resets, role changes)
- Implementation or configuration assistance (contact sales)
- Third-party apps, OS, or network issues
- Twingate CLI, custom API scripts, or deployment scripts

## Step-by-Step: Opening a Ticket
1. Sign into Twingate Customer Portal
2. Click **Create Ticket** (top right)
3. Select **Technical Assistance** from dropdown
4. Fill in required fields:
   - **Issue Type**: Type of issue observed
   - **Priority**: Align to Technical Support Priority Levels (P1/Urgent = full production down, org-wide)
   - **Twingate Component** (optional): Affected component
   - **Subject**: Brief description
   - **Description**: Include all details below
5. Attach full log bundle (Client Logs or Connector Logs)
6. Click **Submit**

## Required Description Details
- Name or ID of affected Connector, Resource, User, or Device
- Results from Self-Serve Troubleshooting Guide
- Has this ever worked? Has anything changed?
- Timestamp of when issue occurred
- Frequency of issue
- Relevant error messages
- Isolated vs. widespread impact

## Gotchas
- P1/Urgent priority is strictly for **full production outages affecting the entire org**—do not misuse
- Twingate cannot perform user account changes (2FA reset, role change) except in extraordinary circumstances requiring proof of domain ownership
- Twingate will not support environments where third-party configurations break Twingate functionality
- To view all org tickets in the portal, request **portal admin** access from Twingate Support
- CLI, custom API scripts, and deployment scripts are explicitly excluded from support scope

## Related Docs
- Self-Service Resources
- Technical Support Coverage Hours
- Technical Support Priority Levels
- Self-Serve Troubleshooting Guide
- Subscription Management
- Signing into the Twingate Customer Portal
- Client Logs / Connector Logs