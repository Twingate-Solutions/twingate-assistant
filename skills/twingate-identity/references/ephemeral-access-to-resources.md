# Ephemeral Access to Resources

## Summary
Ephemeral Access grants temporary, time-limited access to Resources for specific users or Groups. Access automatically expires after a configured duration, removing the Group from the Resource without manual intervention.

## Key Information
- Configure from either a **Resource page** or **Group page**
- Expiration window: **1 hour minimum** to **1 year maximum** from current date
- On expiration: Group is automatically removed from the Resource
- All expiration changes logged in **Audit Logs** under the Access category (Admin Console)

## Prerequisites
- Admin Console access
- Existing Groups and Resources configured in Twingate

## Step-by-Step

### Via Resource Page
1. Navigate to the Resource page
2. When adding a Group, specify an expiration time/date
3. For existing Group access: click the **options button** → set expiration time

### Via Group Page
1. Navigate to the relevant Group page
2. Locate the Resource in the Group's resource list
3. Set expiration time for that specific Resource

## Configuration Values
| Parameter | Range | Behavior |
|-----------|-------|----------|
| Expiration time | 1 hour – 1 year | Group auto-removed from Resource at expiry |

## Common Use Cases
- Projects with defined end dates
- Contractor engagements
- "Break glass" access to sensitive resources

## Gotchas
- No sub-hour granularity (minimum unit is 1 hour)
- Expiration removes the **Group** from the Resource, not individual users — all users in that Group lose access simultaneously
- Audit trail exists but no built-in pre-expiry notification mentioned

## Related Docs
- Audit Logs (Access category)
- Resource management
- Group management