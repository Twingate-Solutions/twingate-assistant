# CI/CD Configuration for Twingate Headless Client

## Summary
Provides sample configurations for integrating the Twingate headless Client into CI/CD pipelines using a Service Key. Covers GitHub Actions (via Marketplace action) and CircleCI. Configurations are included in Twingate's public GitHub repository and automated testing.

## Key Information
- GitHub Marketplace Action available: "Connect to Twingate"
- Headless client runs on Ubuntu; **may not be compatible with other Linux distributions**
- Service Key must be pre-configured as a CI/CD secret
- CircleCI requires Service Key to be **base64 encoded** due to variable storage requirements

## Prerequisites
- Twingate Service Key (configured as a secret in your CI/CD platform)
- Ubuntu-based runner/machine image
- Resources assigned to the Service account

## GitHub Actions — Step-by-Step

1. **Install Twingate** via apt from `packages.twingate.com/apt/`
2. **Setup**: pipe `$TWINGATE_SERVICE_KEY` into `sudo twingate setup --headless=-`
3. **Start**: `sudo twingate start`
4. **Run workflow steps** accessing protected Resources
5. **Stop**: `sudo twingate stop`

## CircleCI — Step-by-Step

1. **Install** `ca-certificates` then Twingate via apt
2. **Decode and setup**: `echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-`
3. **Start**: `sudo twingate start`
4. **Test** protected and public resources via `curl`
5. **Stop**: `sudo twingate stop`

## Configuration Values

| Parameter | Value/Notes |
|---|---|
| `TWINGATE_SERVICE_KEY` | GitHub Actions secret name |
| `SERVICE_KEY` | CircleCI env var (must be base64 encoded) |
| APT repo | `deb [trusted=yes] https://packages.twingate.com/apt/ /` |
| `--headless=-` | Reads service key from stdin |
| CircleCI image | `ubuntu:jammy-20250530` |

## Useful Debug Commands
```bash
twingate status
journalctl -u twingate --no-pager | tail -n 20
```

## Gotchas
- CircleCI: Service Key **must be base64 encoded** when stored; decode before passing to `twingate setup`
- Linux Client compatibility is **not guaranteed** outside Ubuntu
- Image/version references in docs may not reflect latest available — check official sources
- These are guide examples, not hardened production configs; apply security best practices before production use

## Related Docs
- [Headless Client / Services documentation](https://www.twingate.com/docs/services)
- [Twingate GitHub Actions Marketplace](https://github.com/marketplace)
- [Public sample repository](https://github.com/Twingate) (referenced but not linked)