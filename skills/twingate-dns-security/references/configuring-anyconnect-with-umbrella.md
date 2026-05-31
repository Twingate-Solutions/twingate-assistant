# Configuring AnyConnect with Umbrella for Twingate

## Page Title
How to Configure AnyConnect with Umbrella

## Summary
AnyConnect with Umbrella Module is compatible with Twingate (unlike the legacy Umbrella Roaming Client). To prevent AnyConnect from intercepting Twingate resource traffic, protected domains must be added to AnyConnect's Internal Domains list.

## Key Information
- **Roaming Client** = legacy Cisco product; incompatible with Twingate Client due to static DNS resolver list behavior
- **AnyConnect with Umbrella Module** = current product; fully compatible with Twingate
- AnyConnect operates via kernel module intercepting port 53 traffic — no OS resolver list modification
- Upgrade from Roaming Client to AnyConnect with Umbrella Module is free

## Prerequisites
- AnyConnect with Umbrella Module installed (not legacy Roaming Client)
- Access to Cisco Umbrella Management Console
- Knowledge of Twingate Resource domains (e.g., `*.example.com`)

## Step-by-Step Configuration

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add each Twingate Resource domain (e.g., `example.com`)
4. Repeat for all domains backing Twingate Resources

## Configuration Values

| Setting | Location | Value |
|---|---|---|
| Internal Domains | Umbrella Console → Deployments → Configuration → Domain Management | Twingate resource domains (e.g., `example.com`) |

## Gotchas
- **Wildcard syntax**: AnyConnect does **not** support midfield wildcards (`bla.*.example.com` is invalid). Left-hand wildcards are implied — adding `example.com` is equivalent to `*.example.com`
- **Publicly resolvable domains**: Must be explicitly added to Internal Domains list even if publicly resolvable, or AnyConnect will intercept and forward to Umbrella instead of allowing Twingate to resolve them
- **Roaming Client incompatibility**: The Roaming Client captures the OS resolver list at startup and never polls for changes; Twingate Client cannot function alongside it

## How AnyConnect Internal Domains Works
- Matched domains → request returned to OS network stack (bypasses Umbrella)
- Unmatched domains → forwarded to Umbrella backend for allow/block decision
- "Do not intercept" tags are held in memory and reset on AnyConnect restart

## Related Docs
- [Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)