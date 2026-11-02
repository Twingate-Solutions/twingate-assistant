<!-- manual-reference: do-not-overwrite -->
# deployment.yaml schema

`twingate-deployment/deployment.yaml` is the single source of truth for a deployment. Update it
after every answer, artifact, or API read. Keep it human-readable — the admin may open and edit it.
Only the main conversation writes this file; subagents receive a slice of it and return results.

## Where the state file lives

| Environment | Location | Resume |
|---|---|---|
| Claude Code, Cowork with a local folder | `twingate-deployment/deployment.yaml` in the working directory | Automatic: look for the file at session start |
| Chat with no writable working directory | Give the admin the full file as a downloadable YAML block at the end of every session | Ask the admin to attach it at the start of the next session |

The file contains internal hostnames, IPs, and org structure. Tell the admin once, at creation:
keep it out of public repositories (add `twingate-deployment/` to `.gitignore` if the folder is
inside a repo). Never store tokens, keys, connector tokens, passwords, PSKs, or SNMP communities.

## Provenance

Every catalog entry (remote network, resource, persona, group mapping) carries `provenance`:

| Value | Meaning | Buildable? |
|---|---|---|
| `inferred` | Claude guessed it — diagram label, service type, persona catalog, transcript interpretation | No |
| `stated` | The admin said it in conversation, or confirmed a transcript excerpt verbatim | Yes |
| `sourced` | Came from an artifact: export, screenshot, CLI output, API read. Set `source_ref` | Yes |
| `confirmed` | The admin approved an `inferred` value without changing it | Yes |

When the admin corrects an inferred value, replace it and set provenance to `stated`, not
`confirmed`. A transcript is a `sources` entry; facts pulled from it start `inferred` until read
back and accepted.

## Top-level keys

```yaml
meta:
  customer: ""              # display name
  tenant: ""                # <tenant>.twingate.com subdomain
  path: guided              # guided | expert  — does the admin already know the access model?
  assist_level: handhold    # handhold | checklist | automate  — how much help; admin may change any time
  scripting: python         # python | powershell | terraform | pulumi | console | none
  existing_iac: ""          # e.g. "Terraform in infra/ (AWS modules)" — Twingate gets added there
  phase: 0                  # current phase number (0-9)
  goals: []                 # free text, stated
  success_criteria:         # testable statements; strings are treated as status: open
    - text: "DBAs reach db1:1433 from home without VPN"
      status: open          # open | met | deferred
      note: ""              # reason when deferred
  in_scope: []              # sites/zones/apps in scope
  out_of_scope: []

sources:                    # every artifact received
  - id: src-1
    kind: diagram           # diagram | screenshot | export | cli-output | api | transcript | answer | doc | idp-directory
    description: "Customer network diagram (PNG)"
    received: 2026-11-02
    notes: ""               # never paste secrets here

environment:
  idp: ""                   # okta | entra | google | jumpcloud | onelogin | keycloak | other | none
  idp_connected: false      # true once the IdP shows connected in the tenant
  scim: unknown             # yes | no | unknown
  mdm_edr: []               # e.g. [intune, crowdstrike]
  os_mix: ""                # e.g. "80% Windows, 20% macOS, managed"
  windows_only: unknown     # yes | no | unknown — gates the PowerShell question
  existing_vpn: ""          # e.g. "AnyConnect on ASA"
  conflicting_software: []  # other VPNs, SSE agents, DNS filters, AV web protection
  egress:
    ssl_inspection: unknown # yes | no | unknown
    proxy_required: unknown
    notes: ""

remote_networks:
  - name: "HQ Datacenter"
    location: ON_PREMISE    # value from the API's remote network location enum (verify via twingate-api)
    subnets: ["10.20.0.0/24"]
    boundary: "ASA 5520"    # firewall / VPC / VNet / site that defines the zone
    connector_platform: docker   # docker | systemd | hyperv | vmware | aws-ecs | azure-aci | gcp | k8s | other
    connector_count: 2
    connector_hosts: []     # hypervisor host / VLAN / subnet details
    connectors: []          # from API: [{name, id, state}]
    firewall_change: pending  # not_needed | pending | requested | done
    twingate_id: null       # set after creation (read back from API)
    provenance: inferred
    source_ref: src-1

resources:
  - id: res-db1             # stable local id
    name: "db1 (Prod DB)"
    address: "db1.corp.example.com"   # FQDN preferred; IP/CIDR when no hostname
    ip_hint: "10.20.0.70"   # informational
    remote_network: "HQ Datacenter"
    service_type: mssql     # key from persona-catalog.md, or unknown
    description: "Production database server"
    environment: prod       # prod | dev | test | shared
    sensitivity: high       # low | medium | high | restricted
    owner: ""               # person/team who approves access
    ports: {tcp: ["1433"], udp: [], icmp: true}   # ["*"] = all ports; "a-b" ranges; [] = none on that protocol
    personas: [dba, server-admin]
    in_scope: true
    provenance: inferred
    source_ref: src-1
    twingate_id: null

personas:                   # roles/teams that need access; NOT Twingate objects
  - id: dba
    name: "Database Administrators"
    description: "Manage prod and dev SQL Server"
    idp_search_hint: "groups containing DBA, database, SQL"
    policy_tier: elevated   # standard | elevated | restricted  (maps to a security policy)
    groups: []              # Twingate group NAMES mapped to this persona (must exist in groups:)
    provenance: inferred

groups:                     # read from the Twingate API (or a screenshot), never invented
  - name: "IT-DBA"
    twingate_id: "R3JvdXA6..."
    type: SYNCED            # SYNCED | MANUAL | SYSTEM
    member_count: 6
    provenance: sourced
    source_ref: src-4

decisions:                  # approvals and choices, append-only
  - date: 2026-11-02
    phase: 4
    decision: "Approved access matrix v1"
    approved_by: "admin name"

open_questions:
  - id: q-1
    phase: 3
    question: "What ports does the HR app on hr01 use besides SSH?"
    owner: admin            # admin | claude | <team name>
    status: open            # open | answered | deferred

tasks:                      # the admin's (and Claude's) to-do list
  - id: t-1
    phase: 6
    owner: admin
    description: "Request egress rule for connector hosts (rules from twingate-connectors)"
    evidence_needed: "Change ticket number or screenshot of the rule"
    status: todo            # todo | in_progress | blocked | done
```

Product values in this example (location enum, group types, connector states) are shapes, not
the spec. Confirm current values through the twingate-api skill before writing them.

## Phase gates (checked by `scripts/status.py`)

| Phase | Gate to leave the phase |
|---|---|
| 0 Kickoff | `meta.tenant`, `meta.path`, `meta.assist_level` set; ≥1 success criterion |
| 1 Discover | ≥1 remote network; every in-scope resource has `address` and a known `remote_network`; ≥1 persona |
| 2 Tenant & IdP | `environment.idp` set and not `none`; `idp_connected: true`; SCIM `yes` or a phase-2 decision accepting no SCIM; every persona used by an in-scope resource maps to ≥1 group that has a `twingate_id` |
| 3 Confirm resources | ≥1 in-scope resource; every in-scope resource has buildable provenance and at least one TCP or UDP port entry |
| 4 Access model | Every in-scope resource has ≥1 persona; every referenced persona exists with buildable provenance; a phase-4 decision |
| 5 Remote Networks | ≥1 remote network; every remote network has buildable provenance and a `twingate_id`; a phase-5 decision |
| 6 Connectors | ≥1 remote network; every remote network has `connector_count` (≥2) connectors in state `ALIVE` |
| 7 Resources & access | ≥1 in-scope resource; every in-scope resource has a `twingate_id`; a phase-7 decision |
| 8 Pilot | ≥1 success criterion; every success criterion is `met` or `deferred` with a note |
| 9 Rollout & harden | A phase-9 decision (admin sign-off) |

**Build rules** (reported by `status.py` as `networks_build_allowed` / `resources_build_allowed`):

- Creating Remote Networks (phase 5) requires gates 0–1 to pass and every remote network to have
  buildable provenance.
- Creating Resources and access (phase 7) requires gates 1 through 6 to pass.
- Write `scim: "yes"` quoted when editing by hand (unquoted `yes` is a YAML boolean; the script
  accepts both, other tools may not).
- Phases may run in parallel when that unblocks the admin (resource confirmation while waiting on
  IdP admins, for example). Never build past an unmet build rule.
