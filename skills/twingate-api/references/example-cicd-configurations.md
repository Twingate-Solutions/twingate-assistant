# CI/CD Configurations for Twingate

## Summary
Provides sample configurations for integrating Twingate headless Client into CI/CD pipelines (GitHub Actions and CircleCI). Workflows install, configure, and start the Twingate Client using a Service Key to access protected Resources.

## Key Information
- Sample configs maintained in a public GitHub repository with automated testing
- Official GitHub Marketplace Action available: "Connect to Twingate"
- Base OS must be Ubuntu; Linux Client may not be compatible with other distributions
- Service Account/Service Key required to authenticate the headless Client

## Prerequisites
- Twingate Service Key (store as CI/CD secret)
- Ubuntu-based runner/machine
- Resources assigned to the Service Account

## GitHub Actions – Step-by-Step

1. **Install Twingate** – Add APT repo and install via `apt`
2. **Setup** – Pipe `SERVICE_KEY` secret to `twingate setup --headless=-`
3. **Start** – Run `sudo twingate start`
4. **Access Resources** – Make requests to protected Resources normally
5. **Stop** – Run `sudo twingate stop` at end of job

## CircleCI – Step-by-Step

1. **Install Twingate** – Add APT repo, install `ca-certificates` and `twingate`
2. **Setup** – Decode base64 `$SERVICE_KEY`, pipe to `twingate setup --headless=-`
3. **Start** – Run `sudo twingate start`
4. **Test** – Access protected and public URLs via `curl`
5. **Stop** – Run `sudo twingate stop`

## Configuration Values

| Parameter | Value/Notes |
|---|---|
| APT repo | `deb [trusted=yes] https://packages.twingate.com/apt/ /` |
| Setup flag | `--headless=-` (reads key from stdin) |
| GitHub secret name | `secrets.SERVICE_KEY` |
| CircleCI env var | `$SERVICE_KEY` (must be **base64 encoded**) |
| CircleCI decode | `echo "$SERVICE_KEY" \| base64 --decode \| sudo twingate setup --headless=-` |
| CircleCI image | `ubuntu:jammy-20250530` |

## Gotchas
- **CircleCI only**: Service Key must be stored base64-encoded due to CircleCI variable storage requirements; decode before passing to setup
- Container image versions in examples may not be the latest — verify against official docs
- Linux Client compatibility limited to Ubuntu; other distros not guaranteed
- These are guide-level examples; apply security best practices before production use

## Related Docs
- [Headless Client / Services documentation](https://www.twingate.com/docs/services)
- [GitHub Marketplace Action: "Connect to Twingate"](https://github.com/marketplace)
- Twingate public GitHub sample repository (referenced but URL not provided)