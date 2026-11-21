---
source: https://www.twingate.com/docs/kubernetes-access
type: docs
fetched: 2026-11-19
source_version: d9c66d636029ad46a5f192e6c689b413a18e56db1b0b02ba0667413f2cdf9aa4
trust: official
---

# Privileged Access for Kubernetes Overview

## Summary
Privileged Access for Kubernetes is the Kubernetes component of Twingate Privileged Access Management. A Twingate Gateway (Layer 7 reverse proxy) sits in front of the cluster API server and impersonates the authenticated Twingate user. Kubernetes RBAC and audit logs therefore see the real identity, and kubectl activity is audited and replayable.

## Key Information
- Request flow: `kubectl → Twingate Client → Connector → Twingate Gateway → Kubernetes API server`.
- Replaces long-lived kubeconfig tokens and cloud CLI credentials (gcloud, aws eks, doctl). The API server can stay private.
- Identity sent to the cluster:
  - **Username:** Twingate username (usually the email).
  - **Groups:** the Twingate Groups granting access to the Resource, plus `twingate:authenticated`. Kubernetes also adds `system:authenticated`.
- Use these usernames and Groups as subjects in `RoleBindings` and `ClusterRoleBindings`.
- Setup via the Operator creates a Resource of type **Kubernetes Cluster** in the Admin Console, with Gateway details.
- Audit logs go to `stderr` by default (can be configured to write to a file). They are not uploaded to Twingate and stay on your infrastructure.
- Session recordings use asciicast v2 format. Replay at https://www.twingate.com/sessionplayer by pasting the log or uploading a file.
- AI agents and Service Accounts get a different identity (see AI Agent Access docs).
- Free for up to five resources.
- Supported client platforms: macOS, Windows, Linux only.

## Prerequisites
- Twingate Remote Network for the cluster (note its ID).
- API key with **Read, Write & Provision** permissions.
- Helm.
- At least one Connector in the same Remote Network, version **1.82.0 or later**.
- An existing `.kube` folder on user machines.

## Step-by-Step
1. In the Admin Console, create a Remote Network and note its ID.
2. Create an API key with Read, Write & Provision permissions.
3. Install the Twingate Kubernetes Operator with the Gateway subchart enabled:
   `helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml`
   The operator deploys the Gateway, registers it, and creates the Kubernetes Cluster Resource.
4. Deploy a Connector in the same Remote Network (e.g., via a `TwingateConnector` custom resource).
5. Grant users or Groups access to the Kubernetes Cluster Resource in the Admin Console.
6. Create Kubernetes RBAC bindings for those users or Groups.
7. Users sync kubeconfig in the Twingate Client (single Resource, all Resources, or auto-sync), then verify:
   `kubectl --context twingate-my-kubernetes-cluster auth whoami`

## Configuration Values
- `values.yaml` for the Helm chart (contents are in the Operator PAM user guide and the Gateway quick start, not on this page).
- Helm release name used in the example: `twop`.
- Chart: `oci://ghcr.io/twingate/helmcharts/twingate-operator`.
- kubectl context naming: `twingate-<cluster-resource-name>`.

## Gotchas
- Connectors for Kubernetes Resources must be ≥ 1.82.0.
- Syncing kubeconfig fails if `.kube` doesn't exist. Run `kubectl` once or create an empty folder.
- Access requires both Twingate Resource access and a matching Kubernetes RBAC binding.
- Logs are not retained by Twingate, so you must export or store them yourself.

## Related Docs
- Kubernetes Operator Privileged Access Management user guide
- Gateway Kubernetes quick start guide
- Kubernetes Kubeconfig Sync (including headless and CI/CD usage)
- AI Agent Access
- Twingate Privileged Access Management