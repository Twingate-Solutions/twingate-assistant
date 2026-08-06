---
source: https://github.com/Twingate-Community/home-assistant-add-on
type: github
fetched: 2026-08-06
source_version: 44f6d226ae3148eaeefb138c2d60bce1a148c4ab
---

<!-- triage: unassigned -->

# Twingate Connector Home Assistant Add-on

## Summary
Packages the Twingate Connector as a Home Assistant add-on. Provides a Dockerfile and supporting configuration to build a Docker container compatible with Home Assistant's Supervisor add-on store. Enables running a Twingate Connector directly on a Home Assistant instance.

## Key Information
- Repository type: Home Assistant add-on repository
- Add-on included: `twingate-connector`
- Supported architectures: `aarch64`, `amd64`, `armv7`
- Base: Dockerfile + install scripts targeting Home Assistant Supervisor

## Prerequisites
- Home Assistant installation with Supervisor (i.e., Home Assistant OS or Supervised)
- A Twingate account with a network and Connector token configured
- Access to Home Assistant's add-on store

## Usage / Step-by-Step

**Add the repository to Home Assistant:**

1. Click the badge in the README or navigate manually to **Settings → Add-ons → Add-on Store**.
2. Click the menu (⋮) → **Repositories**.
3. Add the URL: `https://github.com/Twingate-Community/home-assistant-add-on`
4. Find **Twingate Connector** in the store and install it.
5. Configure the add-on with your Twingate Connector token.
6. Start the add-on.

**Manual URL entry:**
```
https://github.com/Twingate-Community/home-assistant-add-on
```

## Configuration Values
Specific configuration options are defined in the `twingate-connector` subdirectory (not fully detailed in the README). Expected values based on standard Twingate Connector setup:

| Key | Description |
|-----|-------------|
| `TWINGATE_ACCESS_TOKEN` / connector token | Token from the Twingate Admin Console to authenticate the Connector |

Check `twingate-connector/config.yaml` in the repo for the authoritative list of options.

## Gotchas
- Requires Home Assistant **Supervisor** — does not apply to Home Assistant Core (Docker-only) or Container installations without Supervisor.
- `armv7` is listed as supported; verify your device's architecture before installing.
- The Connector token must be generated in the Twingate Admin Console before configuring the add-on.
- This is a community-maintained repository, not an official Twingate-supported product.

## Related Docs
- [Twingate Connector documentation](https://www.twingate.com/docs/connector)
- [Home Assistant Add-on development](https://developers.home-assistant.io/docs/add-ons/)
- [Home Assistant Supervisor add-on store](https://www.home-assistant.io/addons/)