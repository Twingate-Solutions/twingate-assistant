# Configuring AnyConnect with Umbrella for Twingate

## Summary
AnyConnect with Umbrella Module is compatible with Twingate, unlike the legacy Umbrella Roaming Client. Configuration requires adding Twingate-protected domains to AnyConnect's Internal Domains list to prevent traffic interception.

## Key Information
- **Roaming Client**: Legacy, incompatible with Twingate — do not use alongside Twingate Client
- **AnyConnect with Umbrella Module**: Fully compatible with Twingate; uses kernel module to intercept DNS on port 53
- AnyConnect does **not** modify the OS resolver list (unlike Roaming Client)
- Internal Domains bypass Umbrella and return to normal OS network stack
- Publicly resolvable domains protected by Twingate **must** be added to Internal Domains list

## Prerequisites
- Cisco AnyConnect Client with Umbrella Module (not legacy Roaming Client)
- Access to Cisco Umbrella Management Console
- Knowledge of domains used by Twingate Resources (e.g., `*.example.com`)

## Step-by-Step Configuration

1. Log into **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add each domain used by Twingate Resources
   - Example: add `example.com` to cover all subdomains

## Configuration Values

| Setting | Location | Value |
|---|---|---|
| Internal Domains | Deployments → Configuration → Domain Management | Your Twingate resource domains (e.g., `example.com`) |

## Gotchas
- **Roaming Client incompatibility**: The legacy Umbrella Roaming Client captures the OS resolver list at startup and never updates it — Twingate Client cannot function alongside it
- **Wildcard syntax**: AnyConnect does **not** support midfield wildcards (`bla.*.example.com` is invalid). Left-hand wildcards are implied — `example.com` automatically covers `*.example.com`
- **Publicly resolvable domains**: Must explicitly be added to Internal Domains or Umbrella will intercept/block Twingate resolution
- AnyConnect tags intercepted domains as "do not intercept" in memory; tags reset on AnyConnect Client restart

## Related Docs
- [Cisco Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)
- Cisco AnyConnect upgrade from Roaming Client is available free of charge