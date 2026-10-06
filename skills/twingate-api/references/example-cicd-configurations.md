---
source: https://www.twingate.com/docs/example-cicd-configurations
type: docs
fetched: 2026-10-04
source_version: 38482f1b848b6f01a49ef49f5cb23d6f879641efda416cdf25c449879b674311
trust: official
---

# CI/CD Configuration Examples

## Page Title
Example CI/CD Configurations for Twingate Headless Client

## Summary
Provides sample CI/CD pipeline configurations for integrating Twingate's headless Client using a Service Key. Covers GitHub Actions (via Marketplace action) and CircleCI. Configurations connect a runner to Twingate-protected Resources during pipeline execution.

## Key Information
- Official GitHub Action available on GitHub Marketplace: "Connect to Twingate"
- Sample configs maintained in a public GitHub repository with automated testing
- Headless Client requires a **Service Key** (not user credentials)
- Base OS must be Ubuntu/Debian (apt-based); other Linux distros may be incompatible
- CircleCI requires the Service Key to be **base64-encoded** when stored as a variable, then decoded before use

## Prerequisites
- Twingate Service Key created and assigned to relevant Resources
- Service Key stored as a CI/CD secret (`SERVICE_KEY`)
- Ubuntu/Debian-based runner environment
- Resources configured in Twingate admin console

## Step-by-Step (Both Platforms)

1. **Install Twingate** — Add apt source and install package
2. **Setup** — Pipe Service Key into `twingate setup --headless=-`
3. **Start** — Run `sudo twingate start`
4. **Use Resources** — Execute pipeline steps requiring protected Resources
5. **Stop** — Run `sudo twingate stop` at end of job

## Configuration Values

### GitHub Actions
```yaml
env:
  TWINGATE_SERVICE_KEY: ${{ secrets.SERVICE_KEY }}
run: |
  echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-
  sudo twingate start
```

### CircleCI
```yaml
# SERVICE_KEY stored as base64-encoded env var
echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-
sudo twingate start
```

### APT Install (both platforms)
```
echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list
sudo apt update -yq && sudo apt install -yq twingate
```

### Useful CLI Commands
| Command | Purpose |
|---|---|
| `twingate status` | Check connection state |
| `journalctl -u twingate` | View logs |
| `sudo twingate stop` | Disconnect |

## Gotchas
- **CircleCI base64 requirement**: Service Key must be base64-encoded in CircleCI environment variables; raw key will fail
- **OS compatibility**: Only Ubuntu/Debian confirmed supported; other distros may not work
- **Image versions**: Code samples may reference outdated Ubuntu image tags (e.g., `ubuntu:jammy-20250530`); check CircleCI docs for current images
- **Production use**: Samples are guides only; apply your own security hardening before production deployment
- The `--headless=-` flag tells `twingate setup` to read the key from stdin (the pipe)

## Related Docs
- [Twingate Headless Client documentation](https://www.twingate.com/docs/headless-clients)
- [GitHub Marketplace Action: "Connect to Twingate"](https://github.com/marketplace)
- [Twingate Services (Service Accounts)](https://www.twingate.com/docs/services)