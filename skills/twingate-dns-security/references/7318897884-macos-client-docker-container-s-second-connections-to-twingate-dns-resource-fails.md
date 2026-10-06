---
source: https://help.twingate.com/articles/7318897884-macos-client-docker-container-s-second-connections-to-twingate-dns-resource-fails
type: help
fetched: 2026-10-04
source_version: a57a9dded0adf534b026a171d9e1c87317de34d7e003a573fe00a613574f39eb
trust: official
---

# macOS Client: Docker Container Second Connections to Twingate DNS Resource Fails

## Summary
On macOS with Twingate Client running, Docker containers can connect to Twingate DNS resources on the first attempt but fail on subsequent attempts. The root cause is that Docker switches away from Twingate resolvers after the first DNS query, returning a non-CGNAT IP instead of the expected CGNAT address.

## Key Information
- First connection succeeds because Docker uses Twingate resolvers (returns CGNAT IP in `100.x.x.x` range)
- Subsequent connections fail because Docker uses different resolvers (returns non-CGNAT IP, e.g. `10.x.x.x`)
- Docker for Mac uses `192.168.65.5` as its internal DNS by default, which does not consistently forward to Twingate resolvers

## Prerequisites
- Twingate Client running on macOS host
- Docker for Mac installed
- Container attempting to reach a Twingate-protected DNS resource

## Diagnostic Steps
1. Run first DNS lookup inside container — expect CGNAT IP (`100.x.x.x`):
   ```
   nslookup <twingate_resource> 
   # Returns: Address: 100.98.x.x  ← correct
   ```
2. Run second DNS lookup — if broken, returns non-CGNAT IP:
   ```
   nslookup <twingate_resource>
   # Returns: Address: 10.x.x.x  ← incorrect
   ```

## Resolution

Add explicit Twingate DNS resolver flags to your `docker run` command:

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

These are Twingate's CGNAT resolver addresses and must be set explicitly to bypass Docker's default resolver behavior.

## Gotchas
- All four DNS entries should be specified for redundancy
- This affects Docker for Mac specifically; behavior may differ on Linux Docker hosts
- The issue is intermittent/progressive — first connection masking the problem can delay diagnosis
- Docker Compose users should add a `dns:` block under the service definition instead of CLI flags

## Related Docs
- Twingate DNS resource configuration
- Docker `--dns` flag documentation: [docs.docker.com](https://docs.docker.com)