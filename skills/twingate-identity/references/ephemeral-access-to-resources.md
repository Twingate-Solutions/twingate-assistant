# Ephemeral Access to Resources

## Page Title
Ephemeral Access to Resources

## Summary
Ephemeral Access grants time-bounded access to Resources for specific Groups, with automatic revocation at expiration. Configured via the Admin Console on Resource or Group pages, it supports expiration windows from 1 hour to 1 year. When expired, the Group is automatically removed from the Resource and users lose access.

## Key Information
- Access expiration range: **1 hour to 1 year** from current date
- Expiration is set **per Group per Resource** (not globally)
- Expired Groups are **automatically removed** from the Resource
- Expiration changes are logged in **audit logs** (Access category)
- Expiration can be **removed without revoking** the Group's access entirely
- Visual indicator: `Expires [date]` pill on Group rows

## Prerequisites
- Admin Console access
- Existing Groups and Resources configured in Twingate

## Step-by-Step

### From a Resource Page (New Group)
1. Navigate to the Resource page
2. Begin granting access to a new Group
3. Click **Set Expiration** in the access configuration
4. Select date and time in the date picker
5. Click **Set Expiration Time** to confirm
6. Click **Grant Access** to finalize

### From a Resource Page (Existing Group)
1. Navigate to the Resource page
2. Click the **options menu** on the Group's row
3. Select **Set Expiration**
4. Choose date/time or click **Remove Expiration** to clear without revoking access

### From a Group Page
- Same patterns apply: use **Set Expiration** when adding new Resources, or **options menu → Set Expiration** for existing Resources

## Configuration Values
| Parameter | Range | Notes |
|-----------|-------|-------|
| Expiration time | 1 hour – 1 year | From current date/time |

## Gotchas
- Expiration removes the **entire Group** from the Resource — all users in that Group lose access simultaneously
- No partial/per-user expiration within a Group
- No built-in notification to users before expiration occurs (not mentioned in docs)
- Must use **Remove Expiration** (not delete) to clear a timer without revoking access

## Common Use Cases
- Projects with defined end dates
- Contractor engagements with fixed duration
- "Break glass" scenarios for sensitive Resource access

## Related Docs
- Twingate Groups documentation
- Twingate Resources documentation
- Audit Logs (Access category)