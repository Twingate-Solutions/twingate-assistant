# Ephemeral Access to Resources

## Summary
Ephemeral Access grants time-bounded access to Resources for specific Groups, with automatic revocation at expiration. Configured via the Admin Console, it removes the Group from the Resource when the expiration time is reached, revoking access for all users in that Group.

## Key Information
- Access expiration range: **1 hour to 1 year** from current date
- Expiration is set at the **Group-Resource relationship level**, not per-user
- Expired Groups are **automatically removed** from the Resource (no manual action needed)
- Active expirations display an **"Expires [date]" pill** on the Group row
- All expiration changes are logged in **audit logs** under the Access category
- Expiration can be **removed without revoking access** using the "Remove Expiration" link in the date picker

## Prerequisites
- Admin Console access
- Existing Groups and Resources configured in Twingate

## Step-by-Step

### Grant New Access with Expiration (from Resource Page)
1. Navigate to the Resource page
2. Add a new Group to the Resource
3. Click **Set Expiration** in the access configuration
4. Select date and time via the date picker
5. Click **Set Expiration Time**
6. Click **Grant Access** to finalize

### Modify Expiration on Existing Group Access (from Resource Page)
1. Navigate to the Resource page
2. Find the Group row with existing access
3. Click the **options menu** on the Group row
4. Select **Set Expiration**
5. Modify date/time, or click **Remove Expiration** to clear without revoking access

### From Group Page
- Same patterns apply—use **Set Expiration** when adding new Resources, or **options menu → Set Expiration** for existing Resource access

## Gotchas
- Expiration applies to the **entire Group's access**, not individual users—removing ephemeral access affects all Group members
- **Removing expiration** ≠ revoking access; use "Remove Expiration" to make access permanent again
- No built-in notification/warning before expiration occurs (access is silently revoked at the set time)
- Cannot set expiration shorter than 1 hour or longer than 1 year

## Common Use Cases
- Projects with defined end dates
- Contractor engagements with fixed durations
- "Break glass" emergency access to sensitive Resources

## Related Docs
- Twingate Groups documentation
- Twingate Resources documentation
- Audit Logs (Access category)