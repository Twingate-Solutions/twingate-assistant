## DNS-over-HTTPS (DoH) Configuration

Reference for Twingate's native DoH support -- what it does, how it behaves, fallback methods, and per-Group exceptions.

### Platform Support

- **macOS, Windows, Linux** Clients only
- Mobile Clients (iOS, Android) NOT supported

### How It Works

When DoH is enabled:
1. User signs in to the Twingate Client -> Client receives DoH config from server
2. If DoH is enabled for the account AND user is not in a DoH exception Group -> Client enables DoH
3. All DNS A queries (not destined for a Twingate Resource) get encapsulated in DoH and sent to the configured resolver
4. Twingate Resource queries are **not** sent to the DoH resolver -- they're handled by Twingate's internal resolver

**IPv6 Note**: AAAA (IPv6) queries are NOT supported. Local resolution falls back to IPv4 before being encapsulated in DoH.

**Sign-In Requirement**: DoH activates when the Client connects. With /docs/internet-security-client-configuration, DoH can run pre-sign-in via Machine Key.

### Configuration (Admin Console -> Internet Security -> Secure DNS)

| Setting | Options |
|---|---|
| **Enable DoH** | On / Off (off by default) |
| **DoH Resolver** | Pre-configured public resolvers OR custom URL |
| **Fallback Method** | Strict (never fall back) / Automatic (fall back to system DNS on failure) |
| **Exception Groups** | Groups whose users will NOT receive DoH config |

### DoH Resolver Options

**Pre-configured public resolvers** (Cloudflare, Google, NextDNS profiles, etc.) -- lowest-friction option.

**Custom DoH URL** -- for:
- Private/internal DoH resolvers
- DNS filtering services like NextDNS / Cloudflare Zero Trust

**Important**: Twingate validates only that the URL is HTTPS -- not that it's a working DoH endpoint. **Bad URL + Strict mode = all DNS fails for users**.

### Custom DoH Template Fields

Inject device-specific info into the resolver URL via template variables:

| Variable | Example Value |
|---|---|
| `${deviceName}` | Alex's MacBook Pro |
| `${deviceId}` | (Twingate device ID) |
| `${deviceModel}` | MacBook Pro (16-inch, M1 Pro, Late 2021) |
| `${deviceHostname}` | alexs-macbook-pro.local |
| `${userEmail}` | alex@company.com |

Example custom URL:
```
https://doh.example/query?deviceHostname=${deviceHostname}
```

Useful for per-device attribution at the DoH resolver / DNS filter service.

### DoH as a Resource

If your DoH resolver's domain matches a Twingate Resource, DoH traffic routes **through that Resource** (i.e., over Twingate to the Connector). Useful for private DoH resolvers reachable only inside your network.

**Client version requirements:**
- macOS 2024.311+
- Windows 2024.351+
- Linux 2024.331+

**Wildcard Resource matching is supported.**

**CRITICAL**: DoH-as-Resource Resources MUST have a **Device-only Resource Policy** (per /docs/device-only-resource-policies). Otherwise users can't authenticate (chicken-and-egg: can't reach DoH to do DNS to authenticate).

### Fallback Methods

| Mode | Behavior |
|---|---|
| **Strict** | Never fall back. If DoH is unavailable, ALL DNS fails -- including private DNS that public resolvers can't answer |
| **Automatic** (default) | Fall back to regular DNS if DoH resolver fails or returns no answer |

**Recommendation**: use Automatic unless you have a specific compliance need for Strict (and have tested extensively).

### Exception Groups

Any user in an Exception Group bypasses DoH entirely (uses system DNS). Useful for:
- Contractor groups whose machines aren't expected to support DoH
- Special-case workloads / debugging

If a user is in **multiple Groups, any one being an Exception Group** disables DoH for them.

### Decision Notes

- **For most deployments**: enable DoH with Automatic fallback + a public resolver (Cloudflare, Google, or Twingate-native filtering)
- **For compliance**: Strict + a custom enterprise DoH resolver may be required -- test thoroughly first
- **For per-device DNS analytics**: use the template fields with NextDNS or a custom resolver that ingests them

### Gotchas

- Bad custom DoH URL + Strict mode = catastrophic; always test with Automatic first
- AAAA queries unsupported -- some IPv6-heavy workflows may behave unexpectedly
- Private DoH (DoH-as-Resource) without device-only policy = lockout
- Fallback in Automatic mode is silent -- monitor logs to confirm DoH is actually being used

### Related Docs

- /docs/internet-security -- IS overview
- /docs/dns-filtering -- Filtering on top of DoH
- /docs/internet-security-client-configuration -- Always-on DoH via Machine Key
- /docs/nextdns-configuration, /docs/doh-cloudflare -- Custom DoH resolver patterns
- /docs/device-only-resource-policies -- Required for DoH-as-Resource
