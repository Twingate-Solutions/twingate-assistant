# Ephemeral Access to Resources

## Summary
Ephemeral Access grants time-bounded access to Resources for specific Groups, with automatic revocation at expiration. Configured via the Admin Console, it sets an expiration on a Group's access to a Resource without requiring manual cleanup.

## Key Information
- Access expiration range: 1 hour to 1 year from current date
- Expired Groups are **automatically removed** from the Resource
- Active expirations show an `Expires [date]` pill on the Group row
- All expiration changes are logged in **Access category** of audit logs
- Expiration can be removed without revoking access entirely

## Prerequisites
- Admin Console access
- Existing Resource and Group configured in Twingate

## Configuration Steps

### From a Resource Page
**New Group:**
1. Navigate to Resource → access configuration
2. Click **Set Expiration** → select date/time → click **Set Expiration Time**
3. Click **Grant Access** to finalize

**Existing Group:**
1. Click options menu on Group row → **Set Expiration**
2. Select date/time → **Set Expiration Time**
3. To clear: use **Remove Expiration** link inside the date picker

### From a Group Page
**New Resource:**
1. Navigate to Group → add Resource → click **Set Expiration** → set date/time

**Existing Resource:**
1. Click options menu on Resource row → **Set Expiration** → set date/time

## Configuration Values
| Parameter | Range |
|-----------|-------|
| Expiration window | 1 hour – 1 year from current date |

## Gotchas
- Expiration removes the **Group from the Resource** entirely — all users in that Group lose access simultaneously
- "Remove Expiration" clears the timer but does **not** remove the Group's access
- No API/CLI configuration documented — Admin Console only
- No warning notifications mentioned before expiration occurs

## Common Use Cases
- Fixed-duration contractor access
- Project-scoped access with defined end dates
- Break-glass scenarios for sensitive Resources

## Related Docs
- Audit Logs (Access category)
- Resource access configuration
- Group management