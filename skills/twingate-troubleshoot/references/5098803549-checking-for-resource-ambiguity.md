---
source: https://help.twingate.com/articles/5098803549-checking-for-resource-ambiguity
type: help
fetched: 2026-09-06
source_version: 3d67dabfbb77c8e7d57d0afa2488050e6e24d5caaea48623cd7332525e178226
---

# Checking For Resource Ambiguity

## Page Title
Checking For Resource Ambiguity

## Summary
Twingate allows identical Resources (same IP, CIDR range, hostname, or FQDN) to be declared across multiple Remote Networks, which supports environments with overlapping address spaces. However, this can create ambiguity in Resource resolution, causing connectivity issues when Twingate cannot determine the correct network path.

## Key Information
- Each Resource is attached to a single Remote Network
- Identical Resources can exist across different Remote Networks (intentional feature)
- Ambiguity occurs during Resource resolution when Twingate cannot determine the correct network path for a given IP, hostname, or FQDN

## Ambiguity Conditions
Resource ambiguity exists when **both** of the following are true simultaneously:
- Identical Resources are mapped to different Remote Networks **AND** at least one Group grants access to identical Resources
- Users belong to Groups that contain those identical Resources

## Resolution
Follow the [Best Practices guide on overlapping IP addresses](https://help.twingate.com/articles/overlapping-ip-addresses) to resolve ambiguity issues.

## Gotchas
- Overlapping Resources across Remote Networks is a supported use case (e.g., multi-tenant or multi-VPC environments with shared RFC1918 space), but requires careful Group/access configuration
- Ambiguity is not just IP-based — hostnames and FQDNs can also create conflicts
- Connectivity issues from ambiguity may not produce obvious error messages; troubleshoot by auditing Group memberships and Resource assignments

## Related Docs
- Best Practices: Overlapping IP Addresses
- Twingate Troubleshooting Guide