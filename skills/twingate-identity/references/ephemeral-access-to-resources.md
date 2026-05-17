# Ephemeral Access to Resources

## Summary
Ephemeral Access grants temporary, time-limited access to Resources for specific users or Groups. Access automatically expires at a configured time, removing the Group from the Resource without manual intervention.

## Key Information
- Expiration window: 1 hour minimum to 1 year maximum from current date
- Access is managed at the **Group level** (not individual user level)
- Upon expiration, Group is automatically removed from the Resource
- All expiration changes are logged in **Audit Logs** under the Access category

## Prerequisites
- Admin Console access
- Existing Groups and Resources configured in Twingate

## Step-by-Step

### Via Resource Page
1. Navigate to the Resource page in Admin Console
2. When adding a new Group: specify expiration time/date during the add flow
3. For existing Group access: click the **options button** next to the Group → set/modify expiration time

### Via Group Page
1. Navigate to the relevant Group page in Admin Console
2. Locate the Resource in the Group's access list
3. Set expiration time for that specific Resource

## Configuration Values
- **Minimum expiration**: 1 hour from current time
- **Maximum expiration**: 1 year from current date
- **Granularity**: Specific date and time selection

## Common Use Cases
- Projects with defined end dates
- Contractor/vendor engagements
- "Break glass" emergency access to sensitive resources

## Gotchas
- Expiration is set per **Group-Resource relationship**, not per individual user — all users in the Group lose access simultaneously
- No built-in notification/warning before expiration; plan accordingly
- Modifying expiration resets the timer — audit log will reflect the change
- If you need to extend access, you must update the expiration before it elapses (once expired, the Group is removed and must be re-added)

## Related Docs
- Audit Logs (Access category)
- Groups management
- Resource access configuration