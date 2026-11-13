---
source: https://github.com/Twingate/github-action
type: github
fetched: 2026-11-13
source_version: 05376965f4960039e9bd8823171315c574bfef31
trust: official
---

# Twingate GitHub Action

A GitHub Action that connects a workflow runner to Twingate using a Service Key, enabling access to private resources and IP-restricted services without granting broad network access.

## Key Information

- Supports Linux (x64/ARM) and Windows runners
- Uses Twingate [Services](https://docs.twingate.com/docs/services) for zero-trust automated access
- Packages are cached by default, reducing installation time by 30–45%
- Latest release: `v1.11` — fixes setup abort when service key ends with a newline

## Prerequisites

- A Twingate account with a configured Service and Service Key
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
| `service-key` | Yes | — | Twingate Service Key |
| `cache` | No | `true` | Cache downloaded packages |
| `cache-version` | No | `3` | Increment to invalidate cached packages |
| `debug` | No | `false` | Enable verbose debug logging |

## Gotchas

- **Docker steps requiring Twingate resources**: Containers on Azure-hosted runners inherit `168.63.129.16` as a nameserver in `/etc/resolv.conf`, which can override Twingate's DNS. Remove it inside the container, and add back the host's systemd-resolved stub (`127.0.0.53`) if no nameserver remains:
  ```sh
  sed '/^nameserver 168.63.129.16$/d; /^search/d' /etc/resolv.conf > /tmp/resolv.conf &&
  { grep -q '^nameserver' /tmp/resolv.conf || echo 'nameserver 127.0.0.53' >> /tmp/resolv.conf; } &&
  cat /tmp/resolv.conf > /etc/resolv.conf
  ```
  - `127.0.0.53` is only reachable when the container shares the host's network (`docker run --network host`), which is what this repository's CI tests.
  - On most GitHub-hosted runners `/etc/resolv.conf` is the systemd-resolved stub, so a `--network host` container gets `nameserver 127.0.0.53` and the `sed` removes nothing.
  - Some runners (seen in Azure `westus2`) have `/etc/resolv.conf` as a regular file (`resolv.conf mode: foreign`) listing `127.0.0.100`, `127.0.0.53` and `168.63.129.16`. Docker drops the loopback entries, leaving only `168.63.129.16`; removing it leaves no nameserver and all DNS lookups fail. Re-adding `127.0.0.53` routes lookups through the host's systemd-resolved and on to the Twingate Client.
- Service keys with trailing newlines are handled correctly as of `v1.11`; earlier versions may fail on Linux.
- To force a fresh package download, increment `cache-version` rather than disabling `cache` entirely.

## Related Docs

- [Twingate Services](https://docs.twingate.com/docs/services)
- [SaaS App Gating / IP Whitelisting](https://docs.twingate.com/docs/saas-app-gating)
- [Azure IP 168.63.129.16 explanation](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16)