---
source: https://github.com/Twingate/github-action
type: github
fetched: 2026-10-04
source_version: 358e205bb31e636fef1dfb706228ab60eb90c181
trust: official
---

# Twingate GitHub Action

GitHub Action that installs and starts the Twingate client on a runner to allow workflow steps to access private resources protected by Twingate. Supports Linux (x64/ARM) and Windows runners.

## Key Information

- Uses Twingate [Services](https://docs.twingate.com/docs/services) (service keys) for authentication, not user credentials
- Supports two use cases: direct access to private resources (e.g., VPC databases), and routing traffic through a Connector for IP-allowlisted SaaS apps
- Packages are cached by default; caching reduces install time by 30–45%
- Latest release (v1.11): fixes a setup abort caused by a trailing newline in service keys on Linux

## Prerequisites

- A Twingate account with a configured Service and a generated Service Key
- Service Key stored as a GitHub Actions secret

## Usage

```yaml
- uses: twingate/github-action@v1
  with:
    service-key: ${{ secrets.TWINGATE_SERVICE_KEY }}
```

## Configuration Values

| Input | Required | Default | Description |
|---|---|---|---|
| `service-key` | Yes | — | Twingate Service Key for authentication |
| `cache` | No | `true` | Cache downloaded packages between runs |
| `cache-version` | No | `3` | Increment to invalidate the package cache |
| `debug` | No | `false` | Enable verbose logging for troubleshooting |

## Gotchas

- **Docker steps on Azure-hosted runners**: Docker containers inherit `168.63.129.16` (Azure internal nameserver) in `/etc/resolv.conf`, which can override Twingate's DNS. Fix by running inside the container before DNS-dependent steps:
  ```bash
  sed '/^nameserver 168.63.129.16$/d; /^search/d' /etc/resolv.conf > /tmp/resolv.conf && cat /tmp/resolv.conf > /etc/resolv.conf
  ```
- Service keys with trailing newlines previously caused setup to abort on Linux (fixed in v1.11).
- `cache-version` must be manually incremented to force a fresh package download; there is no automatic invalidation on Twingate version changes.

## Related Docs

- [Twingate Services](https://docs.twingate.com/docs/services)
- [SaaS App Gating / IP Whitelisting](https://docs.twingate.com/docs/saas-app-gating)
- [Azure IP 168.63.129.16 explanation](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16)