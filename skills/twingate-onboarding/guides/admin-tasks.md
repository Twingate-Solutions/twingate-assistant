<!-- manual-reference: do-not-overwrite -->
# Admin tasks — "Your next steps"

Close every turn with a "Your next steps" block. Each task gives:

- the **action**, as one concrete verb phrase;
- **where** — system and page. Take exact console paths and field names from the owning skill's
  references (twingate-identity, twingate-connectors, twingate-api, …), never from memory —
  console menus change;
- **what to send back** — the evidence that closes the task.

Record each task in `tasks` with `evidence_needed`. When evidence arrives, update the state file
and mark the task done.

## Format by assist level

`handhold` — numbered sub-steps with click paths, plus what success looks like on screen:

```
**Your next steps**
1. Connect Entra ID to Twingate.
   a. In the Twingate admin console, open <page from twingate-identity references>.
   b. …
   You should see: <expected state>. Send back: a screenshot of that page.
(Estimated time: ~15 min. Blocked on: nothing.)
```

`checklist` — one line per task:

```
**Your next steps**
1. Connect Entra ID with SCIM in the admin console. Send back: screenshot showing it connected.
2. Raise the connector egress firewall change. Send back: ticket number.
```

`automate` — the same checklist, plus the generated command/script/IaC for each task Claude can
automate, and which ones Claude can run directly (with approval) vs. the admin must run.

Order tasks so slow, external work comes first (firewall change requests, IdP admin approvals,
procurement), then quick tasks.

## Common tasks and evidence

| Task | Evidence that closes it |
|---|---|
| Send the network diagram (source file if possible) or an IPAM export | The file |
| Send a transcript of the environment walkthrough | The transcript |
| Export VPN group policies / split-tunnel ACLs (redact secrets) | The file or pasted text |
| Create a Read API token, set it as env var `TWINGATE_API_KEY` | Admin confirms it's set — **never** the token |
| Upgrade to a Read+Write token for the build | Confirmation only |
| Create the tenant | Tenant name |
| Connect the IdP and enable SCIM | Screenshot of the identity provider settings showing connected |
| Assign groups to the Twingate app in the IdP and sync | Groups list via API read, or screenshot of the Groups page |
| Raise a firewall egress change for connector hosts | Ticket number or screenshot of the rule |
| Run the connector-host preflight | Pasted output |
| Deploy connectors | Connector states via API read or screenshot — **not** connector tokens |
| Install the Client for pilot users | Pilot user list with OSes |
| Pilot test checklist | Pass/fail per resource per pilot user |
| Tighten zone firewalls to connector-only inbound | Ticket number or screenshot |
| Revoke temporary API tokens | Confirmation |

## Tone

Short and literal: one task per line in `checklist`. If the admin is stuck, offer to break the
task down or to read what they see ("send me a screenshot of where you are").
