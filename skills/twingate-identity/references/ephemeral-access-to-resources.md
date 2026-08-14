---
source: https://www.twingate.com/docs/ephemeral-access-to-resources
type: docs
fetched: 2026-08-14
source_version: 16e87e095a9530fd580b64b44798910f7e60eebf253fa9bab2d76eb0323aad3d
---

# Ephemeral Access to Resources

## Page Title
Ephemeral Access to Resources

## Summary
Ephemeral Access grants time-bounded access to Resources for specific Groups, with automatic revocation at expiration. Configured via the Admin Console, it sets an expiration on a Group's access to a Resource within a window of 1 hour to 1 year. When the expiration is reached, the Group is automatically removed from the Resource.

## Key Information
- Access expiration is set **per Group per Resource** (not globally)
- Expiration range: **1 hour to 1 year** from current date
- Expired Groups are **automatically removed** from the Resource — no manual cleanup needed
- Active expirations display as an **`Expires [date]` pill** in the Admin Console
- All expiration changes are logged in **audit logs** under the Access category
- Expiration can be **removed without revoking access** using the "Remove Expiration" link in the date picker

## Prerequisites
- Admin Console access with permissions to manage Resources and Groups
- Groups must exist before granting ephemeral access

## Step-by-Step

### From a Resource Page (new Group)
1. Navigate to the Resource page
2. Begin granting access to a new Group
3. Click **Set Expiration** in the access configuration
4. Select date and time in the date picker
5. Click **Set Expiration Time**
6. Click **Grant Access** to finalize

### From a Resource Page (existing Group)
1. Navigate to the Resource page
2. Click the **options menu** on the Group's row
3. Select **Set Expiration**
4. Modify date/time or click **Remove Expiration** to clear it

### From a Group Page
- Same patterns apply — use **Set Expiration** when adding a new Resource, or use the **options menu** on existing Resources

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Minimum expiration | 1 hour from current time |
| Maximum expiration | 1 year from current date |
| Scope | Per Group, per Resource |

## Gotchas
- Expiration applies to the **Group's access**, not individual users — all users in the Group lose access simultaneously
- Removing an expiration ≠ removing access; the Group retains access indefinitely until manually removed
- No notification system mentioned — plan for user communication before expiration independently
- Cannot set expiration on a per-user basis, only per Group

## Common Use Cases
- Projects with a defined end date
- Contractor engagements with fixed duration
- "Break glass" scenarios for temporary sensitive Resource access

## Related Docs
- Twingate Groups documentation
- Twingate Resources documentation
- Audit Logs (Access category)