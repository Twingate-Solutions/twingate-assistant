# Ephemeral Access to Resources

## Summary
Ephemeral Access grants time-bounded access to Resources for specific Groups, with automatic revocation at expiration. Configured via "Set Expiration" in the Admin Console, it removes the Group from the Resource when the time window expires.

## Key Information
- Access is scoped to **Group-Resource relationships**, not individual users
- Expiration range: **1 hour to 1 year** from current date/time
- At expiration, the Group is **automatically removed** from the Resource
- Active expirations display an **"Expires [date]" pill** on the Group row
- All expiration changes are logged in **audit logs** under the Access category
- Expirations can be **cleared without removing access** via "Remove Expiration" link in the date picker

## Prerequisites
- Admin Console access
- Existing Groups and Resources configured in Twingate

## Configuration Steps

### From a Resource Page
1. Navigate to the Resource page
2. **New Group**: Click "Set Expiration" during access configuration → select date/time → click "Set Expiration Time" → click "Grant Access"
3. **Existing Group**: Click options menu on Group row → "Set Expiration" → select date/time

### From a Group Page
1. Navigate to the Group detail page
2. **New Resource**: Click "Set Expiration" during access configuration
3. **Existing Resource**: Click options menu on Resource row → "Set Expiration"

### Remove an Expiration (Without Revoking Access)
- Open the date picker via "Set Expiration" → click "Remove Expiration" link inside the picker

## Common Use Cases
- Projects with defined end dates
- Contractor engagements with fixed durations
- "Break glass" scenarios requiring temporary sensitive Resource access

## Gotchas
- Expiration removes the **entire Group** from the Resource — all users in that Group lose access simultaneously
- No per-user expiration; granularity is at the Group level only
- No mention of notification/warning before expiration triggers
- Minimum expiration is 1 hour; cannot set sub-hour windows

## Related Docs
- Audit Logs (Access category)
- Group management
- Resource access configuration