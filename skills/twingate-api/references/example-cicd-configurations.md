---
source: https://www.twingate.com/docs/example-cicd-configurations
type: docs
fetched: 2026-08-14
source_version: 9d53780d56bb0d1bb698c63183f9b9371202c0d5522f5e36da2b06c97c9825b0
---

# CI/CD Configurations for Twingate

## Summary
Provides sample configurations for integrating Twingate headless Client into CI/CD pipelines. Covers GitHub Actions (via Marketplace action) and CircleCI. Configurations install, configure, and start the Twingate Client using a Service Key to access protected Resources.

## Key Information
- Sample configs are maintained in a public GitHub repository and included in automated testing
- A published GitHub Marketplace Action ("Connect to Twingate") simplifies GitHub workflow integration
- Headless Client requires a Twingate Service Key (not user credentials)
- Base OS must be Ubuntu; Linux Client may not be compatible with other distributions

## Prerequisites
- Twingate Service Account with a generated Service Key
- Resources assigned to the Service Account
- Ubuntu-based runner/machine image
- Service Key stored as a secret in your CI/CD platform

## GitHub Actions Configuration

```yaml
# Install
echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list
sudo apt update -yq && sudo apt install -yq twingate

# Setup & start
echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-
sudo twingate start

# Stop
sudo twingate stop
```

**Secret:** `SERVICE_KEY` → referenced as `secrets.SERVICE_KEY`

## CircleCI Configuration

```yaml
machine:
  image: ubuntu:jammy-20250530
```

```bash
# Install
echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list
sudo apt update -yq && sudo apt install -yq twingate

# Setup (base64 decode required for CircleCI)
echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-
sudo twingate start

# Stop
sudo twingate stop
```

**CircleCI-specific:** `$SERVICE_KEY` must be stored **base64-encoded** due to CircleCI variable storage requirements; decode before passing to `twingate setup`.

## Configuration Values

| Parameter | Description |
|---|---|
| `TWINGATE_SERVICE_KEY` | Service Key for headless auth (GitHub Actions) |
| `SERVICE_KEY` | Base64-encoded Service Key (CircleCI) |
| `--headless=-` | Flag to read Service Key from stdin |

## Gotchas
- CircleCI requires the Service Key to be **base64-encoded** in variable storage — must decode with `base64 --decode` before piping to `twingate setup`
- Only Ubuntu is officially supported; other Linux distros may not be compatible
- Image versions in samples may not be latest — verify against official docs
- These are guides only; apply security best practices before production use

## Related Docs
- [Twingate Headless Client](https://www.twingate.com/docs/headless-client)
- [GitHub Marketplace Action: Connect to Twingate](https://github.com/marketplace)
- [Twingate Services](https://www.twingate.com/docs/services)
- [Sample configs GitHub repository](https://github.com/Twingate)