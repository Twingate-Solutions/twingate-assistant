# Ephemeral Access to Resources

## Summary
Ephemeral Access grants time-bounded access to Resources for specific Groups, with automatic revocation at expiration. Configured via the Admin Console on either Resource or Group pages, it removes the Group from the Resource automatically when the expiration time is reached.

## Key Information
- Access expiration range: **1 hour to 1 year** from current date
- Expiration is set **per Group per Resource** (not globally)
- At expiration: Group is automatically removed from Resource; users lose access
- Active expirations display an **"Expires [date]" pill** in the UI
- All expiration changes are logged in **Admin Console audit logs** (Access category)
- Expiration can be removed without revoking access (via "Remove Expiration" link)

## Prerequisites
- Admin Console access
- Existing Groups and Resources configured in Twingate

## Configuration Steps

### From a Resource Page
1. Navigate to the Resource page
2. **New Group:** Click "Set Expiration" during access configuration → select date/time → click "Set Expiration Time" → click "Grant Access"
3. **Existing Group:** Click options menu on Group's row → "Set Expiration" → select date/time

### From a Group Page
1. Navigate to the Group's detail page
2. **New Resource:** Click "Set Expiration" during access configuration → select date/time
3. **Existing Resource:** Click options menu on Resource row → "Set Expiration"

### Removing an Expiration (Without Revoking Access)
- Open the date picker via "Set Expiration" → click "Remove Expiration" link inside the picker

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Minimum expiration | 1 hour from now |
| Maximum expiration | 1 year from now |
| Granularity | Date and time picker |

## Use Cases
- Projects with defined end dates
- Contractor engagements with fixed duration
- Break-glass scenarios (temporary sensitive Resource access)

## Gotchas
- Expiration is **per Group**, not per individual user — all users in the Group lose access simultaneously
- No warning/notification mechanism mentioned before expiration — plan ahead
- Audit log category is "Access" — filter accordingly when reviewing logs

## Related Docs
- Resource access configuration
- Group management
- Admin Console audit logs