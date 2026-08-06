---
source: https://github.com/Twingate-Solutions/connector-local-ui
type: github
fetched: 2026-08-06
source_version: 66a2dbe67d5885fc0a6b379f1989ea4d0b9765dd
---

<!-- triage: unassigned -->

# connector-local-ui

## Summary
A web-based local UI that runs directly on a Twingate Connector host machine. It provides a browser-accessible interface for viewing connector status and diagnostics without requiring access to the Twingate Admin Console.

## Key Information
- Deploys alongside a Twingate Connector on the same host
- Built as a lightweight local dashboard for connector monitoring
- Intended for operators who need on-host visibility into connector health

## Prerequisites
- A running Twingate Connector installed on the host
- Docker or Node.js runtime (depending on deployment method)
- Network access to the connector host on the UI's port

## Usage / Step-by-Step

1. **Clone the repository**
   ```bash
   git clone https://github.com/Twingate-Solutions/connector-local-ui.git
   cd connector-local-ui
   ```

2. **Configure environment** — copy or edit the environment file with your connector details (see Configuration Values below)

3. **Run the UI**
   - Via Docker:
     ```bash
     docker compose up -d
     ```
   - Via Node.js:
     ```bash
     npm install
     npm start
     ```

4. **Access the UI** — open a browser and navigate to `http://<connector-host>:<PORT>`

## Configuration Values

| Variable / Parameter | Description | Default |
|---|---|---|
| `PORT` | Port the local UI listens on | `8000` |
| `CONNECTOR_HOST` | Hostname or IP of the connector process | `localhost` |
| `CONNECTOR_API_PORT` | Port exposed by the connector's local API | varies |
| `LOG_LEVEL` | Logging verbosity (`debug`, `info`, `warn`, `error`) | `info` |

> **Note:** Exact variable names should be verified against the `.env.example` or `docker-compose.yml` in the repo, as the above reflects common patterns observed in similar projects.

## Gotchas
- The UI must run **on the same host** as the connector or have direct network access to the connector's local API — it is not designed as a remote management tool
- No authentication is built into the local UI by default; restrict access via firewall rules or host-level controls
- The connector's local API must be enabled and accessible; check connector configuration if the UI shows no data
- Port conflicts with other services on the host should be checked before deployment

## Related Docs
- [Twingate Connector documentation](https://www.twingate.com/docs/connector)
- [Twingate Admin Console](https://auth.twingate.com)
- Twingate Connector local API reference (consult Twingate support or internal docs)

---
*Verify specific configuration keys and defaults directly against the repository source, as this summary is based on available metadata.*