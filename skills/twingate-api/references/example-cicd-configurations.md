# CI/CD Configuration for Twingate

## Summary
Provides sample configurations for integrating Twingate headless Client into CI/CD pipelines using GitHub Actions and CircleCI. Pipelines authenticate via a Twingate Service Key to access protected Resources. Reference configurations are maintained in a public GitHub repository with automated testing.

## Key Information
- GitHub Marketplace Action available: "Connect to Twingate"
- Supported platforms: GitHub Actions, CircleCI (Ubuntu-based)
- Authentication method: Twingate Service Key (headless mode)
- Linux Client may not be compatible with non-Ubuntu distributions
- Sample configs are included in Twingate's automated testing

## Prerequisites
- Twingate Service account with a Service Key
- Resources assigned to the Service
- Ubuntu-based runner/machine image
- Service Key stored as a CI/CD secret

## Step-by-Step (GitHub Actions)

1. Install Twingate via apt using Twingate's package repository
2. Configure headless Client: `echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-`
3. Start Client: `sudo twingate start`
4. Access protected Resources in subsequent steps
5. Stop Client: `sudo twingate stop`

## Step-by-Step (CircleCI)

1. Install `ca-certificates`, then Twingate via apt
2. Decode base64 Service Key and configure: `echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-`
3. Start Client: `sudo twingate start`
4. Access protected Resources
5. Stop Client: `sudo twingate stop`

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `TWINGATE_SERVICE_KEY` | Service Key secret (GitHub: raw value; CircleCI: base64-encoded) |
| `--headless=-` | Reads Service Key from stdin |
| `TEST_URL` | URL of Twingate-protected Resource for validation |

**APT repository:**
```
deb [trusted=yes] https://packages.twingate.com/apt/ /
```

**CircleCI machine image used in example:**
```
ubuntu:jammy-20250530
```

## Gotchas
- CircleCI requires Service Key stored as **base64-encoded** due to variable storage requirements; must decode before passing to `twingate setup`
- Linux Client compatibility is not guaranteed on non-Ubuntu distributions
- Image/version references in samples may not be latest — verify against official docs
- These are sample/guide configurations only; apply additional security hardening for production use

## Related Docs
- [Twingate Headless Client documentation](#)
- [Twingate Services documentation](#)
- [Public GitHub sample repository](https://github.com/Twingate) (referenced but URL not provided)
- [GitHub Marketplace: Connect to Twingate Action](https://github.com/marketplace)