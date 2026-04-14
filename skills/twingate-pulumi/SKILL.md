---
name: twingate-pulumi
description: |
  Twingate Pulumi provider for infrastructure as code. Use this skill when the
  user mentions Pulumi, wants to deploy Twingate with Pulumi, or has existing
  Pulumi code and wants to add Twingate. Trigger on 'Pulumi', 'pulumi-twingate',
  or when the user's codebase uses Pulumi.
---

# twingate-pulumi

## When to Use

Activate this skill when:
- The user asks about deploying Twingate with Pulumi
- The user has existing Pulumi infrastructure and wants to add Twingate resources
- The user mentions `pulumi-twingate`, `@pulumi/twingate`, or `pulumi_twingate`
- The user wants to manage Twingate remote networks, connectors, or resources as code using a non-Terraform IaC tool
- The user is migrating from Terraform and their target is Pulumi
- The user wants to integrate Twingate provisioning into an existing Pulumi stack

When generating or debugging Twingate Pulumi code, inspect `https://github.com/Twingate/pulumi-twingate` at runtime for current SDK examples and schema definitions. Also check the Pulumi Registry page at `https://www.pulumi.com/registry/packages/twingate/` for the latest published version and full resource documentation.

---

## Quick Reference

| Item | Value |
|---|---|
| Pulumi Registry | `https://www.pulumi.com/registry/packages/twingate/` |
| TypeScript/JS package | `@pulumi/twingate` |
| Python package | `pulumi_twingate` |
| Go module | `github.com/pulumi/pulumi-twingate/sdk/go/twingate` |
| .NET package | `Pulumi.Twingate` |
| Provider source | `https://github.com/Twingate/pulumi-twingate` |
| Reference programs | `https://github.com/Twingate-Solutions/pulumi-scripts` |
| API token env var | `TWINGATE_API_TOKEN` |
| Network env var | `TWINGATE_NETWORK` |
| Pulumi config key (token) | `twingate:apiToken` |
| Pulumi config key (network) | `twingate:network` |

---

## Evergreen Knowledge

### Provider Overview

The Twingate Pulumi provider is a bridge over the same Twingate GraphQL API used by the Terraform provider. Every resource available in Terraform has a direct Pulumi equivalent. The provider is published to the Pulumi Registry and supports all four major Pulumi language SDKs: TypeScript/JavaScript, Python, Go, and C#/.NET.

Because the Pulumi provider wraps the same underlying API, resource behavior, required fields, and limitations are identical to the Terraform counterpart. Use the `twingate-terraform` skill as a reference for resource semantics when provider documentation is ambiguous.

### Installing the Provider

**TypeScript / JavaScript**
```bash
npm install @pulumi/twingate
```

**Python**
```bash
pip install pulumi_twingate
```

**Go**
```bash
go get github.com/pulumi/pulumi-twingate/sdk/go/twingate
```

**C#/.NET**
```bash
dotnet add package Pulumi.Twingate
```

### Authentication and Configuration

The Twingate Pulumi provider requires two configuration values: the API token and the network name (the subdomain of your Twingate account, e.g. `acme` for `acme.twingate.com`).

**Permissions required for the API token:** Read, Write, and Provision. Generate the token in the Twingate Admin Console under Settings > API.

**Setting via environment variables (recommended for CI/CD):**
```bash
export TWINGATE_API_TOKEN="<your-token>"
export TWINGATE_NETWORK="<your-network-name>"
```

**Setting via Pulumi config (use `--secret` for the token):**
```bash
pulumi config set twingate:network acme
pulumi config set --secret twingate:apiToken <your-token>
```

Use `--secret` for the API token so Pulumi encrypts it in the stack state. Never store the token as a plain config value.

### Resource Parity with Terraform

All Terraform provider resources have Pulumi equivalents. Property names follow Pulumi SDK naming conventions (camelCase in TypeScript, snake_case in Python).

| Pulumi Resource | Terraform Equivalent | Notes |
|---|---|---|
| `twingate.RemoteNetwork` | `twingate_remote_network` | Location, name |
| `twingate.Connector` | `twingate_connector` | References remote network |
| `twingate.ConnectorTokens` | `twingate_connector_tokens` | Sensitive — mark as secret |
| `twingate.Resource` | `twingate_resource` | Services, port restrictions, group access |
| `twingate.Group` | `twingate_group` | User group for access policies |
| `twingate.ServiceAccount` | `twingate_service_account` | Non-human identity |
| `twingate.ServiceAccountKey` | `twingate_service_account_key` | Sensitive — mark as secret |

### Resource IDs

Twingate resource IDs returned by the provider are base64-encoded GraphQL global IDs, not human-readable strings. Do not construct or parse them manually. Always reference IDs through Pulumi output references (e.g., `connector.id`).

Example of a real ID: `Q29ubmVjdG9yOjEyMzQ1` (decodes to `Connector:12345`)

### Sensitive Outputs and Pulumi Secrets

Connector tokens and service account keys are sensitive values produced as outputs. Wrap them with `pulumi.secret()` in TypeScript or `pulumi.Output.secret()` in Python so Pulumi encrypts them in state. If you skip this step, the values appear in plaintext in the state file and any Pulumi Cloud output.

### Deployment Sequence

The correct order of operations mirrors the Terraform provider:

1. Configure the provider (API token + network name)
2. Create a `RemoteNetwork` for each network location
3. Create one or more `Connector` resources referencing the remote network
4. Create `ConnectorTokens` for each connector — these are the credentials the Connector process uses to authenticate
5. Pass connector tokens to compute resources (EC2 `userData`, Kubernetes `Secret`, Docker environment variables, etc.)
6. Create `Resource` records for each protected service, with port restrictions and protocol rules as needed
7. Create or look up `Group` records
8. Assign groups to resources via the `access` block on the `Resource`

---

## Common Patterns

### Pattern 1: Provider Configuration

**TypeScript**
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as twingate from "@pulumi/twingate";

// Provider reads TWINGATE_API_TOKEN and TWINGATE_NETWORK from env,
// or from Pulumi config set with:
//   pulumi config set twingate:network acme
//   pulumi config set --secret twingate:apiToken <token>
const provider = new twingate.Provider("twingate", {
    apiToken: process.env.TWINGATE_API_TOKEN,
    network: process.env.TWINGATE_NETWORK,
});
```

**Python**
```python
import os
import pulumi
import pulumi_twingate as twingate

provider = twingate.Provider("twingate",
    api_token=os.environ["TWINGATE_API_TOKEN"],
    network=os.environ["TWINGATE_NETWORK"],
)
```

If you set both environment variables and Pulumi config, Pulumi config takes precedence. In most CI/CD pipelines, environment variables are the cleaner approach — set them as pipeline secrets and do not commit the Pulumi config value for the token.

---

### Pattern 2: Remote Network + Connector + Tokens (the foundational trio)

Every Twingate deployment starts with this trio. Create a remote network, attach a connector, and generate tokens. The tokens are then passed to whatever compute resource runs the connector process.

**TypeScript**
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as twingate from "@pulumi/twingate";

// Remote network — logical grouping of connectors in one location
const network = new twingate.RemoteNetwork("prod-aws-us-east-1", {
    name: "prod-aws-us-east-1",
    location: "AWS",
});

// Connector — one per availability zone or redundancy group
const connector = new twingate.Connector("prod-connector-1", {
    remoteNetworkId: network.id,
    name: "prod-connector-1",
});

// Tokens — required to authenticate the connector process
const connectorTokens = new twingate.ConnectorTokens("prod-connector-1-tokens", {
    connectorId: connector.id,
});

// Wrap sensitive outputs as Pulumi secrets
const accessToken = pulumi.secret(connectorTokens.accessToken);
const refreshToken = pulumi.secret(connectorTokens.refreshToken);

// Export for use in compute resource (EC2 userData, K8s secret, etc.)
export const connectorAccessToken = accessToken;
export const connectorRefreshToken = refreshToken;
```

**Python**
```python
import pulumi
import pulumi_twingate as twingate

network = twingate.RemoteNetwork("prod-aws-us-east-1",
    name="prod-aws-us-east-1",
    location="AWS",
)

connector = twingate.Connector("prod-connector-1",
    remote_network_id=network.id,
    name="prod-connector-1",
)

connector_tokens = twingate.ConnectorTokens("prod-connector-1-tokens",
    connector_id=connector.id,
)

# Wrap as secrets so Pulumi encrypts them in state
access_token = pulumi.Output.secret(connector_tokens.access_token)
refresh_token = pulumi.Output.secret(connector_tokens.refresh_token)

pulumi.export("connector_access_token", access_token)
pulumi.export("connector_refresh_token", refresh_token)
```

---

### Pattern 3: Define a Resource with TCP Port Restrictions

Use the `protocols` block to restrict which ports and protocols are exposed. This is equivalent to Terraform's `protocols` block on `twingate_resource`.

**TypeScript**
```typescript
const appResource = new twingate.Resource("internal-app", {
    name: "Internal App Server",
    address: "10.0.1.50",
    remoteNetworkId: network.id,
    protocols: {
        allowIcmp: false,
        tcp: {
            policy: "RESTRICTED",
            ports: ["443", "8080-8090"],
        },
        udp: {
            policy: "DENY_ALL",
            ports: [],
        },
    },
    access: [{
        groupIds: [devGroup.id],
    }],
});
```

**Python**
```python
app_resource = twingate.Resource("internal-app",
    name="Internal App Server",
    address="10.0.1.50",
    remote_network_id=network.id,
    protocols=twingate.ResourceProtocolsArgs(
        allow_icmp=False,
        tcp=twingate.ResourceProtocolsTcpArgs(
            policy="RESTRICTED",
            ports=["443", "8080-8090"],
        ),
        udp=twingate.ResourceProtocolsUdpArgs(
            policy="DENY_ALL",
            ports=[],
        ),
    ),
    access=[twingate.ResourceAccessArgs(
        group_ids=[dev_group.id],
    )],
)
```

Port policy values:
- `"ALLOW_ALL"` — no restriction, all ports accessible
- `"RESTRICTED"` — only listed ports are accessible
- `"DENY_ALL"` — protocol completely blocked

---

### Pattern 4: Group-Based Access

Create or reference groups and attach them to resources via the `access` block. Groups map to Twingate's access policies and can be synced from your IdP via SCIM.

**TypeScript**
```typescript
// Create a new group
const devGroup = new twingate.Group("developers", {
    name: "Developers",
});

// Attach group to a resource
const devResource = new twingate.Resource("dev-db", {
    name: "Dev Database",
    address: "10.0.2.10",
    remoteNetworkId: network.id,
    protocols: {
        allowIcmp: false,
        tcp: {
            policy: "RESTRICTED",
            ports: ["5432"],
        },
        udp: {
            policy: "DENY_ALL",
            ports: [],
        },
    },
    access: [{
        groupIds: [devGroup.id],
    }],
});
```

To attach multiple groups, include each group ID in the `groupIds` array:
```typescript
access: [{
    groupIds: [devGroup.id, opsGroup.id, sreGroup.id],
}],
```

**Python**
```python
dev_group = twingate.Group("developers", name="Developers")

dev_resource = twingate.Resource("dev-db",
    name="Dev Database",
    address="10.0.2.10",
    remote_network_id=network.id,
    protocols=twingate.ResourceProtocolsArgs(
        allow_icmp=False,
        tcp=twingate.ResourceProtocolsTcpArgs(
            policy="RESTRICTED",
            ports=["5432"],
        ),
        udp=twingate.ResourceProtocolsUdpArgs(
            policy="DENY_ALL",
            ports=[],
        ),
    ),
    access=[twingate.ResourceAccessArgs(
        group_ids=[dev_group.id],
    )],
)
```

---

### Pattern 5: Wrapping Sensitive Outputs as Pulumi Secrets

Connector tokens and service account keys are sensitive. Apply `pulumi.secret()` (TypeScript) or `pulumi.Output.secret()` (Python) so Pulumi marks the value as secret in its state backend and masks it in CLI output.

**TypeScript — connector tokens**
```typescript
const tokens = new twingate.ConnectorTokens("connector-tokens", {
    connectorId: connector.id,
});

// Both values are sensitive — wrap both
const safeAccessToken = pulumi.secret(tokens.accessToken);
const safeRefreshToken = pulumi.secret(tokens.refreshToken);
```

**TypeScript — service account key**
```typescript
const serviceAccount = new twingate.ServiceAccount("ci-runner", {
    name: "CI Runner",
});

const saKey = new twingate.ServiceAccountKey("ci-runner-key", {
    serviceAccountId: serviceAccount.id,
    name: "ci-runner-key-2025",
});

const safeKey = pulumi.secret(saKey.token);
```

**Python — connector tokens**
```python
tokens = twingate.ConnectorTokens("connector-tokens",
    connector_id=connector.id,
)

safe_access_token = pulumi.Output.secret(tokens.access_token)
safe_refresh_token = pulumi.Output.secret(tokens.refresh_token)
```

Pass sensitive values downstream using `pulumi.Output.apply()` — do not `.get()` them into a plain string.

```python
# Correct: stay in Output chain
safe_access_token.apply(lambda t: do_something_with(t))

# Wrong: exposes plaintext
plain = tokens.access_token.get()  # do not do this
```

---

### Pattern 6: Passing Connector Tokens to an EC2 Instance (TypeScript)

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import * as twingate from "@pulumi/twingate";

const network = new twingate.RemoteNetwork("prod", { name: "prod", location: "AWS" });
const connector = new twingate.Connector("prod-connector", { remoteNetworkId: network.id });
const tokens = new twingate.ConnectorTokens("prod-tokens", { connectorId: connector.id });

const userData = pulumi.all([
    pulumi.secret(tokens.accessToken),
    pulumi.secret(tokens.refreshToken),
]).apply(([access, refresh]) => `#!/bin/bash
curl -s https://binaries.twingate.com/connector/setup.sh | \
  TWINGATE_ACCESS_TOKEN="${access}" \
  TWINGATE_REFRESH_TOKEN="${refresh}" \
  bash
`);

const instance = new aws.ec2.Instance("twingate-connector", {
    ami: "ami-0abcdef1234567890",
    instanceType: "t3.micro",
    userData: userData,
    tags: { Name: "twingate-connector" },
});
```

---

## Anti-Patterns

**Do not store connector tokens or service account keys in plain Pulumi config.**
```bash
# Wrong — token stored in plaintext in Pulumi state
pulumi config set twingate:apiToken abc123

# Correct — encrypted in state
pulumi config set --secret twingate:apiToken abc123
```

**Do not skip `pulumi.secret()` on sensitive outputs.**
If you export `connectorTokens.accessToken` directly without wrapping, the token appears in plaintext in `pulumi stack output`, in Pulumi Cloud history, and in state file backups. Always wrap sensitive `Output<string>` values with `pulumi.secret()`.

**Do not forget the network name config.**
The provider requires both `apiToken` and `network`. Omitting `network` (either the env var `TWINGATE_NETWORK` or `twingate:network` config) causes authentication errors that are often misread as token permission issues.

**Do not treat resource IDs as human-readable strings.**
Twingate resource IDs are base64-encoded GraphQL global IDs. Do not parse, construct, or hardcode them. Always chain resource references through Pulumi outputs (e.g., `connector.id`, `network.id`).

**Do not call `.get()` on sensitive outputs to pass them to other resources.**
Using `.get()` breaks the Pulumi secret tracking chain and may expose the value. Use `pulumi.all([...]).apply(...)` to compose multiple outputs safely.

---

## Related Skills

- **[twingate-architect](../twingate-architect/SKILL.md)** — Architecture background: how Twingate works, remote networks, connector design, and when to use multiple connectors for HA
- **[twingate-terraform](../twingate-terraform/SKILL.md)** — Terraform equivalent for all resources; use for resource parity reference when Pulumi docs are incomplete
- **[twingate-connectors](../twingate-connectors/SKILL.md)** — Connector deployment detail: Docker, systemd, Kubernetes, AWS, Azure, GCP
- **[twingate-kubernetes](../twingate-kubernetes/SKILL.md)** — K8s deployment integration: Helm chart, operator, how to pass connector tokens as a Kubernetes Secret
- **[twingate-api](../twingate-api/SKILL.md)** — Underlying GraphQL API: useful when Pulumi provider docs are incomplete or when you need to understand what a resource field maps to in the API
