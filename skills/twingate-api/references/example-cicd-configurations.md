# CI/CD Configuration for Twingate

## Summary
Provides sample CI/CD configurations for running the Twingate Client in headless mode within pipelines. Covers GitHub Actions (via Marketplace action) and CircleCI. Configurations install the client, authenticate with a Service Key, and connect to Twingate Resources.

## Key Information
- Public GitHub repo with sample configurations used in Twingate's own automated testing
- GitHub Marketplace action available: "Connect to Twingate"
- Supported base OS: Ubuntu (other Linux distros may not be compatible)
- Client connects using a Twingate Service Key (not user credentials)

## Prerequisites
- Twingate Service Key created and stored as a CI/CD secret
- Ubuntu-based runner/machine
- Resources assigned to the Service account

## GitHub Actions — Step-by-Step

1. Add APT repo: `echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list`
2. Install: `sudo apt update -yq && sudo apt install -yq twingate`
3. Configure: `echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-`
4. Start: `sudo twingate start`
5. (Optional) Check status: `twingate status`
6. Stop after use: `sudo twingate stop`

## CircleCI — Step-by-Step

1. Install client (same APT method as above, also install `ca-certificates`)
2. Decode Service Key before setup: `echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-`
3. Start: `sudo twingate start`
4. Run tests against protected resources
5. Stop: `sudo twingate stop`

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `TWINGATE_SERVICE_KEY` (GitHub) | Secret containing Service Key, passed via stdin |
| `SERVICE_KEY` (CircleCI) | Service Key stored **base64-encoded** due to CircleCI requirements |
| `TEST_URL` | URL of a protected resource to validate connectivity |
| `--headless=-` | Flag to read Service Key from stdin |

**CircleCI machine image:** `ubuntu:jammy-20250530`

## Gotchas
- **CircleCI requires base64-encoded Service Key** — must decode with `base64 --decode` before passing to `twingate setup`
- Linux Client may not be compatible with non-Ubuntu distributions
- Image/version references in docs may not reflect latest available — check official sources
- These are sample configurations, not hardened for production; apply security best practices before production use
- Always stop Twingate (`sudo twingate stop`) at end of job to clean up

## Related Docs
- [Headless Client mode](https://www.twingate.com/docs/headless-clients)
- [Twingate Services](https://www.twingate.com/docs/services)
- [GitHub Marketplace Action](https://github.com/marketplace/actions/connect-to-twingate)
- [Twingate CI/CD sample repo](https://github.com/Twingate) (public)