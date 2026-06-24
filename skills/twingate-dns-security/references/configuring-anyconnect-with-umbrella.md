# Configuring AnyConnect with Umbrella

## Page Title
How to Configure AnyConnect with Umbrella

## Summary
AnyConnect with Umbrella Module is compatible with Twingate (unlike the legacy Roaming Client), but requires configuring Internal Domains in the Umbrella console to prevent AnyConnect from intercepting Twingate traffic. The key configuration step is adding your Twingate resource domains to the Internal Domains list so AnyConnect passes DNS resolution back to the OS/Twingate.

## Key Information
- **Roaming Client is incompatible** with Twingate; AnyConnect with Umbrella Module is fully compatible
- Roaming Client works via DNS resolver replacement (`127.0.0.1` loopback); does not detect OS resolver changes after startup
- AnyConnect uses a **kernel module** intercepting port 53 traffic — no OS resolver list modification required
- AnyConnect marks Internal Domain destinations as "do not intercept" in memory until client restart
- Customers can upgrade from Roaming Client to AnyConnect at no charge

## Prerequisites
- AnyConnect with Umbrella Module (not legacy Roaming Client)
- Access to Cisco Umbrella Management Console
- Knowledge of your Twingate resource domain(s)

## Step-by-Step Configuration

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add each domain used by your Twingate Resources
   - Example: add `example.com` to cover `*.example.com`

## Configuration Values

| Setting | Location | Value |
|---|---|---|
| Internal Domains | Umbrella Console → Deployments → Configuration → Domain Management | Your Twingate resource domains (e.g., `example.com`) |

## Gotchas
- **Wildcard support**: Left-hand wildcards only — `example.com` implicitly covers `*.example.com`. Midfield wildcards (`bla.*.example.com`) are **not supported**
- **Publicly resolvable domains**: Even if resources are publicly resolvable, they **must** be added to Internal Domains for Twingate to resolve them correctly
- AnyConnect's "do not intercept" tag is in-memory only and resets on client restart
- Roaming Client's resolver list is static after startup — incompatible with Twingate's DNS behavior

## Related Docs
- [Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)
- Cisco AnyConnect upgrade from Roaming Client (contact Cisco — free of charge)