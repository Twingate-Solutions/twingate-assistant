# Configuring AnyConnect with Umbrella for Twingate

## Page Title
How to Configure AnyConnect with Umbrella

## Summary
Cisco's Umbrella Roaming Client is incompatible with Twingate due to its static DNS resolver capture method. AnyConnect with Umbrella Module (the replacement) is fully compatible but requires adding Twingate resource domains to the Internal Domains list in the Umbrella console.

## Key Information
- **Roaming Client** (legacy): Captures OS resolver list at startup, replaces first resolver with `127.0.0.1` loopback — **incompatible with Twingate**
- **AnyConnect with Umbrella Module** (current): Uses kernel module intercepting port 53 traffic — **compatible with Twingate**
- Roaming Client → AnyConnect upgrade is free for existing Cisco customers
- AnyConnect caches "do not intercept" tags in memory until client restart

## Prerequisites
- AnyConnect with Umbrella Module (not legacy Roaming Client)
- Access to Cisco Umbrella Management Console
- Known domain patterns for Twingate-protected resources

## Step-by-Step Configuration

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add each Twingate resource domain (e.g., `example.com`)
4. Repeat for all domains corresponding to Twingate Resources

## Configuration Values

| Setting | Location | Value |
|---|---|---|
| Internal Domains | Umbrella Console → Deployments → Configuration → Domain Management | e.g., `example.com` |

## Gotchas
- **Publicly resolvable domains must also be added** to Internal Domains — AnyConnect will intercept them otherwise
- **No midfield wildcards**: `bla.*.example.com` is invalid
- **Left-hand wildcards are implied**: `example.com` automatically covers `*.example.com`
- Roaming Client does **not** poll OS for resolver changes after startup — static list only
- AnyConnect's "do not intercept" tags reset on client restart

## Related Docs
- [Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)
- Twingate: Roaming Client incompatibility is a hard block — migration to AnyConnect required