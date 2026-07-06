# Configuring AnyConnect with Umbrella

## Summary
AnyConnect with Umbrella Module is compatible with Twingate, unlike the legacy Umbrella Roaming Client which conflicts with Twingate. Configuration requires adding Twingate resource domains to AnyConnect's Internal Domains list to prevent traffic interception.

## Key Information
- **Roaming Client** (legacy): Incompatible with Twingate — replaces OS DNS resolver with `127.0.0.1` loopback and uses a static, non-updating resolver list
- **AnyConnect with Umbrella Module** (current): Compatible with Twingate — uses kernel module to intercept port 53 traffic without modifying OS resolver list
- AnyConnect intercepts all DNS on port 53; Internal Domains are tagged "do not intercept" and passed back to the OS network stack
- Non-internal domains are forwarded to Umbrella backend for allow/block decisions
- Customers can upgrade from Roaming Client to AnyConnect at no charge

## Prerequisites
- AnyConnect with Umbrella Module installed (not legacy Roaming Client)
- Access to Cisco Umbrella Management Console
- Knowledge of domains used by Twingate Resources (e.g., `*.example.com`)

## Step-by-Step Configuration

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add the domains corresponding to your Twingate Resources
   - Example: add `example.com` to cover `*.example.com`

## Configuration Values

| Setting | Location | Value |
|---|---|---|
| Internal Domains | Umbrella Console → Deployments → Configuration → Domain Management | Your Twingate resource domains (e.g., `example.com`) |

## Gotchas
- **Publicly resolvable domains** must still be added to Internal Domains — AnyConnect will otherwise intercept and forward them to Umbrella instead of letting Twingate resolve them
- **Wildcard syntax**: Left-hand wildcards only — `example.com` implicitly covers `*.example.com`; mid-field wildcards like `bla.*.example.com` are **not supported**
- Roaming Client stores resolver list at startup and never polls for OS-level changes — this is why it conflicts with Twingate (Twingate's resolver additions are ignored)
- Internal Domain tags are stored in memory and reset when AnyConnect restarts

## Related Docs
- [Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)
- Twingate: Split DNS / DNS configuration docs