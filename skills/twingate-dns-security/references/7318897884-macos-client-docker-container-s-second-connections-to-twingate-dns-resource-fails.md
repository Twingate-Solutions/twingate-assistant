---
source: https://help.twingate.com/articles/7318897884-macos-client-docker-container-s-second-connections-to-twingate-dns-resource-fails
type: help
fetched: 2026-09-06
source_version: 08213d864f9e77ba35472b171ca361fa9734516aa4a7f8616127b5b2348b0682
---

# macOS Client: Docker Container Second Connections to Twingate DNS Resource Fail

## Summary
On macOS, Docker containers can connect to Twingate DNS resources on the first attempt but fail on subsequent attempts. The root cause is that Docker containers switch away from Twingate resolvers after the first DNS query, returning non-CGNAT IPs instead of Twingate-assigned CGNAT addresses.

## Key Information
- **Affected components**: Twingate Client (macOS) + Docker for Mac
- **Symptom**: First connection succeeds; all subsequent connections fail
- **Root cause**: Container uses correct Twingate resolver (returns CGNAT IP `100.x.x.x`) on first query, then falls back to different resolvers returning real IPs on subsequent queries
- Docker's internal DNS (`192.168.65.5`) does not consistently forward to Twingate resolvers

## Prerequisites
- Twingate Client running on macOS host
- Docker for Mac installed
- Access to Twingate-protected DNS resource

## Diagnosis
Run `nslookup` or `dig` inside the container twice and compare results:

**First query (correct)** — returns CGNAT IP:
```
Server: 192.168.65.5
Address: 100.98.196.176  ← CGNAT range, Twingate-assigned
```

**Second query (broken)** — returns real IP:
```
Server: 192.168.65.5
Address: 10.140.140.65  ← non-CGNAT, bypasses Twingate
```

## Resolution

Add explicit DNS flags to the `docker run` command to force the container to use Twingate resolvers:

```bash
docker run --dns=100.95.0.251 --dns=100.95.0.252 --dns=100.95.0.253 --dns=100.95.0.254 <image>
```

## Configuration Values

| Flag | Value |
|------|-------|
| `--dns` (primary) | `100.95.0.251` |
| `--dns` (secondary) | `100.95.0.252` |
| `--dns` (tertiary) | `100.95.0.253` |
| `--dns` (quaternary) | `100.95.0.254` |

## Gotchas
- All four Twingate resolver IPs should be specified; omitting them risks fallback behavior
- This issue is specific to **Docker for Mac** — the macOS host client does not exhibit this behavior directly
- Using `docker-compose`, add a `dns:` block under the service definition instead of CLI flags

## Related Docs
- Twingate DNS resource configuration
- Docker networking documentation (`--dns` flag)