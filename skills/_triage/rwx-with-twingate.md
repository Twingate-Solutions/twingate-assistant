---
source: https://www.twingate.com/docs/rwx-with-twingate
type: docs
fetched: 2026-11-19
source_version: 5e89c25bb35e14e36fbac3087befddb6f72b3abf1736fef322f120d6c82e3c32
trust: official
---

<!-- triage: unassigned -->

# Access Private Resources from RWX Sandboxes

## Summary
Connects RWX sandboxes (used by coding agents such as Claude Code or Codex via `rwx sandbox exec`) to Twingate as a Service. Each sandbox can reach only the Resources assigned to that Service. RWX's `twingate/setup` package installs the Twingate Client and performs headless setup with a Service Key.

## Key Information
- Sandbox is defined in `.rwx/sandbox.yml`; a task named `sandbox` runs `rwx-sandbox`.
- Startup flow: `twingate` task (calls `twingate/setup`) → Client started as background process of `sandbox` task → waits up to 30s for `twingate status` to print `online` → `rwx-sandbox` runs.
- Guide is based on the minimal sandbox.yml using the `ubuntu:26.04` image and `rwx/base 1.2.1`.
- Default network setup is used; required ports are in Twingate Endpoint Requirements.

## Prerequisites
- An RWX organization
- RWX CLI installed and signed in (`rwx login`)
- `.rwx/sandbox.yml` in the repo (create with `rwx sandbox init`)

## Step-by-Step
1. **Create a Service** in Twingate, assign needed Resources, generate a Service Key with a reasonable expiration.
2. **Store the key** in an RWX vault as `TWINGATE_SERVICE_KEY` (raw JSON from the key file):
   `rwx vaults secrets set TWINGATE_SERVICE_KEY="$(cat service-key.json)"` (stores in the `default` vault)
3. **Edit `.rwx/sandbox.yml`**: add a `twingate` task after the `code` task, and update the `sandbox` task:
   ```yaml
   - key: twingate
     call: twingate/setup 1.1.1
     with:
       twingate-service-key: ${{ secrets.TWINGATE_SERVICE_KEY }}

   - key: sandbox
     use: [code, twingate]
     background-processes:
       - key: twingate
         run: sudo twingate start
         ready-check:
           run: '[ "$(twingate status)" = online ]'
           timeout-seconds: 30
     run: rwx-sandbox
   ```
4. **Verify** (from the directory containing `.rwx/sandbox.yml`):
   ```
   rwx sandbox exec -- twingate status
   rwx sandbox exec -- twingate resources
   rwx sandbox exec -- curl -sS -o /dev/null -w '%{http_code}\n' https://staging.internal.example.com
   ```
   Expected: `online`, list of the Service's Resources, then the HTTP status (e.g. `200`).

## Configuration Values
- Secret name: `TWINGATE_SERVICE_KEY`
- Package: `twingate/setup 1.1.1`, input `twingate-service-key`
- Non-default vault: `${{ vaults.<vault>.secrets.TWINGATE_SERVICE_KEY }}`
- Ready-check timeout: `timeout-seconds: 30`
- Client log: `/var/log/twingated.log`

## Gotchas
- If the Client isn't online within 30s, the `sandbox` task fails and `rwx sandbox exec` prints the error.
- Don't test with `ping`; the `ubuntu:26.04` image doesn't include it.
- For non-web Resources (e.g., databases), test with a client for that protocol.
- Replace the example URL with a real web Resource URL.
- Vault must be unlocked and your user must have access, or the `twingate` task can't read the secret.

## Troubleshooting
- Read logs: `rwx sandbox exec -- sudo cat /var/log/twingated.log`
- If the sandbox task failed, open the run linked by the CLI and check the `twingate` background process log.
- After fixing, start a fresh sandbox: `rwx sandbox exec --reset -- twingate status`
- Otherwise see Troubleshooting in Linux Headless Mode.

## Related Docs
- Services (Create a New Service, Service Key lifecycle)
- Linux Headless Mode
- Endpoint Requirements
- RWX sandboxes, secrets, and vaults docs
- `twingate/setup` RWX package
- Coding Agents use case