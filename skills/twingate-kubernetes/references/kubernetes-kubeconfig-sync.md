# Kubernetes Kubeconfig Sync

## Summary
Twingate Client's `twingate kube config sync` command automatically writes kubeconfig contexts for all Kubernetes Cluster Resources a user can access. Eliminates need for cloud provider CLIs (gcloud, doctl, aws eks) to obtain cluster credentials. Works for both interactive workstation use and headless CI/CD pipelines.

## Key Information
- Writes standard kubeconfig contexts to `~/.kube/config` (or `KUBECONFIG` path)
- Each cluster gets a context named after the cluster resource
- Compatible with any kubeconfig-aware tool (Helm, Skaffold, k9s, Lens, etc.)
- Works in headless mode with Service Keys for CI/CD

## Prerequisites
- Twingate Client **v2025.175+** (macOS, Windows, Linux)
- At least one Kubernetes Cluster Resource configured with Privileged Access for Kubernetes
- User/Service Account must have access via a Twingate Group
- Connector version **1.82.0+**

## CLI Commands

| Command | Description |
|---|---|
| `twingate kube config sync` | Sync all accessible K8s Cluster Resources |
| `twingate kube config sync <resource-name>` | Sync single resource by name |
| `twingate kube config autosync on` | Enable automatic kubeconfig updates |
| `twingate kube config autosync off` | Disable automatic updates |

## Configuration Values
- `KUBECONFIG` env var — override default kubeconfig path (`~/.kube/config`)
- `SERVICE_KEY` / `TWINGATE_SERVICE_KEY` — Service Key for headless/CI mode
- `--headless=-` flag — reads Service Key from stdin: `echo "$KEY" | sudo twingate setup --headless=-`

## Step-by-Step (Interactive)
1. Ensure Twingate Client is running and authenticated
2. `twingate kube config sync`
3. `kubectl config get-contexts` — verify contexts written
4. `kubectl --context=my-cluster get pods`
5. Optionally: `twingate kube config autosync on`

## Step-by-Step (CI/CD Headless)
1. Install Twingate via apt package
2. `echo "$SERVICE_KEY" | sudo twingate setup --headless=-`
3. `sudo twingate start`
4. `twingate kube config sync`
5. `kubectl --context=my-cluster <command>`

## Gotchas
- Resources must be type **Kubernetes Cluster** (set via Kubernetes Operator with Privileged Access) — regular TCP resources won't appear
- `sync` returns nothing if Client is unauthenticated or user has no K8s resources assigned
- Connector must be online for `kubectl` to work after sync
- Autosync recommended for interactive use; manual sync sufficient for CI/CD

## Troubleshooting
| Symptom | Fix |
|---|---|
| No resources returned | Run `twingate status`; verify Group assignments in Admin Console |
| kubectl connection errors | Check `twingate status`; verify Connector is online and v1.82.0+ |

## Related Docs
- Privileged Access for Kubernetes
- CI/CD Configuration
- Linux Headless Mode