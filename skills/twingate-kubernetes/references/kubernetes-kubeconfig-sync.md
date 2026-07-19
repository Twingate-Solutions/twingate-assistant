# Kubernetes Kubeconfig Sync

## Summary
Twingate Client can automatically sync kubeconfig entries for Kubernetes Cluster Resources using `twingate kube config sync`, eliminating the need for cloud provider CLIs (gcloud, doctl, aws eks). Works for both interactive developer use and headless CI/CD pipelines with Service Keys.

## Key Information
- Writes standard kubeconfig contexts to `~/.kube/config` (or `$KUBECONFIG` path)
- Context name matches the cluster/resource name
- Compatible with any kubeconfig-aware tool (Helm, Skaffold, k9s, Lens)
- Works in headless mode for CI/CD with Service Accounts

## Prerequisites
- Twingate Client **v2025.175+** (macOS, Windows, Linux)
- Kubernetes Cluster Resource configured with **Privileged Access for Kubernetes**
- User/Service Account assigned to a Twingate Group with access to the Kubernetes Resource
- Connector version **1.82.0+**

## Step-by-Step (Interactive)
1. Ensure Twingate Client is running and authenticated
2. `twingate kube config sync`
3. `kubectl config get-contexts` — verify contexts
4. `kubectl --context=my-cluster get pods`
5. `twingate kube config autosync on` — optional, keeps kubeconfig current

## CLI Commands

| Command | Description |
|---|---|
| `twingate kube config sync` | Sync all accessible Kubernetes resources |
| `twingate kube config sync <resource-name>` | Sync single resource |
| `twingate kube config autosync on` | Enable automatic sync |
| `twingate kube config autosync off` | Disable automatic sync |
| `twingate status` | Verify client is running |

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
- `SERVICE_KEY` — Service Key from Admin Console (CircleCI env var)
- `secrets.SERVICE_KEY` — GitHub Actions secret name
- `KUBECONFIG` — env var to override default kubeconfig path (`~/.kube/config`)

## Gotchas
- Resources must be type **Kubernetes Cluster** (created via Kubernetes Operator with Privileged Access) — standard Resources won't appear
- If `sync` returns no resources: check `twingate status`, verify Group assignments, verify Resource type
- If `kubectl` fails after sync: Connector may be offline — check Admin Console
- Autosync recommended for interactive use; in CI/CD, run `sync` explicitly after starting the client

## Related Docs
- Privileged Access for Kubernetes
- CI/CD Configuration
- Linux Headless Mode