<!-- manual-reference: do-not-overwrite -->
# Question bank

Pick from this list; never recite it. Skip anything the artifacts or state file already answer.
Use the structured question tool when one is available. Give each question options where the
answer space is small, a default, and a one-line "why this matters".

**How many to ask** follows the admin, not a fixed limit:

- **Guided path / `handhold`:** ask freely, in topic-sized rounds, and keep going until the
  phase's gate data is in. Prompted questions with options are how less technical admins surface
  things they wouldn't think to mention — a printer, a vendor login, a legacy app.
- **`checklist`:** fewer rounds, each covering a whole topic; lean on defaults the admin can
  accept in one word.
- **Expert path:** validate what the admin gives you; ask only about gaps, conflicts and risks.

Within a round, group by topic and lead with the lowest-confidence items. If the admin signals
they want fewer (or more) questions, adjust and record it in `meta.assist_level` if it changes.

## Phase 0 — Kickoff

| Question | Options / default | Why it matters |
|---|---|---|
| What's driving this? | VPN replacement / new remote access / contractor access / compliance / POC | Sets scope and what "done" means |
| Do you already know which teams need access to what? | Yes, I'll tell you (expert) / Roughly / No, help me work it out (guided) | Picks the path (`meta.path`) |
| How much help do you want from me? | Walk me through every click (handhold) / Just give me the checklist (checklist) / Do as much as you can for me — scripts, API calls, IaC (automate) | Sets `meta.assist_level`; changeable any time |
| What would make the first week a success? | Free text; example: "DBAs reach db1 from home without VPN" | Becomes testable success criteria |
| Do you have a Twingate tenant yet? What's its name? | `<name>.twingate.com` / not yet | Needed for console links and API calls |
| How should config be managed long term? | Terraform / Pulumi / scripts against the API / admin console | Picks the build path |
| Do you already manage infrastructure as code? Where? | Terraform repo / Pulumi / none | Twingate should be added to existing IaC, not beside it |
| What do you have handy? | Network diagram / recording or notes from a walkthrough / VPN or firewall config / IP, DNS or cloud inventory / IdP group list / nothing yet | Decides how Phase 1 starts |

Ask only if `environment.windows_only` is `yes` and the admin wants scripts:
"Your environment is Windows-only. Do you want scripts in PowerShell instead of Python?"
(PowerShell / Python is fine). Never assume PowerShell.

## Phase 1 — Discover

| Question | Options / default | Why it matters |
|---|---|---|
| Is this diagram current? | Current / probably out of date / not sure | Out-of-date diagrams need verifying before anything gets built |
| Are any of these zones in other sites, cloud accounts or organisations? | Per zone | Places Remote Network boundaries; marks out-of-scope |
| Do these servers have internal DNS names? Is there an internal zone? | Yes, `<zone>` / IPs only / mix | FQDN Resources survive IP changes; CIDRs are the fallback |
| Is there a VPN today? Can you export its group policies or split-tunnel ACLs? | Can export / can't export / no VPN | Best single source for the access model |
| Can you share firewall rules per zone (credentials redacted)? | Yes / no | Shows current access and what to tighten later |
| Can you run a few read-only commands for me? | Yes / no / someone else can | Unlocks `intake-discovery.md` |

## Phase 2 — Tenant & IdP

| Question | Options / default | Why it matters |
|---|---|---|
| Which IdP do you use? | Okta / Entra ID / Google / JumpCloud / OneLogin / Keycloak / other | Determines setup steps and SCIM support |
| Is it connected to Twingate yet? | Yes, with SCIM / yes, no SCIM / no | Without SCIM, deprovisioning is manual |
| For each role: do you know which IdP group matches? | Per persona: known / I'll search / need a new group | Expert mapping vs. guided search |
| Can you share your IdP group list (export, screenshot, or let me read it)? | Export / screenshot / read-only connector / no | Lets Claude suggest which groups to provision |
| May I read the synced groups through the API? | Yes, a Read token is in an env var / I'll screenshot the Groups page | Gives real group IDs |

## Phase 3 — Confirm resources

Ask about the lowest-confidence rows first, framed as confirming a guess:

- "I've assumed **db1** is SQL Server on 1433, used by DBAs and server admins. Correct?" (Yes / Different port / Different users / Not in scope)
- "What does **hr01** run besides SSH? Is there a web UI or app port?"
- "Who owns **<resource>** — who approves access to it?"
- "Is anything here **out of scope** for the first phase?"
- "Is there anything people use that **isn't on the diagram** — SaaS with IP allowlists, printers, jump hosts?"

## Phase 4 — Access model

- "Here are the roles I think need access (table). Anything to add, merge or rename?"
- "Which of these are **sensitive** — need MFA per session, a trusted device, or shorter sessions?" Default: prod DB, HR, identity systems.
- "Do any **contractors or vendors** need access? To what, and for how long?"
- "Do any **scripts, CI pipelines or monitoring systems** need to reach these?" (service accounts)
- "Should **admin access** (RDP/SSH) be separate from **app access** (web/DB)?" Default: yes for prod.
- "Do any SSH, Kubernetes or internal web-app resources need per-user identity or session recording?" (twingate-idfw)

## Phase 5–6 — Remote Networks and Connectors

| Question | Options / default | Why it matters |
|---|---|---|
| Where can connectors run in each zone? | Docker host / Linux VM / Hyper-V or VMware VM / cloud service / Kubernetes | Picks the deployment method |
| Which VLAN, subnet or vSwitch puts a host in each zone? | Per zone | Connectors need line of sight to the resources they serve |
| Does outbound traffic pass through TLS inspection or a proxy? | Yes / no / unknown | Inspection or proxying of Twingate traffic breaks connectors (details: twingate-connectors) |
| How long does a firewall change take to approve? | Days / weeks | Decides when to raise the change request |

## Phase 7–9 — Build, pilot, rollout

- "Here's exactly what will be created (plan). OK to apply?" (Apply / change something / not yet)
- "Who are 2–5 pilot users, covering different roles and OSes?"
- "How will the Client be deployed: MDM push, self-install, or both?"
- "Does anything on standard laptops touch networking — another VPN, an SSE agent, a DNS filter, AV web protection?"
- "Once the pilot passes, can each zone's firewall accept traffic only from the connectors?"
- "Is there a VPN decommission date?"
