---
source: https://help.twingate.com/articles/2672568245-engaging-technical-support
type: help
fetched: 2026-09-20
source_version: b317cd00ca3d6707c7ca2f29823af944a04710fe932f687264eeef9f112a338d
---

# Engaging Technical Support

## Summary
Guide for Twingate Admins to open technical support requests via the Twingate Customer Portal. End users must contact their Twingate Admin directly; Twingate support only works with admins. Requires an active subscription with Technical Support Entitlement.

## Key Information
- **Who can engage support**: Twingate Admins only (not end users)
- **Community support**: Available for all subscription tiers
- **Portal access**: Admin Console → Help → Support

## Prerequisites
- Active subscription with Technical Support Entitlement
- Review Self-Service Resources and Self-Serve Troubleshooting Guide first
- Log bundles collected (Client Logs or Connector Logs)

## What Support Covers
**Supported:**
- Native Connector or Client faults/errors
- Features not working as expected
- Connectivity troubleshooting (after self-serve guide exhausted)

**Not Supported:**
- Billing (use Subscription Management)
- User account changes (2FA reset, role changes)
- Implementation or configuration (contact sales rep)
- Third-party apps, OS, network issues
- Twingate CLI, custom API scripts, deployment scripts

## Step-by-Step: Opening a Ticket
1. Sign into Twingate Customer Portal
2. Click **Create Ticket** (top right)
3. Select **Technical Assistance** from dropdown
4. Fill required fields:
   - **Issue Type**: Type of issue observed
   - **Priority**: Align to Technical Support Priority Levels (P1/Urgent = full production down, entire org impacted)
   - **Twingate Component** (optional): Affected component
   - **Subject**: Brief issue statement
   - **Description**: Include all details below
5. Attach full log bundle
6. Click **Submit**

## Required Description Details
- Name or ID of affected Connector, Resource, User, or Device
- Results from Self-Serve Troubleshooting Guide
- Has this ever worked?
- Has anything changed recently?
- Timestamp of occurrence
- Frequency of issue
- Relevant error messages
- Isolated vs. widespread impact

## Gotchas
- P1/Urgent priority is strictly for full production outages affecting the entire organization
- Account changes (2FA reset) require proof-of-identity showing ownership of the email domain
- Portal admin access (to see all org tickets) must be explicitly requested from Twingate Support
- Twingate will not support environments where third-party configurations break Twingate functionality

## Related Docs
- Technical Support Coverage Hours
- Technical Support Priority Levels
- Self-Serve Troubleshooting Guide
- Client Logs / Connector Logs
- Signing into the Twingate Customer Portal
- Subscription Management