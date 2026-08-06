---
source: https://github.com/Twingate/github-action
type: github
fetched: 2026-08-06
source_version: bedc3e96674162a12a1222f3cecfa62945e59dc5
---

<!-- triage: unassigned -->

# Twingate/github-action

## Summary
A GitHub Action that connects GitHub workflow runners to private resources via Twingate Services using zero-trust network access. It installs and starts the Twingate client on the runner using a Service Key, enabling access to IP-restricted or privately networked resources without granting broad network access.

## Key Information
- Supports Linux (x64/ARM) and Windows runners
- Uses Twingate Service Keys (not user credentials) for authentication
- Packages are cached by default, reducing install time by 30–45%
- Major version tag (`v1`) always points to the latest release

## Prerequisites
- A Twingate account with a configured [Service](https://docs.twingate.com/docs/services)
- A Service Key stored as a GitHub Actions secret
- Runner must support `NET_ADMIN` capability and `/dev/net/tun` (for local testing with `act`)

## Usage

```yaml
- uses: twingate/github-action@v1
  with:
    service-key: ${{ secrets.TWINGATE_SERVICE_KEY }}
```

Place this step before any steps that require access to Twingate-protected resources.

## Configuration Values

| Input | Required | Default | Description |
|---|---|---|---|
| `service-key` | Yes | — | Twingate Service Key for authentication |
| `cache` | No | `true` | Cache downloaded packages between runs |
| `cache-version` | No | `3` | Increment to invalidate existing cache |
| `debug` | No | `false` | Enable verbose logging for troubleshooting |

## Gotchas

- **Docker steps on Azure runners**: Containers inherit `resolv.conf` with Azure's internal nameserver (`168.63.129.16`), which can override Twingate's DNS. Remove it inside the container before making requests:
  ```bash
  sed '/^nameserver 168.63.129.16$/d; /^search/d' /etc/resolv.conf > /tmp/resolv.conf && cat /tmp/resolv.conf > /etc/resolv.conf
  ```
- **IP whitelisting workflows**: Routing `github.com` traffic through Twingate requires a Connector configured for that purpose — not automatic.
- **Cache invalidation**: Bump `cache-version` if you encounter stale or corrupt cached packages.
- **Local testing**: Requires `act` with `--cap-add NET_ADMIN --device /dev/net/tun` flags.

## Related Docs
- [Twingate Services](https://docs.twingate.com/docs/services)
- [SaaS App Gating / IP Whitelisting](https://docs.twingate.com/docs/saas-app-gating)
- [Azure IP 168.63.129.16 explanation](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16)