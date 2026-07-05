# Kubernetes Kubeconfig Sync

## Summary
The `twingate kube config sync` command automatically writes standard kubeconfig contexts for every Kubernetes Cluster Resource a user has access to. This eliminates the need for cloud provider CLIs (gcloud, doctl, aws eks) to obtain cluster credentials. Works for both interactive workstation use and headless CI/CD pipelines.

## Key Information
- Writes to `~/.kube/config` by default, or path specified by `KUBECONFIG` env var
- Context names match the cluster/resource name
- Works with any kubeconfig-aware tool: Helm, Skaffold, k9s, Lens, etc.
- Autosync keeps kubeconfig current as resources change (recommended for interactive use)
- Headless mode uses Service Keys for CI/CD authentication

## Prerequisites
- Twingate Client version **2025.175 or later** (macOS, Windows, Linux)
- At least one Kubernetes Cluster Resource configured with Privileged Access for Kubernetes
- Connector version **1.82.0 or later**
- User/Service Account must have access via a Twingate Group
- Resources must be type `Kubernetes Cluster` (set up via Kubernetes Operator with Privileged Access)

## Step-by-Step (Interactive)
1. Ensure Twingate Client is running and authenticated
2. `twingate kube config sync`
3. `kubectl config get-contexts` — verify contexts
4. `kubectl --context=my-cluster get pods`
5. (Optional) `twingate kube config autosync on`

## CLI Commands
```bash
twingate kube config sync                    # sync all accessible K8s resources
twingate kube config sync <resource-name>    # sync single resource
twingate kube config autosync on             # enable automatic sync
twingate kube config autosync off            # disable automatic sync
twingate status                              # verify client is running/connected
```

## CI/CD Setup Pattern
```bash
# Install
echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list
sudo apt update -yq && sudo apt install -yq twingate

# Start headless
echo "$SERVICE_KEY" | sudo twingate setup --headless=-
sudo twingate start

# Sync and use
twingate kube config sync
kubectl --context=my-cluster get pods
```

## Configuration Values
| Variable | Description |
|---|---|
| `SERVICE_KEY` | Service Key from Twingate Admin Console (CI/CD) |
| `KUBECONFIG` | Custom kubeconfig path (overrides `~/.kube/config`) |

## Gotchas
- No resources returned: Client may not be authenticated OR resources aren't assigned to user's Group OR resources aren't type `Kubernetes Cluster`
- Connection errors after sync: Client not running or Connector is offline — check `twingate status` and verify Connector is online in Admin Console
- Connector must be **1.82.0+** for Privileged Access to function

## Related Docs
- Privileged Access for Kubernetes
- CI/CD Configuration
- Linux Headless Mode