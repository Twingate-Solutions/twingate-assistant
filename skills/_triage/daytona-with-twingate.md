---
source: https://www.twingate.com/docs/daytona-with-twingate
type: docs
fetched: 2026-11-19
source_version: 6b9594a51217f11c100f29f99d5c9273e8a866a3c6b2697e854e96221afc4952
trust: official
---

<!-- triage: unassigned -->

# Access Private Resources from Daytona Sandboxes

## Summary
Each Daytona sandbox connects to Twingate as a Service and can reach only the Resources assigned to that Service. Your code creates the sandbox with the Daytona SDK, installs the Twingate Client, performs headless setup with a Service Key, and starts the agent once the Client is online. Only connections to the Service's Resources go through Twingate; other traffic goes to the internet as before.

## Key Information
- Flow per sandbox: create sandbox → install Client → upload Service Key → `twingate setup --headless` → delete key file → `twingate service-start` → poll `twingate status` until `online` → start agent.
- Polling: every 5 seconds, up to 24 attempts.
- The Client log is at `/var/log/twingated.log` in the sandbox.
- Sandboxes may connect via Relays rather than peer-to-peer, which can add latency.
- Examples are provided in Python (`daytona`) and TypeScript (`@daytona/sdk`).

## Prerequisites
- Daytona organization on Tier 3 or higher, with the default network policy (full internet on Tier 3/4).
- `DAYTONA_API_KEY` environment variable set (read by the SDK).
- Daytona SDK installed (Python or TypeScript).
- A Twingate Service with assigned Resources and a Service Key with a reasonable expiration.

## Step-by-Step
1. **Create a Service** in Twingate, assign the needed Resources, and generate a Service Key.
2. **Expose the key** to your code as `TWINGATE_SERVICE_KEY` (store it in your secrets manager).
3. **Connect each sandbox** with a `connect_to_twingate` helper that runs these commands in the sandbox:
   - Download the installer from `https://binaries.twingate.com/client/linux/install.sh` to `/tmp/twingate-install.sh`, then run it with `sudo bash` (300s timeout).
   - Upload the key to `/tmp/service_key.json` via the SDK's file upload.
   - `sudo twingate setup --headless /tmp/service_key.json`
   - Always `rm -f /tmp/service_key.json` afterward (use try/finally).
   - `sudo twingate service-start`
   - Poll `twingate status` (30s command timeout) until it prints `online`. On failure, raise an error including `tail -n 50 /var/log/twingated.log`.
4. **Start the agent** after the helper returns.
5. **Verify** with `twingate resources` and `curl -sS -o /dev/null -w '%{http_code}' <web Resource URL>`. For non-web Resources (e.g. a database), use a protocol-appropriate client.

## Configuration Values
- `DAYTONA_API_KEY`: Daytona SDK auth.
- `TWINGATE_SERVICE_KEY`: Service Key contents (JSON).
- Daytona network settings that can interfere: `networkAllowList`, `domainAllowList`, `networkBlockAll`.
- Client port requirements: see Endpoint Requirements.

## Gotchas
- Tier 1/2 organizations lack the internet access needed for install and Client connectivity.
- On Tier 3/4, allow lists or `networkBlockAll` can block the install or Client connections.
- A Daytona secret will not work as the Service Key: inside the sandbox it is only a placeholder. This causes the `Invalid service key` log error.
- After a sandbox stops and restarts, `twingate status` may show `not-running`. Run `sudo twingate service-start`; setup does not need to be repeated.
- Command timeouts: pass a longer timeout to the `run` helper.
- Always delete the uploaded key file, even on setup failure.

## Related Docs
- Services
- Linux Headless Mode (troubleshooting)
- Daytona's Twingate guide
- Coding Agents use case
- Endpoint Requirements