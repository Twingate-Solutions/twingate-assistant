<!-- manual-reference: do-not-overwrite -->
# Persona catalog

Turns a host label ("Production Database server", "MS W2K3") into a first guess at service type,
ports, personas and sensitivity. **Every value taken from this file is `inferred`** until the admin
confirms it. The ports are generic, vendor-default networking knowledge, not Twingate facts — they
are starting points to confirm, never values to build from.

## Service types

| service_type | Recognise from | Likely app ports (TCP unless noted) | Admin ports | Personas | Default sensitivity |
|---|---|---|---|---|---|
| web-prod | "production web", IIS, nginx, Apache | 80, 443 | 3389 (Win) / 22 | app-users (if internal), web-dev, server-admin | medium |
| web-dev | "dev web", "staging", "test" | 80, 443, 8080 | 3389 / 22 | web-dev, server-admin | low |
| mssql | "database" on Windows, SQL Server | 1433 | 3389 | dba, app-dev (dev only), server-admin | high (prod) / medium (dev) |
| postgres / mysql / oracle | Postgres, MySQL, Oracle | 5432 / 3306 / 1521 | 22 | dba, app-dev (dev only) | high (prod) |
| file-server | "file server", SMB, NAS | 445 | 3389 | all-staff or department groups, server-admin | medium |
| hr-system | "HR", payroll | 443 + vendor ports | 22 / 3389 | hr-admins, hr-app-admin | restricted |
| identity | AD DC, LDAP, IdM | 443; AD: 53, 88, 389, 445, 464, 636, 3268-3269; UDP 53/88/123/389 | 3389 | identity-admins | restricted |
| mainframe | "mainframe", z/OS, AS/400 | 23/992 (TN3270), vendor ports | — | mainframe-ops, specific app users | high |
| ssh-host | Linux/Unix server, bastion | — | 22 | server-admin, app owner team | medium |
| kubernetes | k8s API, cluster | 6443 / 443 | — | platform-eng (consider twingate-idfw / twingate-kubernetes) | high |
| hypervisor | vCenter, Hyper-V host, iDRAC/iLO | 443 | 443 / 22 / 3389 | infra-admins | restricted |
| network-device | router, firewall, switch management | 443, 22 | 22 | network-admins | restricted |
| workstation | developer desktop, user PC | — | 3389 / 22 / 5900 | usually a **client**, not a resource | low |
| printer | printer, MFP | 9100, 631, 443 | — | all-staff | low |
| monitoring | Grafana, Zabbix, Nagios | 443, 3000 | 22 | ops, server-admin | medium |
| ci-cd | Jenkins, GitLab, build servers | 443, 8080 | 22 | developers, **service accounts** for pipelines | medium |
| unknown | anything else | ask | ask | ask | ask |

## Persona defaults

| Persona id | IdP group search terms | Policy tier |
|---|---|---|
| server-admin | "server", "sysadmin", "infrastructure", "IT ops", "windows admins" | elevated |
| dba | "DBA", "database", "SQL", "data platform" | elevated |
| web-dev / app-dev | "developers", "engineering", "dev", team names | standard |
| hr-admins | "HR", "people ops", "payroll" | restricted |
| identity-admins | "IAM", "identity", "IdM", "AD admins" | restricted |
| infra-admins | "infrastructure", "virtualization", "platform" | restricted |
| network-admins | "network", "netops" | restricted |
| all-staff | "all staff", "employees", "everyone" (fine for low-sensitivity resources only) | standard |
| contractors | "contractors", "vendors", "external", vendor name | restricted + time-boxed |

## Policy tiers (proposals — configure via twingate-identity)

- **standard** — the default security policy.
- **elevated** — stronger authentication requirements and a trusted device for prod.
- **restricted** — the strongest available controls: per-session re-authentication, trusted device,
  and optionally approval-based or time-limited access.

What each tier maps to in product terms (policy options, device-trust settings, JIT/approval
features) comes from the twingate-identity skill's references at the time of the work.

## Heuristics

- When a production server needs both app and admin access, propose **separate personas**:
  developers reach the app, only server-admins reach RDP/SSH. Different ports per persona can mean
  two Resources for one address — check twingate-architect (grep its references for "overlap")
  before proposing that.
- Workstations in "developers" or "users" zones are almost always **clients**. Ask before making
  them Resources.
- Anything in another organisation's network is **out of scope** by default; revisit as an
  IP-allowlisting use case (twingate-architect, twingate-dns-security for fixed egress).
- An EOL operating system is a finding to raise, not a blocker. Record it in `open_questions`.
- SSH, Kubernetes API, or internal web apps where *who* did *what* matters → suggest
  twingate-idfw in Phase 4.
