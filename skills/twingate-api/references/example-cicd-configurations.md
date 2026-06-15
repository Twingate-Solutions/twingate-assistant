# CI/CD Configuration for Twingate

## Summary
Twingate provides sample configurations for integrating the headless Client into CI/CD pipelines using a Service Key. A GitHub Marketplace Action is available for simplified GitHub workflows, and manual configurations are provided for CircleCI. All samples connect a pipeline runner to Twingate-protected Resources via a Service Account.

## Key Information
- Sample configurations hosted in a public GitHub repository and included in automated testing
- GitHub Marketplace Action: "Connect to Twingate" handles install, configure, and start automatically
- Headless Client runs on Ubuntu; may not be compatible with other Linux distributions
- CircleCI requires the Service Key to be base64-encoded when stored as a variable

## Prerequisites
- Twingate Service Key (from a configured Service Account)
- Ubuntu-based runner/machine image
- Resources assigned to the Service Account
- Service Key stored as a CI/CD secret (`SERVICE_KEY`)

## Step-by-Step (GitHub Actions)

1. Install Twingate via apt from `packages.twingate.com/apt/`
2. Pass Service Key via stdin: `echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-`
3. Start client: `sudo twingate start`
4. Run workflow steps accessing protected Resources
5. Stop client: `sudo twingate stop`

## Step-by-Step (CircleCI)

1. Install Twingate via apt (include `ca-certificates` first)
2. Decode base64 Service Key and pipe to setup: `echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-`
3. Start client: `sudo twingate start`
4. Run access tests against protected Resources
5. Stop client: `sudo twingate stop`

## Configuration Values

| Parameter | Value/Notes |
|---|---|
| APT source | `deb [trusted=yes] https://packages.twingate.com/apt/ /` |
| Setup flag | `--headless=-` (reads key from stdin) |
| GitHub secret | `secrets.SERVICE_KEY` |
| CircleCI variable | `$SERVICE_KEY` (base64 encoded) |
| CircleCI image | `ubuntu:jammy-20250530` |

## Debugging Commands
```bash
twingate status
journalctl -u twingate          # GitHub Actions
journalctl -u twingate --no-pager | tail -n 20  # CircleCI
```

## Gotchas
- CircleCI stores environment variables requiring base64 encoding; must decode before passing to `twingate setup`
- Linux Client compatibility limited — Ubuntu recommended; other distros may not work
- Use `--headless=-` flag (stdin) rather than passing key as a direct argument to avoid exposure in process lists
- Code samples may reference outdated software versions; verify against official docs

## Related Docs
- [Twingate Headless Client documentation](https://www.twingate.com/docs/headless-clients)
- [Service Accounts / Service Keys](https://www.twingate.com/docs/services)
- [GitHub Marketplace Action](https://github.com/marketplace/actions/connect-to-twingate)
- [Twingate CI/CD sample repository (GitHub)](https://github.com/Twingate)