---
source: https://help.twingate.com/articles/5098803549-checking-for-resource-ambiguity
type: help
fetched: 2026-08-06
source_version: d59b4d582281cd9513f1c52176d4889e1269b8df7caff14187101f373156cabe
---

# Checking For Resource Ambiguity

## Page Title
Checking For Resource Ambiguity

## Summary
Twingate allows identical Resources (same IP, CIDR range, or hostname) to be assigned to different Remote Networks, which is useful for overlapping subnets. However, this can create ambiguity in Resource resolution, causing connectivity issues when Twingate cannot determine the correct network path.

## Key Information
- Each Resource is attached to a single Remote Network
- Duplicate Resources across different Remote Networks are permitted by design
- Ambiguity occurs during Resource resolution for a given IP, hostname, or FQDN
- Ambiguity causes **connectivity issues**, not a hard configuration error

## Conditions That Trigger Ambiguity
Both of the following must be true simultaneously:
1. Identical Resources are mapped to different Remote Networks **AND** at least one Group grants access to those identical Resources
2. Users belong to Groups that contain those identical Resources

## Gotchas
- Overlapping Resources alone don't cause issues — the problem arises when Group access policies expose those overlapping Resources to the same users
- This is a silent failure mode; Twingate won't necessarily alert you to the ambiguity — it manifests as connectivity problems
- Affects IP addresses, CIDR ranges, hostnames, and FQDNs

## Resolution
Follow the **Best Practices guide on overlapping IP addresses** (linked within the Twingate help center) to resolve ambiguity.

## Related Docs
- Best Practices guide on overlapping IP addresses (Twingate internal link)
- Twingate Troubleshooting Guide