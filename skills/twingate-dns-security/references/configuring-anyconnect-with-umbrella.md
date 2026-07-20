# Configuring AnyConnect with Umbrella for Twingate

## Summary
AnyConnect with Umbrella Module is compatible with Twingate, unlike the legacy Umbrella Roaming Client. Configuration requires adding Twingate resource domains to AnyConnect's Internal Domains list to prevent DNS interception interference.

## Key Information
- **Roaming Client ≠ AnyConnect**: Legacy Roaming Client is incompatible with Twingate; AnyConnect with Umbrella Module is fully compatible
- AnyConnect operates at kernel level, intercepting port 53 traffic via kernel module (no OS resolver list modification)
- Internal Domains tagged "do not intercept" are passed back to the OS network stack unchanged
- Publicly resolvable domains protected by Twingate **must** be added to Internal Domains list

## Prerequisites
- Cisco Umbrella Management Console admin access
- AnyConnect with Umbrella Module deployed (not legacy Roaming Client)
- Known list of domains for Twingate Resources

## Step-by-Step Configuration

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add each Twingate resource domain (e.g., `example.com`)
4. Save configuration

## Configuration Values

| Setting | Location | Value |
|---|---|---|
| Internal Domain entry | Umbrella Domain Management | `example.com` (covers `*.example.com`) |

## Gotchas
- **Roaming Client is incompatible** with Twingate—must migrate to AnyConnect with Umbrella Module
- AnyConnect does **not** support midfield wildcards (`bla.*.example.com` is invalid)
- Left-hand wildcards are implied: adding `example.com` is equivalent to `*.example.com`
- Roaming Client captures resolver list at startup and never refreshes it—dynamic resolver changes (like Twingate's) break it
- Internal Domain "do not intercept" tags are **in-memory only**; cleared on AnyConnect restart

## Related Docs
- Cisco Umbrella Domain Management: https://docs.umbrella.com/deployment-umbrella/docs/domain-management
- Twingate: Upgrading from Roaming Client to AnyConnect is free of charge via Cisco