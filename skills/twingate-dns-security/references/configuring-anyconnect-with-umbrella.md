## Configuring Cisco AnyConnect with Umbrella + Twingate

How to make Cisco AnyConnect (with Umbrella Module) coexist with the Twingate Client. The legacy **Umbrella Roaming Client** is **incompatible** with Twingate; AnyConnect with Umbrella Module **is compatible** with proper config.

### Roaming Client vs. AnyConnect — What's What

- **Umbrella Roaming Client** = Cisco's legacy DNS filtering agent (deprecated; no new development)
- **AnyConnect with Umbrella Module** = Cisco's current generation; replaces Roaming Client (free upgrade for existing customers)

### Why the Roaming Client Is Incompatible with Twingate

The Roaming Client (R.C.):
1. On startup, snapshots the OS DNS resolver list into an internal config
2. Replaces the first OS resolver with **127.0.0.1** (loopback)
3. Routes all DNS through its local proxy -> Umbrella backend for filter decision
4. Does **not poll the OS** for resolver changes -- the snapshot is static

When Twingate adds its own resolver (for private DNS resolution), the R.C. doesn't pick it up. As a result, **the Twingate Client cannot work alongside the Umbrella Roaming Client**.

### Why AnyConnect with Umbrella Module Works

AnyConnect operates differently:
1. Uses a **kernel module** to intercept DNS traffic (port 53) at the network stack level
2. Does NOT touch the OS resolver list
3. Does NOT cache an internal resolver list
4. For each DNS request:
   - If the destination matches a configured **Internal Domain** -> request returns to the OS network stack as-if-untouched
   - Otherwise -> sent to Umbrella backend for filter decision

This kernel-level interception is compatible with Twingate's resolver behavior.

### Configuration Required: Internal Domains

To prevent AnyConnect from intercepting Twingate-resolved domains, add them to AnyConnect's **Internal Domains** list.

**Steps in Cisco Umbrella Management Console:**

1. **Deployments -> Configuration -> Domain Management**
2. Under **Internal Domains**, add the domain(s) Twingate resolves
   - Example: if your Twingate Resources include `*.example.com`, add `example.com`
3. Save

### Wildcard Behavior

- **Mid-field wildcards NOT supported**: `bla.*.example.com` is **invalid**
- **Left-hand wildcards are implicit**: adding `example.com` is equivalent to `*.example.com`

So most patterns (`*.acme.internal`, `*.corp.example.com`) just need the base domain entered.

### Important: Publicly Resolvable Domains

If Twingate Resources have addresses that are **publicly resolvable** (e.g., `app.public.example.com` is in public DNS but you want Twingate to handle it), you **must** add them to Internal Domains -- otherwise Umbrella will resolve them publicly and bypass Twingate.

### Decision Notes

- **For new deployments**: never use the Roaming Client; only AnyConnect with Umbrella Module
- **For migrations from Roaming Client**: upgrade to AnyConnect first, then deploy Twingate
- Audit your Twingate Resource list and ensure every private domain pattern is in AnyConnect's Internal Domains
- Test thoroughly: a single missed pattern can cause flaky behavior where some lookups go through Twingate and others don't

### Gotchas

- The "left-hand wildcard implicit" semantics is non-obvious -- experiment with subdomain coverage to confirm
- AnyConnect's Internal Domain tagging is **in-memory and persists until restart** -- after policy changes, restart the AnyConnect Client on test machines
- The Roaming Client is silently incompatible -- users may not see clear errors, just intermittent failures

### Related Docs

- /docs/configuring-zscaler-with-twingate -- Sibling pattern for Zscaler
- /docs/netskope-dlp-config -- Netskope coexistence
- /docs/dns-ultimate-guide -- DNS in Twingate
- /docs/private-dns-best-practices -- Private DNS Resource patterns
