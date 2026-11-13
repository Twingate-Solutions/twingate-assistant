---
source: https://help.twingate.com/articles/2672568245-engaging-technical-support
type: help
fetched: 2026-11-13
source_version: 466ef5b4c44640c88c5edbd6c2d29730a5a8da8edae80c8b24304fcda79d53a3
trust: official
---

# Engaging Technical Support

## Summary
This page explains how Twingate Admins open a Technical Assistance request through the Twingate Customer Portal. It also covers what support does and does not handle, which details to include in a ticket, and how to follow up on open requests.

## Key Information
- Only Twingate Admins can engage Twingate support. End users must go through their own admins (security and liability reasons).
- Technical support requires an active subscription with Technical Support Entitlement. Community support is available for all subscriptions.
- Coverage hours are listed on the "Technical Support Coverage Hours" page.
- **Support covers:**
  - Faults or errors in the native Twingate Connector or Client.
  - Components or features not working as expected.
  - Connectivity troubleshooting when the Self-Serve Troubleshooting Guide doesn't resolve the issue.
- **Support does NOT cover:**
  - Billing (see Subscription Management).
  - Access or permission changes, such as 2FA resets or user role changes. Account recovery in extraordinary cases requires proof of ownership of the email domain.
  - Implementation or configuration help (contact your sales representative).
  - Third-party apps, OSes, networks, known incompatibilities, or environments that break Twingate functionality.
  - Twingate CLI, custom API scripts, or deployment scripts.
- Exceptions may apply per your Support Services Agreement.

## Prerequisites
- Try the Self-Service Resources first, including the Self-Serve Troubleshooting Guide.
- Active subscription with Technical Support Entitlement.
- Twingate Admin role.

## Step-by-Step: Open a Request
1. Sign into the Twingate Customer Portal. From the Admin Console, click **Help**, then **Support**.
2. Click **Create Ticket** (top right).
3. Select **Technical Assistance** from the drop-down.
4. Fill in the fields:
   - **Issue Type**
   - **Priority**: P1/Urgent is only for a full production outage affecting the entire organization.
   - **Twingate Component** (optional)
   - **Subject**
   - **Description**
   - **Attachments**: full log bundle of the affected component (see Client Logs or Connector Logs docs).
5. Click **Submit**.

## Description Checklist
- Name or ID of the affected Connector, Resource, User, or Device.
- Results from the Self-Serve Troubleshooting Guide.
- Whether it has ever worked, and whether anything changed.
- Timestamp(s) of occurrence and frequency.
- Relevant error messages.
- Whether the issue is isolated or widespread.

## After Submission
- You get a confirmation email, and support follows up by email for more information.
- Review open requests in the Customer Portal and add replies or attachments.
- To see all of your organization's tickets, ask Twingate Support to enable you as a portal admin.

## Configuration Values
None (no env vars, CLI flags, or API parameters). The ticket form fields are listed above.

## Gotchas
- Do not mark a request P1 unless production is fully down organization-wide.
- Support cannot reset 2FA or change user roles.
- Omitting the full log bundle will slow resolution.
- Custom scripts, CLI, and API usage are out of scope.

## Related Docs
- Self-Service Resources / Self-Serve Troubleshooting Guide
- Technical Support Coverage Hours
- Technical Support Priority Levels
- Signing into the Twingate Customer Portal
- Client Logs
- Connector Logs
- Subscription Management