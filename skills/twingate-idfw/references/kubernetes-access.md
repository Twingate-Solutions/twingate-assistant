---
source: https://www.twingate.com/docs/kubernetes-access
type: docs
fetched: 2026-11-13
source_version: 76240c7bf0d2d295937dbeab2eaf048cf74170a931b49155f18fd73a5bfb0979
trust: official
---

# Privileged Access for Kubernetes Overview

## Summary
Privileged Access for Kubernetes is the Kubernetes component of Twingate Identity Firewall. It places a Twingate Gateway (an L7 reverse proxy) in front of the cluster API server, so each `kubectl` request carries the user's Twingate identity and is authorized by native Kubernetes RBAC. Free for up to five resources.

## Key Information
- Replaces long-lived kubeconfig tokens and cloud CLI credentials (`gcloud`, `aws eks`, `doctl`) with Twingate identity.
- Keeps the API server private, with no public endpoint.
- Request flow: `kubectl → Twingate Client → Connector → Twingate Gateway → Kubernetes API server`.
- The Gateway impersonates the authenticated user, so Kubernetes RBAC and the Kubernetes audit log see the real identity.
- Setup via the Operator creates a Resource of type **Kubernetes Cluster** in the Admin Console, with Gateway-specific details.
- Available on macOS, Windows, and Linux only.
- AI agents and Service Accounts get scoped, revocable access (see AI Agent Access doc).

## Identity Sent to the Cluster
| Attribute | Value |
|---|---|
| Username | Twingate username, usually the email address |
| Groups | Twingate Groups granting access to the Resource, plus `twingate:authenticated` |

Kubernetes also adds `system:authenticated`. Use these as subjects in `RoleBinding` and `ClusterRoleBinding`. Verify with `kubectl auth whoami`.

## Prerequisites
- Twingate Remote Network for the cluster (note its ID)
- API key with **Read, Write & Provision** permissions
- Helm
- At least one Connector in the same Remote Network, version **1.82.0 or later**
- Existing `.kube` folder on the user's machine

## Step-by-Step
1. In the Admin Console, create a Remote Network and note its ID.
2. Create an API key with Read, Write & Provision permissions.
3. Install the Twingate Kubernetes Operator with the Gateway subchart enabled:
   `helm upgrade twop oci://ghcr.io/twingate/helmcharts/twingate-operator --install --wait -f ./values.yaml`
4. Deploy a Connector in the same Remote Network (for example, a `TwingateConnector` custom resource).
5. Grant users or Groups access to the Kubernetes Cluster Resource in the Admin Console.
6. Create Kubernetes RBAC bindings for those users or Groups.
7. Users sync kubeconfig in the Twingate Client, then run `kubectl auth whoami`.

## Configuration Values
- `values.yaml`: Operator Helm values (contents are in the Operator guide).
- Helm release name: `twop`
- Chart: `oci://ghcr.io/twingate/helmcharts/twingate-operator`
- Example kubeconfig context: `twingate-my-kubernetes-cluster`
- Session player: `https://www.twingate.com/sessionplayer`

## Auditing and Session Recording
- The Gateway logs all user actions and commands to `stderr` by default, or to a file if configured. Each entry is tied to a user identity.
- Logs are not uploaded to Twingate. They stay on your infrastructure, and admins export or store them.
- Format is asciicast v2. Replay `kubectl exec` sessions by pasting the log or uploading a file to the session player.

## Gotchas
- Connectors for Kubernetes Resources must be at least v1.82.0.
- The Twingate Client fails to sync if `.kube` is missing. Run `kubectl` once or create an empty folder first.
- Users can sync a specific Resource, all Resources, or enable auto-sync. Headless and CI/CD usage is covered in the Kubeconfig Sync doc.
- RBAC must be written against Twingate usernames and Groups, not cloud IAM identities.

## Related Docs
- Kubernetes Operator Identity Firewall user guide
- Gateway Kubernetes quick start guide
- Kubernetes Kubeconfig Sync
- AI Agent Access