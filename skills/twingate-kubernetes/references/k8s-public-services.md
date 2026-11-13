---
source: https://www.twingate.com/docs/k8s-public-services
type: docs
fetched: 2026-11-13
source_version: cce33c86de8cf82ac05e0602469fd6f9eef1fb0e5f65fa03044ef11e0850ab43
trust: official
---

# Publicly Exposed Resources in Kubernetes

## Summary
This page describes how to give external users access to a service running in a Kubernetes cluster while controlling that access through Twingate Resources and Group assignments. The service gets a non-public external IP, and a Connector deployed outside the cluster reaches it. Access is then granted through a Twingate Resource.

## Key Information
- **Use case:** Provide external access to a K8s service, governed by Twingate Resources and Group assignments.
- The Connector is deployed **outside** the target K8s cluster.
- The service's external IP must be external to the cluster but **not reachable from the public internet**.
- Private DNS can be used in place of the private IP address.
- The Twingate Resource points to the service's IP or private DNS address. Only authorized Twingate users can reach the service.

## Prerequisites
- A running K8s cluster with a service to expose.
- Ability to deploy a Twingate Connector outside the cluster.
- Ability to assign a non-public external IP to the K8s service.
- Network path from the Connector to that external IP.
- (Optional) Private DNS for the service.

## Step-by-Step
1. **Deploy Connector(s) outside the K8s cluster.** Ensure the Connector has network access to the service's external IP.
2. **Configure an external IP for the K8s service.** The IP must be outside the cluster, non-public, and reachable from the Connector. Optionally set up private DNS to use a hostname instead of the IP.
3. **Create a new Twingate Resource** using the service's IP or private DNS address. Assign it to the appropriate Groups.

## Configuration Values
No environment variables, CLI flags, or API parameters are given on this page. The only configuration inputs are:
- Resource address: service external (private) IP or private DNS name
- Group assignments on the Resource

## Gotchas
- Do not deploy the Connector inside the target cluster for this pattern.
- The service's external IP must not be exposed to the public internet, or the Twingate access control is bypassed.
- The Connector must be able to route to the service IP, so verify network reachability before creating the Resource.
- The page gives no specifics on how to assign the external IP (for example, the Service type or load balancer configuration). Those details depend on your cluster or cloud environment.

## Related Docs
- Twingate docs on deploying Connectors
- Twingate docs on creating Resources and assigning Groups
- Twingate docs on private DNS
- Other Twingate Kubernetes guides at https://www.twingate.com/docs/k8s-public-services