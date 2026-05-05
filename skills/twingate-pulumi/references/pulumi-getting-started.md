## Getting Started with Pulumi and Twingate

Entry point for the Twingate Pulumi provider (`@twingate/pulumi-twingate`) -- IaC alternative to Terraform that lets you provision Twingate alongside cloud infrastructure using a real programming language (TypeScript/JavaScript shown in the docs; Python, Go, .NET also supported by Pulumi runtime).

**Prerequisites (all Pulumi guides):**
- Node.js installed (`node -v` to verify)
- Pulumi CLI installed (`pulumi version`) and connected to a Pulumi account (free tier OK)

**Cloud-Specific Guides:**
- /docs/pulumi-aws -- AWS (uses Twingate AMI)
- /docs/pulumi-azure -- Azure (uses Ubuntu VM + setup.sh)
- /docs/pulumi-gcp -- GCP (uses Ubuntu VM + setup.sh)

**Common Configuration Pattern:**
- `pulumi config set twingate:apiToken <token> --secret` -- encrypted in `Pulumi.<stack>.yaml`
- `pulumi config set twingate:network <tenant>` -- tenant subdomain
- Cloud creds via env vars or native CLI (e.g., `aws configure`, `az login`, `gcloud auth application-default login`)

**Twingate Pulumi Resource Pattern (TypeScript):**
```
import * as twingate from "@twingate/pulumi-twingate";

const network = new twingate.TwingateRemoteNetwork("demo", { name: "demo" });
const connector = new twingate.TwingateConnector("conn", { remoteNetworkId: network.id });
const tokens = new twingate.TwingateConnectorTokens("toks", { connectorId: connector.id });
const group = new twingate.TwingateGroup("g", { name: "demo group" });
const resource = new twingate.TwingateResource("r", {
  name: "demo server",
  address: server.privateIp,
  remoteNetworkId: network.id,
  accessGroups: [{ groupId: group.id }],
  protocols: { /* ... */ },
});
```

**Why Pulumi vs. Terraform:**
- Real programming language constructs (loops, functions, modules) for dynamic infrastructure
- Pulumi automatically encrypts secrets in state
- Same Twingate concepts as the Terraform provider; just different language ergonomics

**Open-Source Caveat:**
The Pulumi provider is community-maintained -- file issues at the GitHub repo (linked from each cloud guide). Production workloads should pin versions and have a fallback plan.

**Related Docs:**
- /docs/terraform-getting-started -- Terraform alternative
- /docs/api-overview -- Underlying GraphQL API
