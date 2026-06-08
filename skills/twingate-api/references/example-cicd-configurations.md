# CI/CD Configurations for Twingate

## Summary
Provides sample configurations for integrating Twingate headless Client into CI/CD pipelines using GitHub Actions and CircleCI. Configurations install the Twingate Client, authenticate via a Service Key, and enable access to protected Resources during pipeline execution.

## Key Information
- Sample configs available in a public GitHub repository and included in Twingate's automated testing
- Official GitHub Marketplace Action: "Connect to Twingate" available for direct use in workflows
- Supported platform: Ubuntu (Linux Client may not be compatible with other distributions)
- Authentication uses Twingate Service Keys (not user credentials)

## Prerequisites
- Twingate Service Key configured as a CI/CD secret
- Ubuntu-based runner/machine image
- Resources assigned to the Service account

## GitHub Actions Configuration

**Install Twingate:**
```bash
echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list
sudo apt update -yq && sudo apt install -yq twingate
```

**Setup and start:**
```bash
echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-
sudo twingate start
```

**Stop:**
```bash
sudo twingate stop
```

**Required secret:** `SERVICE_KEY` → exposed as `TWINGATE_SERVICE_KEY` env var

## CircleCI Configuration

**Key difference:** Service Key must be **base64 encoded** for CircleCI variable storage, then decoded at runtime:
```bash
echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-
```

**Recommended image:** `ubuntu:jammy-20250530`

**Install requires** `ca-certificates` before Twingate package.

## Configuration Values

| Parameter | Value |
|-----------|-------|
| APT repo | `deb [trusted=yes] https://packages.twingate.com/apt/ /` |
| Sources file | `/etc/apt/sources.list.d/twingate.list` |
| Setup flag | `--headless=-` (reads key from stdin) |
| CircleCI env var | `$SERVICE_KEY` (base64 encoded) |
| GitHub env var | `$TWINGATE_SERVICE_KEY` (plaintext) |

## Gotchas
- CircleCI requires Service Key to be base64 encoded in variable storage — must decode before passing to `twingate setup`
- Linux Client compatibility is not guaranteed outside Ubuntu
- Always stop Twingate at end of job (`sudo twingate stop`)
- Use `twingate status` and `journalctl -u twingate` for debugging connection issues

## Related Docs
- Twingate headless Client mode documentation
- Twingate Services documentation
- GitHub Marketplace: "Connect to Twingate" Action