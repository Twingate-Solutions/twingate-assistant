---
source: https://www.twingate.com/docs/k8s-helm-chart-upgrades
type: docs
fetched: 2026-11-13
source_version: a6afd3de0d3a395cc17fc7c3d266fe3d6a5e144428520f554db0b5aface88fd2
trust: official
---

# How to Upgrade Connectors Running in Kubernetes with Helm

## Summary
This page explains how to check the running version of a Twingate Connector in a Kubernetes Pod, update the Twingate Helm chart repo, and upgrade the Connector image. Updating the Helm chart alone does not upgrade running Connectors; a Pod restart pulls the latest image.

## Key Information
- Check the running Connector version by running `connectord --version` inside the Pod.
- The Twingate Helm chart changes infrequently, but it should be updated whenever Connectors are upgraded.
- Running `helm repo update twingate` refreshes the chart repo only. It does **not** upgrade the Connector image of active Pods.
- The official Twingate Helm chart sets image `pullPolicy: Always`. Restarting a Pod therefore pulls the latest Connector image and upgrades it.
- Latest build versions and update notes are in the Connector Release Notes.

## Prerequisites
- `kubectl` access to the cluster/namespace running the Connector
- Helm installed, with the `twingate` repo already added
- Connector deployed via the official Twingate Helm chart

## Step-by-Step
1. Check the current version:
   ```
   kubectl exec connector-1 -- ./connectord --version
   ```
   (`connector-1` is the Pod name; replace with yours.)
2. Compare against the latest version in the Connector Release Notes.
3. Update the Helm repo:
   ```
   helm repo update twingate
   ```
4. Restart the Connector Pod(s) so the latest image is pulled (works because `pullPolicy: Always`).

## Configuration Values
- `pullPolicy`: `Always` (default in the official chart); makes a Pod restart pull the newest image.
- Helm repo name: `twingate`
- Binary inside the Pod: `./connectord --version`

## Gotchas
- Updating the Helm chart does not upgrade running Connectors; the Pod must be restarted.
- If you override `pullPolicy` to something other than `Always`, a restart may not pull the newest image.
- Restarting a Pod briefly interrupts that Connector. Consider rolling restarts, or running multiple Connectors for availability, so they are not all restarted at once (general practice; not stated on the page).
- The page does not specify a restart command; use your standard method (e.g., deleting the Pod or a rollout restart on the Deployment).

## Related Docs
- Connector Release Notes
- Official Twingate Helm Chart
- Twingate Kubernetes Connector deployment docs