# CI/CD Configuration for Twingate

## Summary
Provides sample configurations for integrating Twingate headless Client into CI/CD pipelines via GitHub Actions and CircleCI. A prebuilt GitHub Marketplace action is available for simplified integration. Configurations use Twingate Service Keys for authentication.

## Key Information
- Sample configs maintained in a public GitHub repository with automated testing
- GitHub Marketplace action available: "Connect to Twingate"
- Supports GitHub Actions and CircleCI (Ubuntu-based)
- Linux Client compatibility limited — may not work on non-Ubuntu distributions
- CircleCI requires `SERVICE_KEY` to be base64-encoded due to variable storage requirements

## Prerequisites
- Twingate Service Key created and assigned Resources
- Ubuntu-based runner/machine (required for Linux Client compatibility)
- Secret storage configured in CI platform (`SERVICE_KEY`, `TEST_URL`)

## Step-by-Step (GitHub Actions)

1. Add Twingate apt repo and install client
2. Pipe `TWINGATE_SERVICE_KEY` to `twingate setup --headless=-`
3. Run `sudo twingate start`
4. Execute workflow steps requiring protected Resource access
5. Run `sudo twingate stop` at end of job

## Step-by-Step (CircleCI)

1. Install `ca-certificates` and Twingate via apt
2. Decode base64 `SERVICE_KEY`: `echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-`
3. Run `sudo twingate start`
4. Access protected/public resources
5. Run `sudo twingate stop`

## Configuration Values

| Variable | Platform | Notes |
|---|---|---|
| `TWINGATE_SERVICE_KEY` | GitHub Actions | Plaintext secret |
| `SERVICE_KEY` | CircleCI | Must be base64-encoded |
| `TEST_URL` | Both | URL of protected Resource |

**Key CLI flags:**
- `twingate setup --headless=-` — reads service key from stdin
- `twingate start` / `twingate stop` / `twingate status`

**Apt repository:**
```
deb [trusted=yes] https://packages.twingate.com/apt/ /
```

## Gotchas
- CircleCI: `SERVICE_KEY` **must be base64-encoded** before storing; decode before passing to setup
- Linux Client may not be compatible with non-Ubuntu distributions
- Machine image versions in examples may not be latest — verify current image tags in official docs
- These are guide configurations only; apply additional security hardening for production use
- Use `journalctl -u twingate` for debugging connection issues

## Related Docs
- Twingate headless Client mode documentation
- Twingate Services (Service Keys) documentation
- [GitHub Marketplace Action](https://github.com/marketplace) — "Connect to Twingate"
- Public sample repo: referenced in Twingate docs (linked from source page)