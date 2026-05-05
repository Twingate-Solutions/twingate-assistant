## Helm Chart and Connector Upgrades

How to update the Twingate Helm chart and the Connector container image running in pods. The two are decoupled.

**Check Connector Version:**
```
kubectl exec <pod-name> -- ./connectord --version
```
Compare against the latest version in /docs/connector-release-notes.

**Update the Helm Chart:**
```
helm repo update -n twingate
```
The chart itself changes infrequently -- still update before bumping Connector versions.

**Update the Connector Image:**
- The chart sets `image.pullPolicy: Always`
- Simply **delete or restart the pod** -- the new pod pulls the latest Connector image automatically
- Example: `kubectl rollout restart deployment/twingate-connector -n <namespace>`

**Key Behaviour:**
- `helm repo update` and `helm upgrade` change chart-level settings (replicas, resources, labels) but do not refresh container images on running pods
- Pod restart is the trigger that fetches the latest image (because of `pullPolicy: Always`)
- Pin image tags (`image.tag=1.X.Y`) for production to avoid silently rolling forward on pod restart -- updates become explicit version bumps in your Helm values

**Recommended Order:**
1. `helm repo update` -- pull latest chart version
2. `helm upgrade --install twingate-connector twingate/connector -n <ns> -f values.yaml` -- apply any chart changes
3. `kubectl rollout restart deployment/twingate-connector -n <ns>` -- restart pods to pull the new Connector image

**Gotchas:**
- A failing rollout can leave the cluster without a working Connector -- run multiple Connector replicas per Remote Network for HA so one can be upgraded at a time
- If `pullPolicy` is changed to `IfNotPresent`, image updates require explicit tag changes (no implicit upgrades on restart)
- Don't manually delete/recreate pods unless the chart's deployment is the only owner -- prefer `kubectl rollout restart`

**Related Docs:**
- /docs/k8s-helm-chart -- Initial install
- /docs/upgrading-connectors -- General Connector upgrade strategy
- /docs/connector-release-notes -- Latest Connector version + release notes
