---
source: https://github.com/Twingate-Solutions/railway-private-web-app
type: github
fetched: 2026-08-06
source_version: 65e249e8fa3f1ca8e0612ae1293f17bad1694a29
---

<!-- triage: unassigned -->

# railway-private-web-app

## Summary
A minimal Node.js/Express web app designed to run on Railway with no public ingress. Access is enforced exclusively at Layer 4 via a Twingate Connector. Serves as a proof-of-concept for private Railway deployments.

## Key Information
- Listens on `0.0.0.0:80` (or `$PORT`)
- No public Railway domain required or intended
- Twingate Connector provides the only network path to the service
- No reverse proxy, WAF, or application-layer auth involved
- MIT licensed

## Prerequisites
- [Railway](https://railway.app) account
- Twingate account with a deployed Connector
- Node.js (for local development)

## Usage / Step-by-Step

**Local:**
```bash
npm install
npm start
# Visit http://localhost:80/
```

**Deploy to Railway (private):**
1. Deploy this repo to Railway
2. **Do not generate a public domain** for the service
3. Optionally set `PORT=80`
4. Deploy a Twingate Connector in the same Railway project
5. Create a Twingate Resource pointing to the Railway internal DNS:
   ```
   railway-private-web-app.railway.internal
   ```
6. Access the app through the Twingate client — if the page loads, access is private

## Configuration Values

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `80` | Port the Express app listens on |

## Gotchas
- Railway internal DNS hostname may differ from the example (`railway-private-web-app.railway.internal`) — verify the actual private hostname in your Railway project settings
- Public access is controlled solely by whether a Railway domain is assigned; no app-level auth exists
- This is a POC, not production-ready

## Related Docs
- [Railway Private Networking](https://docs.railway.app/reference/private-networking)
- [Twingate Connectors](https://www.twingate.com/docs/connectors)
- [Twingate Resources](https://www.twingate.com/docs/resources)