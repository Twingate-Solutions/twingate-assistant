# CI/CD Configuration for Twingate

## Summary
Provides sample configurations for integrating Twingate headless Client into CI/CD pipelines using GitHub Actions and CircleCI. Workflows install the Twingate client, authenticate with a Service Key, and connect to private Resources. Sample configs are maintained in a public GitHub repository with automated testing.

## Key Information
- GitHub Marketplace Action available: "Connect to Twingate"
- Supported platforms: Ubuntu (Jammy tested); other Linux distros may not be compatible
- Uses Twingate Service Keys for headless authentication
- APT repo: `https://packages.twingate.com/apt/`

## Prerequisites
- Twingate Service Key (from Twingate Admin Console)
- Ubuntu-based runner/machine
- Resources assigned to the Service account

## GitHub Actions — Step-by-Step

1. Install Twingate via APT:
   ```bash
   echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list
   sudo apt update -yq && sudo apt install -yq twingate
   ```
2. Configure and start using Service Key:
   ```bash
   echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-
   sudo twingate start
   ```
3. Access private Resources in subsequent steps
4. Stop client when done: `sudo twingate stop`

## CircleCI — Step-by-Step

1. Same APT install as above (also install `ca-certificates` first)
2. Decode base64 Service Key, then setup:
   ```bash
   echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-
   sudo twingate start
   ```
3. Test access to protected and public resources
4. Stop: `sudo twingate stop`

## Configuration Values

| Variable | Platform | Notes |
|---|---|---|
| `TWINGATE_SERVICE_KEY` | GitHub Actions | Store as repo secret; passed via stdin |
| `SERVICE_KEY` | CircleCI | Must be **base64-encoded** due to CircleCI variable storage requirements |
| `TEST_URL` | Both | URL of Twingate-protected Resource for validation |

## Gotchas
- **CircleCI requires base64-encoded Service Key** — decode before passing to `twingate setup`
- Service Key is passed via **stdin** (`--headless=-`), not as a CLI argument
- Linux Client **may not be compatible** with non-Ubuntu distributions
- Pinned image versions in examples may be outdated — check official docs for current images
- `sudo` required for install, setup, start, and stop commands

## Related Docs
- [Headless Client / Services documentation](https://www.twingate.com/docs/services)
- [GitHub Marketplace Action](https://github.com/marketplace/actions/connect-to-twingate)
- [Twingate public sample repo](https://github.com/Twingate) (referenced but URL not specified)