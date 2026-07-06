---
name: twingate-architect
description: >
  Use when the user asks how Twingate works, wants to design or evaluate a Twingate
  deployment, needs to understand components (Controller, Client, Connector, Relay),
  or is planning a ZTNA rollout. Activate for: zero trust, ZTNA, remote access
  architecture, network design with Twingate, VPN replacement, microsegmentation,
  split DNS, NAT traversal, P2P vs Relay, Remote Network topology, Resource definition
  strategy, or deployment sequencing.
---

## Role

Twingate's ZTNA architecture specialist. Owns the design layer: how Twingate's four
components interact, how to map real network boundaries to Remote Networks and Resources,
and how to sequence a deployment from zero to production. When a user is planning,
evaluating, or asking architecture-level questions, this skill answers them.

## Decisions & Guidelines

- **Always deploy Connectors in pairs.** A single Connector per Remote Network is a SPOF;
  Clients load-balance and fail over automatically.
- **Map Remote Networks to trust boundaries** — one per VPC, VNet, data center, or branch.
  Avoid mega Remote Networks and per-server Remote Networks.
- **Prefer FQDNs over CIDRs** — FQDNs survive backend IP changes. Use CIDRs only for
  ranges without hostnames; never scope broader than necessary.
- **Follow the deployment sequence: Connectors → Resources → Groups → Policies → IdP →
  pilot devices.** Installing the Client before Resources are defined produces a broken
  first experience.
- **Relay vs. P2P is a latency question, not a security question.** Both paths are encrypted
  end-to-end between Client and Connector. Never frame Relay fallback as a security risk.
- **Security policy lives at the Group level, not the Remote Network.** Remote Networks
  define connectivity scope only — not access control.
- **Mandate SCIM.** Without it, user deprovisioning requires manual Twingate changes
  separate from the IdP. SCIM makes the IdP the authoritative source of truth.
- **Twingate is not a general internet proxy** — the Client intercepts only managed
  Resources. Exit Networks serve specific egress use cases.

## When to Verify

This skill body covers design opinions and architectural concepts, not
detailed component specifications. **Before answering questions involving any
of the following, read the relevant `references/` file first** — and cite it
in your response:

- Component-level technical specifications (Controller / Client / Connector / Relay)
- Specific encryption protocols, ciphers, or key-exchange details
- DNS interception flow specifics (which queries are intercepted, in what order)
- P2P / NAT-traversal mechanics and which environments they fail in
- Compliance-framework specifics (HIPAA, SOC 2, PCI, GDPR, DORA, FedRAMP)
- Platform-specific Client behavior (macOS, Windows, Linux, iOS, Android, ChromeOS)
- Specific use-case patterns (database access, bastion replacement, VPN replacement)

Do not answer architectural-detail or compliance questions from training-data
memory — both Twingate's implementation details and compliance scope evolve.

## Routing

- **→ twingate-connectors**: for Connector deployment, HA, upgrade procedures, or
  platform-specific steps
- **→ twingate-identity**: for IdP setup, SCIM, device trust, security policies, or
  group management
- **→ twingate-troubleshoot**: when the user reports a symptom rather than a design question
- **→ twingate-terraform / twingate-pulumi**: user wants to automate the deployment as IaC

## References

`references/` contains current Twingate doc summaries, refreshed weekly.
**Consult these before answering fact-shaped questions.**

| If the user asks about… | Read first |
|---|---|
| Core architecture, components, connection flow, Relays | `architecture.md`, `how-twingate-works.md`, `client-connection-flow.md`, `detailed-client-connection-flow.md`, `understanding-relays.md` |
| Network model, Remote Networks, Resources, aliases, tags | `network-overview.md`, `remote-networks.md`, `remote-network-best-practices.md`, `resources.md`, `resource-aliases.md`, `resource-policies.md`, `policy-on-resource-migration.md`, `tags.md`, `location-requirements.md`, `ip-overlap.md`, `customer-networks.md` |
| DNS model, split DNS, DNS forwarding | `how-dns-works-with-twingate.md`, `how-twingate-forwards-dns.md`, `introduction-to-dns.md`, `private-dns-best-practices.md`, `supporting-unqualified-domain-names.md` |
| P2P / NAT traversal | `peer-to-peer-communication-in-twingate.md`, `how-nat-traversal-works.md`, `local-peer-to-peer-best-practices.md` |
| Encryption, cryptography | `how-encryption-works-in-twingate.md` |
| VPN comparison, VPN replacement, performance | `twingate-vs-vpn.md`, `twingate-vs-mesh-vpns.md`, `twingate-performance.md`, `aws-vpn-replacement.md`, `vpn-replacement-use-case.md`, `diy-vpn-setup-guide.md` |
| Bastion replacement, cloaking | `bastion-replacement.md`, `cloak-your-bastion-server.md`, `strongdm-cloaking.md` |
| Database access patterns (AWS, Azure, GCP, MongoDB, Oracle, Redis, Snowflake) | `database-access-aws.md`, `database-access-azure.md`, `database-access-gcp.md`, `database-access-guide.md`, `database-access-mongodb.md`, `database-access-oracle.md`, `database-access-redis.md`, `database-access-snowflake.md` |
| AWS / cloud access patterns | `accessing-private-resources-in-azure.md`, `aws-cloudfront.md`, `aws-how-to-setup-subnets-for-secure-access.md`, `aws-workspaces.md` |
| App / SaaS protection & specialized access (Elasticsearch, legacy MFA, IP allowlisting, Windows SBL, site-to-site, staging, CI/CD) | `protect-access-to-elasticsearch-and-kibana.md`, `protect-legacy-apps-with-multi-factor-authentication.md`, `whitelisting-traffic-to-public-services.md`, `windows-sbl.md`, `site-2-site.md`, `access-control-for-staging-environments.md`, `cicd-pipelines-with-twingate.md` |
| Homelab & personal access | `homelab-personal-use-case.md`, `homelab-step-by-step.md`, `remotely-access-a-nas-device.md`, `remotely-access-a-coworkers-development-server.md`, `github-codespaces.md` |
| Game streaming | `game-streaming-remote.md`, `game-streaming-apollo.md`, `game-streaming-sunshine.md`, `game-streaming-duo.md` |
| Minecraft servers (homelab use case) | `minecraft-guides.md`, `minecraft-server.md`, `minecraft-server-linux.md`, `minecraft-bedrock-server.md`, `minecraft-bedrock-server-linux.md`, `minecraft-forge-server.md`, `minecraft-forge-server-linux.md` |
| AI / LLM / MCP access | `llms.md`, `remote-llm-access.md`, `remote-mcp-access.md` |
| Use-case overviews (infra access, internet security, device controls, IP-based) | `use-cases.md`, `guides.md`, `infra-access-use-case.md`, `internet-security-use-case.md`, `device-controls-use-case.md`, `ip-based-access-use-case.md`, `compliance-use-case.md` |
| Service accounts / headless services | `services.md` |
| Audit logs, network events, analytics, reporting | `audit-logs.md`, `audit-logs-schema.md`, `admin-console-export.md`, `network-events-ac-export.md`, `detailed-network-event-schema.md`, `network-summary-export.md`, `analytics.md`, `generating-insights-reports.md`, `exporting-network-traffic.md`, `user-activity.md`, `device-report.md`, `syncing-data-to-s3.md` |
| Client platform details (macOS, Windows, Linux, mobile, ChromeOS, MDM) | `clients.md`, `using-twingate.md`, `endpoint-requirements.md`, `macos.md`, `macos-and-ios.md`, `macos-standalone-client.md`, `linux.md`, `linux-headless.md`, `linux-userspace-networking.md`, `linux-device-id-migration.md`, `ios.md`, `android.md`, `chromeos.md`, `windows.md`, `windows-client-dotnet-8.md`, `windows-headless.md`, `deploy-twingate-client-with-microsoft-endpoint-manager.md` |
| Compliance frameworks & attestations (HIPAA, PCI, SOC 2, GDPR, DORA, FIPS) | `compliance-use-case.md`, `hipaa-compliance.md`, `twingate-hipaa.md`, `pci-compliance.md`, `twingate-pci.md`, `gdpr-compliance.md`, `soc-2.md`, `dora-compliance.md`, `dora-locations.md`, `twingate-fips140.md` |
| Security posture, trust center, disclosure, advisories | `twingate-security.md`, `trust-center.md`, `twingate-customer-data.md`, `service-reliability.md`, `responsible-disclosure-policy.md`, `vulnerability-reporting-acknowledgements.md`, `log4j-vulnerabilities-log4shell-cve-2021-44228-and-cve-2021-45046.md` |
| Open-source attributions & source | `open-source-software.md`, `open-source-attributions.md`, `oss-windows-client-application.md`, `oss-macos-and-ios-client-applications.md`, `oss-linux-client-application.md`, `oss-android-and-chromeos-client-applications.md` |
| Billing, subscription, admin console, team, notifications | `administration.md`, `admin-console-security.md`, `subscription-management.md`, `subscription-cancellation.md`, `upgrade-starter-to-home.md`, `notifications.md`, `team.md` |
| Product lifecycle, service status, support, FAQ | `release-stages.md`, `maintenance-events-service-status-outages.md`, `ubuntu-18-04-eol.md`, `support.md`, `faq.md` |
| MSP, multi-tenant, partner deployments | `msp.md`, `msp-billing.md` |
| Quick start / onboarding | `quick-start.md`, `automated-quick-start.md`, `digitalocean-getting-started.md` |

This table indexes every file in `references/` (~150 architecture-related
summaries). **Default to checking** — architectural details, compliance
scope, and use-case patterns evolve.
