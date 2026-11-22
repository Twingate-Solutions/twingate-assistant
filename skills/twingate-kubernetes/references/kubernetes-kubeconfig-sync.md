---
source: https://www.twingate.com/docs/kubernetes-kubeconfig-sync
type: docs
fetched: 2026-11-22
source_version: 5d2e8e8d8787240e483fa10a66ad3795c06f6e25cc41a61bfbe49128623440c9
trust: official
---

# Kubernetes Kubeconfig Sync

## Summary
The Twingate Client command `twingate kube config sync` writes standard kubeconfig contexts for every Kubernetes Cluster Resource a user or Service Account can access. This removes the need for cloud provider CLIs (`gcloud`, `doctl`, `aws eks`) to get cluster credentials. After syncing, `kubectl --context=<cluster-name>` works directly.

## Key Information
- Each Resource gets a context named after the cluster.
- Contexts are written to `~/.kube/config` by default, or to the path in `KUBECONFIG`.
- Contexts route kubectl traffic through the Twingate Client, then the Connector and Gateway, to the cluster.
- The contexts are standard, so Helm, Skaffold, k9s, Lens, etc. work unmodified.
- Autosync keeps kubeconfig current as Resources are added, removed, or changed. It is recommended for interactive use.
- In CI/CD, the Client runs headless with a Service Key. `twingate kube config sync` then works the same way.

## Prerequisites
- Twingate Client installed (macOS, Windows, or Linux).
- At least one Kubernetes Cluster Resource configured with Privileged Access for Kubernetes (https://www.twingate.com/docs/kubernetes-access).
- The user or Service Account has access to the Resource through a Twingate Group.
- Connector version 1.82.0 or later.

## Step-by-Step (interactive)
1. Make sure the Client is running and authenticated.
2. Run `twingate kube config sync`.
3. List contexts: `kubectl config get-contexts`.
4. Access a cluster: `kubectl --context=my-cluster get pods`.
5. Optional: `twingate kube config autosync on`.

## Commands
- `twingate kube config sync`: sync all Resources.
- `twingate kube config sync <resource-name>`: sync a single Resource without touching other contexts.
- `twingate kube config autosync on|off`: enable or disable automatic sync.
- `twingate status`: check Client state.

## Headless CI/CD Flow
1. Install the Twingate package. The page's examples add the Twingate apt repository and run `apt install twingate`. See the CI/CD Configuration page for the exact steps.
2. Set up headless mode by passing the Service Key on stdin: `twingate setup --headless=-`.
3. Run `sudo twingate start`.
4. Run `twingate kube config sync`, then use `kubectl --context=<cluster>`.

## Configuration Values
- `SERVICE_KEY`: CircleCI project environment variable holding the Service Key from the Admin Console.
- `TWINGATE_SERVICE_KEY`: GitHub Actions env var, populated from the `secrets.SERVICE_KEY` secret.
- `KUBECONFIG`: overrides the kubeconfig path.

## Gotchas
- No resources returned: the Client may not be authenticated, or the Resources are not assigned to the user's Group. Resources must be of type Kubernetes Cluster.
- Connection errors after sync: the Client is not running, or the Connector is offline or older than 1.82.0.
- The apt source line in the examples uses `[trusted=yes]`, which skips signature verification. Consider whether that fits your security posture.
- macOS-specific issues such as connection resets, TLS errors, and sync failures are covered in the Kubernetes troubleshooting page.

## Related Docs
- Privileged Access for Kubernetes (https://www.twingate.com/docs/kubernetes-access)
- CI/CD Configuration (https://www.twingate.com/docs/example-cicd-configurations)
- Linux Headless Mode (https://www.twingate.com/docs/linux-headless)
- Kubernetes Troubleshooting (https://www.twingate.com/docs/kubernetes-troubleshooting)