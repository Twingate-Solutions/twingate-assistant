# CI/CD Configuration - Twingate

## Summary
Provides sample configurations for integrating Twingate headless Client into CI/CD pipelines. Covers GitHub Actions (including a Marketplace action) and CircleCI. Configurations install the Twingate client, authenticate via Service Key, and connect to protected Resources.

## Key Information
- Public GitHub repository contains sample configs used in Twingate's own automated testing
- GitHub Marketplace action available: "Connect to Twingate"
- Supported base OS: Ubuntu (other Linux distros may not be compatible)
- Client runs in headless mode using a Service Key
- CircleCI requires Service Key to be base64-encoded due to variable storage requirements

## Prerequisites
- Twingate Service Key (stored as CI/CD secret)
- Ubuntu-based runner/machine
- Resources assigned to the Service account

## Step-by-Step

### GitHub Actions
1. Install Twingate via apt from `packages.twingate.com/apt/`
2. Pass `TWINGATE_SERVICE_KEY` secret via stdin: `echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-`
3. Start client: `sudo twingate start`
4. Run workflow steps accessing protected Resources
5. Stop client: `sudo twingate stop`

### CircleCI
1. Install Twingate via apt (also install `ca-certificates` first)
2. Decode base64 Service Key, pipe to setup: `echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-`
3. Start client: `sudo twingate start`
4. Run test steps
5. Stop client: `sudo twingate stop`

## Configuration Values

| Parameter | Usage |
|-----------|-------|
| `TWINGATE_SERVICE_KEY` | GitHub Actions secret containing raw Service Key |
| `SERVICE_KEY` | CircleCI env var containing **base64-encoded** Service Key |
| `TEST_URL` | CircleCI env var for the protected Resource URL |
| `--headless=-` | Flag to read Service Key from stdin |

**APT source:** `deb [trusted=yes] https://packages.twingate.com/apt/ /`

**CircleCI image:** `ubuntu:jammy-20250530`

## Gotchas
- CircleCI: Service Key **must be base64-encoded** in the env var; decode before passing to `twingate setup`
- GitHub Actions: Service Key passed as **raw value** (no base64 encoding needed)
- Linux Client may not be compatible with non-Ubuntu distributions
- Image/version references in docs may not reflect latest available versions — check official sources

## Debugging Commands
```bash
twingate status
journalctl -u twingate --no-pager | tail -n 20
```

## Related Docs
- Twingate headless Client documentation
- Twingate Services documentation
- [GitHub Marketplace Action](https://github.com/marketplace) - "Connect to Twingate"
- [Sample configs repo](https://github.com/Twingate) (public GitHub repository)