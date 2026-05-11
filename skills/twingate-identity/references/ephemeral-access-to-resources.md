# Ephemeral Access to Resources

## Summary
Ephemeral Access grants temporary, time-limited access to Resources for specific users or Groups. Access automatically expires at a configured time, removing the Group from the Resource without manual intervention.

## Key Information
- Configurable from either a **Resource page** or a **Group page**
- Expiration window: **1 hour minimum** to **1 year maximum** from current date
- On expiration: Group is automatically removed from Resource; users lose access
- Expiration changes are logged in **Audit Logs → Access category** in Admin Console
- Expiration times can be modified after initial assignment

## Prerequisites
- Admin Console access
- Existing Groups and Resources configured in Twingate

## Step-by-Step

### Via Resource Page
1. Navigate to the Resource page in Admin Console
2. Add a Group to the Resource (or select an existing Group via the options button)
3. Set expiration time and date (range: next hour → 1 year)
4. Save — Group is auto-removed when expiration is reached

### Via Group Page
1. Navigate to the relevant Group page
2. Locate the Resource to set expiration on
3. Set the expiration time for that specific Resource

## Configuration Values
| Parameter | Range | Notes |
|-----------|-------|-------|
| Expiration time | 1 hour – 1 year | From current date/time |

## Common Use Cases
- Projects with defined end dates
- Contractor/third-party engagements
- "Break glass" emergency access to sensitive resources

## Gotchas
- No built-in notification/warning before expiration — plan accordingly
- Modifying expiration requires manual action; no recurring/renewable access option mentioned
- Audit log entries only capture changes to expiration times, not just access events

## Related Docs
- Audit Logs (Access category)
- Resource configuration
- Group management