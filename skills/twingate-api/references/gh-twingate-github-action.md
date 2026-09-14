---
source: https://github.com/Twingate/github-action
type: github
fetched: 2026-09-13
source_version: 7a7f18087d4bf841d7bced88bc877ecef1b1233b
---

# Twingate Connect — GitHub Action

## Summary
A GitHub Action that connects workflows to private resources via Twingate Services using zero-trust network access. It installs and starts the Twingate client on the runner, authenticating with a Service Key. Supports both direct private resource access and IP-allowlist bypass scenarios.

## Key Information
- **Repo:** `Twingate/github-action`
- **Latest version:** `v1.8`
- **Supported runners:** Linux (x64/ARM), Windows
- **Auth mechanism:** Twingate Service Key (not user credentials)
- Caching reduces installation time by 30–45%

## Prerequisites
- A Twingate account with a configured [Service](https://docs.twingate.com/docs/services)
- A Service Key stored as a GitHub Actions secret
- Runner must support `NET_ADMIN` capability and `/dev/net/tun` device (for local testing with `act`)

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
| `cache-version` | No | `3` | Increment to invalidate existing cache |
| `debug` | No | `false` | Enable verbose logging |

## Gotchas

**Docker container steps and DNS resolution**
When a workflow step runs inside a Docker container, Azure injects `168.63.129.16` into the container's `resolv.conf`. This can override Twingate's DNS and break resource resolution. Fix by removing it inside the container:

```bash
sed '/^nameserver 168.63.129.16$/d; /^search/d' /etc/resolv.conf \
  > /tmp/resolv.conf && cat /tmp/resolv.conf > /etc/resolv.conf
```

**Local testing with `act`**
Requires additional Linux capabilities:
```bash
act -j test -s SERVICE_KEY --container-options "--cap-add NET_ADMIN --device /dev/net/tun"
```

**Cache invalidation**
Increment `cache-version` (e.g., `3` → `4`) to force a fresh package download; do not rely on disabling `cache` alone for this purpose.

**IP allowlisting use case**
Requires a Twingate Connector configured to route `github.com` traffic. See [SaaS app gating docs](https://docs.twingate.com/docs/saas-app-gating).

## Related Docs
- [Twingate Services](https://docs.twingate.com/docs/services)
- [SaaS App Gating / IP Allowlisting](https://docs.twingate.com/docs/saas-app-gating)
- [Azure IP 168.63.129.16 explained](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16)