---
source: https://help.twingate.com/articles/7318897884-macos-client-docker-container-s-second-connections-to-twingate-dns-resource-fails
type: help
fetched: 2026-08-06
source_version: 9ca49c9f5b31189f52a5a79e3cfb7be29a4d6c9981250ecf5d63312b6d4c26b1
---

# macOS Client: Docker Container Second Connections to Twingate DNS Resource Fails

## Summary
On macOS, Docker containers can connect to Twingate DNS resources on the first attempt but fail on subsequent attempts. The root cause is that Docker containers switch DNS resolvers after the first query, returning non-CGNAT IPs instead of Twingate-assigned CGNAT IPs.

## Key Information
- **Affected components**: Twingate Client on macOS host + Docker for Mac containers
- **Symptom**: First connection succeeds; subsequent connections fail
- **Root cause**: Container uses Twingate resolvers on first DNS query, then falls back to different resolvers that return the real (non-CGNAT) IP
- **First query**: Returns CGNAT IP (e.g., `100.98.196.176`) — correct
- **Subsequent queries**: Returns non-CGNAT IP (e.g., `10.140.140.65`) — incorrect

## Prerequisites
- Twingate Client running on macOS host
- Docker for Mac installed
- Container attempting to reach a Twingate-protected DNS resource

## Fix: Force Twingate DNS Resolvers at Container Start

Add `--dns` flags to the `docker run` command to pin the container to Twingate resolvers:

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

## Diagnostics

Run inside the container to verify which resolver is responding and what IP is returned:

```bash
nslookup <twingate_resource>
# or
dig <twingate_resource>
```
- ✅ Correct: Server returns a CGNAT IP (`100.x.x.x`)
- ❌ Incorrect: Server returns a private/non-CGNAT IP (`10.x.x.x`, `172.x.x.x`, `192.168.x.x`)

## Gotchas
- This is macOS-specific due to Docker for Mac's networking architecture (containers run in a Linux VM, not directly on the host network)
- The `--dns` flags must be specified at container start; they cannot be applied to a running container
- If using Docker Compose, add the `dns:` key under the service definition instead of CLI flags

## Related Docs
- Twingate DNS resource configuration
- Docker for Mac networking documentation