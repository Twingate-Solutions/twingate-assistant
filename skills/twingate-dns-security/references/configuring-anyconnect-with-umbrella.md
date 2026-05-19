# Configuring AnyConnect with Umbrella for Twingate

## Summary
AnyConnect with Umbrella Module is compatible with Twingate, unlike the legacy Umbrella Roaming Client. Configuration requires adding Twingate resource domains to AnyConnect's Internal Domains list to prevent traffic interception.

## Key Information
- **Roaming Client** (legacy) is **incompatible** with Twingate Client
- **AnyConnect with Umbrella Module** is **fully compatible** with Twingate
- Umbrella Roaming Client → AnyConnect upgrade is free for existing Cisco customers
- AnyConnect operates at kernel level, intercepting port 53 traffic without modifying OS resolver list

## How Each Works

**Roaming Client (incompatible):**
- Replaces first DNS resolver with `127.0.0.1` loopback at startup
- Stores static resolver list internally; does not poll OS for changes
- Static resolver list causes conflict with Twingate Client

**AnyConnect with Umbrella Module (compatible):**
- Uses kernel module to intercept all outgoing port 53 traffic
- Does not modify OS resolver list
- Routes DNS to Umbrella backend unless domain matches Internal Domains list
- Internal Domains bypass Umbrella and return to OS network stack

## Prerequisites
- AnyConnect with Umbrella Module installed (not legacy Roaming Client)
- Access to Cisco Umbrella Management Console
- Knowledge of domain names used by Twingate Resources

## Step-by-Step Configuration

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add each domain used by Twingate Resources
   - Example: add `example.com` to cover `*.example.com`

## Configuration Values

| Setting | Value | Notes |
|---|---|---|
| Internal Domain entry | `example.com` | Covers all subdomains implicitly |
| Wildcard support | Left-hand only | `*.example.com` implied by `example.com` |
| Unsupported format | `bla.*.example.com` | Midfield wildcards not supported |

## Gotchas

- **Publicly resolvable domains** must still be added to Internal Domains list — AnyConnect will otherwise intercept and forward to Umbrella instead of letting Twingate resolve them
- **No midfield wildcards**: `bla.*.example.com` is invalid; only left-hand wildcards work
- `example.com` and `*.example.com` are treated as equivalent
- AnyConnect's "do not intercept" tag is **in-memory only** — cleared on client restart
- Roaming Client's static resolver list is captured at startup only; OS-level resolver changes are ignored (root cause of Twingate incompatibility)

## Related Docs
- [Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)
- Cisco AnyConnect with Umbrella Module upgrade path (contact Cisco for Roaming Client migration)