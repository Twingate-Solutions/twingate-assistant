---
source: https://github.com/Twingate-Community/unraid-template
type: github
fetched: 2026-08-06
source_version: cc1e9288230ba26b7fee8aecaf8fab4decd60b34
---

<!-- triage: unassigned -->

# Twingate Connector — Unraid Template

## Summary
An official XML template for deploying the Twingate Connector as a Docker container via the Unraid community app system. It provides a pre-configured container definition that integrates with Unraid's Docker management UI. Users fill in credentials and network details, then apply to run the connector.

## Key Information
- Template file: `twingate-connector.xml`
- Targets Unraid's Docker template system (`/boot/config/plugins/dockerMan/templates-user/`)
- Exposes three required fields: Access Token, Refresh Token, Network Name
- Template appears under **[User templates]** in the Unraid Docker UI

## Prerequisites
- Unraid instance with SSH access
- Docker service enabled in Unraid (`Settings > Docker Settings`)
- Active Twingate account with a configured network
- Access Token, Refresh Token, and Network Name from the Twingate Admin Console

## Usage / Step-by-Step

1. SSH into the Unraid instance.
2. Create the template file:
   ```bash
   touch /boot/config/plugins/dockerMan/templates-user/twingate-connector.xml
   ```
3. Open the file in a text editor and paste the contents of `twingate-connector.xml` from this repo.
4. Save and exit.
5. In a browser, navigate to `http://<serverIP>/Settings/DockerSettings` and confirm Docker is enabled.
6. Navigate to `http://<serverIP>/Docker` and click **Add Container**.
7. In the **Template** dropdown, select `twingate-connector` under **[User templates]**.
8. Fill in the required fields (see Configuration Values below).
9. Click **Apply**.

## Configuration Values

| Field | Description |
|---|---|
| `Access Token` | Connector access token from Twingate Admin Console |
| `Refresh Token` | Connector refresh token from Twingate Admin Console |
| `Network Name` | Name of the Twingate network the connector joins |

These values are entered through the Unraid Docker UI after selecting the template; they map to environment variables inside the container.

## Gotchas
- The XML file must be placed exactly at `/boot/config/plugins/dockerMan/templates-user/twingate-connector.xml` — incorrect path means it won't appear in the UI.
- The Unraid `/boot` partition is FAT32; file edits must be saved correctly or may silently fail.
- Docker must be enabled before the template UI is accessible.
- Tokens are connector-specific; generate them per-connector in the Twingate Admin Console, not per-user.
- No automatic update mechanism is described — template changes require manually re-editing the XML file.

## Related Docs
- [Twingate Documentation](https://docs.twingate.com)
- [Twingate Connector Setup](https://docs.twingate.com/docs/connectors)
- Unraid Docker template documentation: Community Apps plugin or Unraid forums