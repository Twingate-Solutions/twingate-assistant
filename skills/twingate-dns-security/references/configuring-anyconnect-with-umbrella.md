---
source: https://www.twingate.com/docs/configuring-anyconnect-with-umbrella
type: docs
fetched: 2026-08-14
source_version: e9b2d4d377c4b00ced7b95718ef0b53cc7cac76d9f6fe4295cfd2abf08e3877e
---

# Configuring AnyConnect with Umbrella

## Summary
AnyConnect with Umbrella Module is compatible with Twingate, unlike the legacy Umbrella Roaming Client which is incompatible. Configuration requires adding Twingate resource domains to AnyConnect's Internal Domains list to prevent traffic interception. The Roaming Client should be replaced with AnyConnect for any Twingate deployment.

## Key Information
- **Roaming Client** = legacy, incompatible with Twingate; replaced by AnyConnect with Umbrella Module
- **AnyConnect with Umbrella Module** = fully compatible with Twingate
- Upgrade from Roaming Client to AnyConnect is free of charge
- Roaming Client conflict: modifies OS DNS resolver list to `127.0.0.1` at startup, never re-polls for changes — Twingate DNS changes are ignored
- AnyConnect uses a **kernel module** intercepting port 53 traffic — no OS resolver list modification

## Prerequisites
- AnyConnect with Umbrella Module installed (not Roaming Client)
- Access to Cisco Umbrella Management Console
- Knowledge of Twingate resource domains (e.g., `*.example.com`)

## Step-by-Step: Configure Internal Domains

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add each Twingate resource domain
   - Example: add `example.com` to cover all `*.example.com` resources

## Configuration Values

| Setting | Location | Value |
|---|---|---|
| Internal Domains | Umbrella Console → Deployments → Configuration → Domain Management | Your Twingate resource domains (e.g., `example.com`) |

## Wildcard Syntax Rules
- ✅ Supported: Left-hand wildcards — `example.com` implies `*.example.com`
- ❌ Not supported: Midfield wildcards — `bla.*.example.com` is invalid

## Gotchas
- **Publicly resolvable domains**: Must still be added to Internal Domains list — AnyConnect will otherwise forward DNS to Umbrella backend instead of letting Twingate resolve them
- **Roaming Client is not compatible** with Twingate under any configuration — must migrate to AnyConnect
- AnyConnect's "do not intercept" tag is **in-memory only** and clears on restart
- Internal Domain entries are permanent for the session; AnyConnect does not re-evaluate after tagging

## How AnyConnect Processes DNS (Decision Flow)
1. Kernel module intercepts all outgoing port 53 traffic
2. If destination matches **Internal Domain** → passes back to OS network stack (Twingate handles it)
3. If destination is **unknown** → forwarded to Umbrella backend for allow/block decision

## Related Docs
- [Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)
- Twingate: Roaming Client incompatibility is inherent — no workaround exists; migration required