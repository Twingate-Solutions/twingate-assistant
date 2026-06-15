# Ephemeral Access to Resources

## Summary
Ephemeral Access grants time-bounded access to Resources for specific Groups, with automatic revocation at expiration. Configured via the Admin Console on either Resource or Group pages, it removes the Group from the Resource automatically when the expiration is reached.

## Key Information
- Access is granted at the **Group level**, not individual user level
- Expiration range: **1 hour to 1 year** from current date
- At expiration: Group is automatically removed from Resource; all users in that Group lose access
- Active expirations display an **"Expires [date]" pill** in the UI
- All expiration changes are logged in **audit logs** under the Access category
- Expiration can be **removed without revoking access** (via "Remove Expiration" link in date picker)

## Prerequisites
- Admin Console access
- Existing Groups and Resources configured in Twingate

## Step-by-Step

### Set Expiration on New Group Access (from Resource page)
1. Navigate to the Resource page
2. Begin granting access to a new Group
3. Click **Set Expiration** in the access configuration
4. Choose date and time in the date picker
5. Click **Set Expiration Time** to apply
6. Click **Grant Access** to finalize

### Modify Expiration on Existing Group Access (from Resource page)
1. Navigate to the Resource page
2. Click the **options menu** on the Group's row
3. Select **Set Expiration**
4. Modify the date/time, or click **Remove Expiration** to clear without revoking access

### From Group Page
- Same patterns apply: **Set Expiration** when adding new Resources; **options menu → Set Expiration** for existing Resources

## Configuration Values
| Parameter | Range | Notes |
|-----------|-------|-------|
| Expiration time | 1 hour – 1 year | From current date/time |

## Gotchas
- Access is Group-scoped — cannot set per-user expiration directly; user loses access only when the Group is removed
- Removing expiration ≠ removing access; the Group retains access indefinitely until manually removed or a new expiration is set
- No notification mechanism mentioned — users are not warned before expiration

## Use Cases
- Projects with defined end dates
- Contractor engagements with fixed duration
- Break-glass access to sensitive Resources

## Related Docs
- Twingate Groups documentation
- Twingate Resources documentation
- Audit Logs (Access category)