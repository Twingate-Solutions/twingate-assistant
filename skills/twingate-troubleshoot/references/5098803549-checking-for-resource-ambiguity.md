---
source: https://help.twingate.com/articles/5098803549-checking-for-resource-ambiguity
type: help
fetched: 2026-10-04
source_version: cce133f54b0096d2353eaea966898046561019ca314cb2f3449ae283d9fe3152
trust: official
---

# Checking For Resource Ambiguity

## Page Title
Checking For Resource Ambiguity

## Summary
Twingate allows identical Resources (same IP, CIDR range, hostname, or FQDN) to be declared across multiple Remote Networks, which is useful for environments with overlapping subnets. However, this can create ambiguity in Resource resolution, causing connectivity issues when Twingate cannot determine the correct network path.

## Key Information
- Each Resource is attached to exactly one Remote Network
- Identical Resources can exist across different Remote Networks (by design)
- Ambiguity occurs at resolution time when Twingate cannot determine which network path to use
- Ambiguity affects: IP addresses, CIDR ranges, hostnames, and FQDNs

## Conditions That Trigger Ambiguity
- Identical Resources are mapped to different Remote Networks **AND** at least one Group grants access to those identical Resources
- Users belong to Groups that contain identical Resources across different Remote Networks

## Symptoms
- Connectivity issues when accessing Resources
- Inconsistent or failed Resource resolution

## Resolution
Follow the **Best Practices guide on overlapping IP addresses** (linked from the Twingate help center) for detailed remediation steps.

## Gotchas
- Ambiguity only becomes a problem when access permissions overlap — having identical Resources in different Remote Networks is not inherently problematic until Group access policies create conflicting resolution paths
- This is a configuration/policy issue, not a network infrastructure issue

## Related Docs
- Twingate Best Practices: Overlapping IP Addresses
- Twingate Troubleshooting Guide