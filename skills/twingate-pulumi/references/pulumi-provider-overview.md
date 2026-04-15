<!-- initial seed — to be refreshed by pipeline -->

## Page Title
Twingate Pulumi Provider

## Summary
The Twingate Pulumi provider allows teams to manage the full Twingate resource hierarchy — networks, connectors, resources, access policies, groups, and service accounts — as infrastructure code using any Pulumi-supported language. It wraps the Twingate GraphQL API, meaning any change made through Pulumi is equivalent to a change made in the Admin Console.

## Key Information
- **Supported languages:** TypeScript/JavaScript, Python, Go, .NET (C#/F#), Java, and Pulumi YAML — the provider ships SDKs for all Pulumi-supported runtimes
- **Provider package name:** `twingate` on the Pulumi Registry; install per language (e.g., `pip install pulumi-twingate` for Python, `npm install @pulumi/twingate` for TypeScript)
- **Authentication:** Requires two values — `TWINGATE_API_TOKEN` (a Twingate API key with Admin scope) and `TWINGATE_NETWORK` (the account subdomain, e.g., `mycompany` for `mycompany.twingate.com`)
- **Key resources:** `twingate.TwingateRemoteNetwork`, `twingate.TwingateConnector`, `twingate.TwingateResource`, `twingate.TwingateResourceAccess`, `twingate.TwingateGroup`, `twingate.TwingateServiceAccount`, `twingate.TwingateServiceAccountKey`
- **State backends:** Works with Pulumi Cloud (managed state + secrets), self-managed backends (S3, Azure Blob, GCS), or local state for development; no Twingate-specific constraints on state backend choice
- **Drift detection:** `pulumi refresh` reconciles Pulumi state against live Twingate API state, catching out-of-band Admin Console changes

## Prerequisites
- Pulumi CLI installed (v3.x+)
- A Twingate account with API access enabled
- An API token generated from the Twingate Admin Console (Settings > API)
- `TWINGATE_API_TOKEN` and `TWINGATE_NETWORK` set as environment variables or Pulumi config secrets
- Language runtime installed for your chosen Pulumi language (Node.js, Python 3.9+, Go 1.21+, etc.)

## Step-by-Step
1. Install the Pulumi CLI and create a new project: `pulumi new typescript` (or `python`, `go`, etc.)
2. Install the Twingate provider SDK for your language:
   - TypeScript: `npm install @pulumi/twingate`
   - Python: `pip install pulumi-twingate`
   - Go: `go get github.com/twingate/pulumi-twingate/sdk/go/twingate`
3. Install the provider plugin: `pulumi plugin install resource twingate`
4. Set authentication config:
   ```
   pulumi config set twingate:apiToken <token> --secret
   pulumi config set twingate:network mycompany
   ```
   Or export environment variables: `export TWINGATE_API_TOKEN=<token> && export TWINGATE_NETWORK=mycompany`
5. Declare a Remote Network, Connector, and Resource in your Pulumi program (see example pattern below)
6. Preview changes: `pulumi preview`
7. Deploy: `pulumi up`
8. Verify in Twingate Admin Console that the network, connector, and resource appear correctly
9. Retrieve connector tokens from state output and configure the connector service with them

## Configuration Values
```
twingate:apiToken: <API token — mark as secret>
twingate:network: <subdomain only, e.g. "mycompany" not "mycompany.twingate.com">

# Common resource properties
TwingateRemoteNetwork.name: string (display name)
TwingateRemoteNetwork.location: "AWS" | "AZURE" | "GCP" | "ON_PREMISE" | "OTHER"
TwingateResource.address: string (DNS name or CIDR, e.g. "10.0.0.0/8" or "db.internal")
TwingateResource.remoteNetworkId: reference to TwingateRemoteNetwork.id
TwingateConnector.remoteNetworkId: reference to TwingateRemoteNetwork.id
TwingateResourceAccess.resourceId: reference to TwingateResource.id
TwingateResourceAccess.principalId: group ID or service account ID
```

## Gotchas
- **Network subdomain only:** `TWINGATE_NETWORK` must be the subdomain alone (`mycompany`), not the full hostname (`mycompany.twingate.com`) — the provider appends the domain automatically
- **Connector tokens are not in state:** The Pulumi provider creates the connector object in Twingate but connector access tokens must be retrieved from the Admin Console or via the Twingate API separately — they are not exposed as Pulumi outputs for security reasons
- **`TwingateResourceAccess` is the access glue:** Creating a `TwingateResource` does not grant any access by itself; you must also create `TwingateResourceAccess` resources binding groups or service accounts to each resource
- **API token scope:** The token used for the provider must have Admin-level API access; read-only or restricted tokens will fail on resource creation with a 403
- **Pulumi Cloud vs self-managed state:** Pulumi Cloud encrypts secrets by default; with self-managed backends you must configure a passphrase or KMS key — the API token stored in Pulumi config is a secret and must be encrypted at rest
- **Import existing resources:** Use `pulumi import twingate:index/twingateResource:TwingateResource my_resource <twingate-resource-id>` to bring existing Twingate resources under Pulumi management without recreating them

## Related Docs
- `/docs/reference/pulumi-provider` — Official Twingate Pulumi provider reference
- `/docs/guides/terraform-provider` — Terraform alternative for HCL-based IaC workflows
- `/docs/reference/api` — Twingate GraphQL API (the underlying API the provider calls)
- `/docs/guides/service-accounts` — Service account and service account key management
- `/docs/guides/remote-networks` — Remote Network concepts and location types
