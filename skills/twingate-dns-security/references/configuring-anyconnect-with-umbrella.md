# Configuring AnyConnect with Umbrella for Twingate

## Page Title
How to Configure AnyConnect with Umbrella

## Summary
Cisco's legacy Umbrella Roaming Client is incompatible with Twingate due to its static DNS resolver approach. AnyConnect with Umbrella Module uses a kernel-level DNS interceptor and **is fully compatible** with Twingate when Internal Domains are properly configured.

## Key Information
- **Roaming Client** (legacy): Incompatible with Twingate — captures DNS resolvers at startup into a static internal list, replacing first resolver with `127.0.0.1`
- **AnyConnect with Umbrella Module** (current): Compatible with Twingate — uses kernel module intercepting port 53 traffic directly
- AnyConnect marks known Internal Domains as "do not intercept" in memory until client restart
- Customers can upgrade from Roaming Client to AnyConnect for free

## Prerequisites
- AnyConnect Client with Umbrella Module (not legacy Roaming Client)
- Access to Cisco Umbrella Management Console
- Knowledge of your Twingate Resource domains (e.g., `*.example.com`)

## Step-by-Step Configuration

1. Open **Cisco Umbrella Management Console**
2. Navigate to **Deployments → Configuration → Domain Management**
3. Under **Internal Domains**, add your Twingate Resource domains
   - Example: add `example.com` (covers `*.example.com` implicitly)

## Configuration Values

| Setting | Location | Value |
|---|---|---|
| Internal Domains | Umbrella Console → Deployments → Configuration → Domain Management | Your Twingate resource domains (e.g., `example.com`) |

## Gotchas
- **Wildcard syntax**: AnyConnect does **not** support midfield wildcards (`bla.*.example.com` is invalid). Left-hand wildcards are implied — `example.com` automatically covers `*.example.com`
- **Publicly resolvable domains**: If Twingate-protected resources are publicly resolvable, they **must** still be added to Internal Domains list or AnyConnect will intercept/forward DNS to Umbrella instead
- **Roaming Client static resolver issue**: The Roaming Client does not poll the OS for resolver changes after startup — this is why it breaks Twingate and cannot be fixed via configuration
- AnyConnect's "do not intercept" tag is memory-only and resets on client restart

## Related Docs
- [Umbrella Domain Management](https://docs.umbrella.com/deployment-umbrella/docs/domain-management)
- Twingate Resources configuration (internal)