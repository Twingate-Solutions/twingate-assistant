# Configuring AnyConnect with Umbrella

## Summary
AnyConnect with Umbrella Module is compatible with Twingate, unlike the legacy Umbrella Roaming Client. To ensure proper operation, Twingate resource domains must be added to AnyConnect's Internal Domains list so DNS traffic is not intercepted by Umbrella.

## Key Information
- **Roaming Client** intercepts DNS by replacing OS resolvers with `127.0.0.1`; does not detect OS resolver changes after startup — **incompatible with Twingate**
- **AnyConnect with Umbrella Module** uses a kernel module intercepting port 53 traffic — **fully compatible with Twingate**
- AnyConnect kernel module routes DNS to Umbrella backend unless destination matches an Internal Domain
- Internal Domain matches are cached in-memory (tagged "do not intercept") until AnyConnect restarts
- Customers can upgrade from Roaming Client to AnyConnect at no cost

## Prerequisites
- AnyConnect with Umbrella Module installed (not the legacy Roaming Client)
- Access to Cisco Umbrella Management Console
- Knowledge of domain names used by Twingate Resources

## Step-by-Step Configuration

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add each domain used by Twingate Resources
   - Example: Add `example.com` to cover all `*.example.com` resources
4. Save configuration

## Configuration Values

| Setting | Location | Notes |
|---|---|---|
| Internal Domains | Deployments → Configuration → Domain Management | Add Twingate resource domains |
| Wildcard syntax | Left-hand only | `example.com` implies `*.example.com` |

## Gotchas
- **Publicly resolvable domains** protected by Twingate must also be added to Internal Domains — not just private/internal ones
- **Midfield wildcards not supported**: `bla.*.example.com` is invalid; only left-hand wildcards work
- `example.com` and `*.example.com` are treated as equivalent in the Internal Domains list
- Roaming Client caches resolver list at startup and never polls for changes — this is the root cause of Twingate incompatibility

## Related Docs
- [Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)
- Twingate Roaming Client incompatibility: use AnyConnect as replacement