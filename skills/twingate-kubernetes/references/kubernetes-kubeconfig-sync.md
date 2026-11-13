---
source: https://www.twingate.com/docs/kubernetes-kubeconfig-sync
type: docs
fetched: 2026-11-13
source_version: 43a33f9f54b4e777e84614d2cda23a195d2f52ce198c334391589a22e52ab3a0
trust: official
---

# Kubernetes Kubeconfig Sync

## Summary
`twingate kube config sync` writes standard kubeconfig contexts for every Kubernetes Cluster Resource a user or Service Account can access. This removes the need for cloud provider CLIs (`gcloud`, `doctl`, `aws eks`) to get cluster credentials. After syncing, `kubectl --context=<cluster-name>` works directly.

## Key Information
- Each synced Resource gets a context named after the cluster.
- Contexts are standard Kubernetes contexts, so Helm, Skaffold, k9s, Lens, etc. work unmodified.
- Sync flow:
  1. The Client queries the Controller for accessible Kubernetes Cluster Resources.
  2. It writes a context per Resource to `~/.kube/config`, or to the path in `KUBECONFIG`.
  3. Each context routes kubectl traffic through the Client, Connector, and Gateway.
- Commands:
  - `twingate kube config sync` syncs all Resources.
  - `twingate kube config sync <resource-name>` syncs one Resource.
  - `twingate kube config autosync on|off` keeps kubeconfig updated as Resources are added, removed, or changed. Recommended for interactive use.
- Headless mode (CI/CD): start the headless Client with a Service Key, then run sync as usual.

## Prerequisites
- Twingate Client installed (macOS, Windows, or Linux).
- At least one Kubernetes Cluster Resource configured with Privileged Access for Kubernetes.
- The user or Service Account has access to the Resource via a Twingate Group.
- Connector version 1.82.0 or later.

## Step-by-Step (interactive)
1. Make sure the Client is running and authenticated.
2. Run `twingate kube config sync`.
3. List contexts: `kubectl config get-contexts`.
4. Access a cluster: `kubectl --context=my-cluster get pods`.
5. Optional: `twingate kube config autosync on`.

## Step-by-Step (CI/CD headless)
1. Install the Twingate Linux package. The page's examples add the apt repo `https://packages.twingate.com/apt/` and run `apt install twingate`; see the source page for the exact commands.
2. Pass the Service Key to `twingate setup --headless=-` via stdin, using `sudo`.
3. Run `sudo twingate start`.
4. Run `twingate kube config sync`.
5. Run kubectl with `--context=<cluster-name>`.

## Configuration Values
- `SERVICE_KEY`: CircleCI project environment variable holding the Service Key from the Admin Console.
- `TWINGATE_SERVICE_KEY`: GitHub Actions env var, populated from the `secrets.SERVICE_KEY` secret.
- `KUBECONFIG`: overrides the default kubeconfig path (`~/.kube/config`).
- `twingate setup --headless=-`: reads the Service Key from stdin.

## Gotchas
- **Sync returns no resources:**
  - The Client may not be running or authenticated. Check with `twingate status`.
  - The Resources may not be assigned to the user's Group.
  - The Resources must be type Kubernetes Cluster, set up via the Kubernetes Operator with Privileged Access.
- **kubectl connection errors after sync:**
  - The Client may not be running.
  - The Connector serving the Resource may be offline. Check the Admin Console.
  - The Connector may be older than 1.82.0.
- The page's example apt source uses `[trusted=yes]`, which skips signature verification. Consider whether that suits your environment.

## Related Docs
- Privileged Access for Kubernetes
- CI/CD Configuration
- Linux Headless Mode
- Twingate Client installation