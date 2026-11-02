---
source: https://help.twingate.com/articles/5098803549-checking-for-resource-ambiguity
type: help
fetched: 2026-11-01
source_version: c02a3c7c2fc85ebe41a2c542d3b0b06f6366b79e52b795979f19e5a921113231
trust: official
---

# Checking For Resource Ambiguity

## Page Title
Checking For Resource Ambiguity

## Summary
Twingate allows identical Resources (same IP, CIDR, hostname, or FQDN) to be assigned to different Remote Networks, which is useful for environments with overlapping subnets. However, this can create ambiguity in Resource resolution, causing connectivity issues when Twingate cannot determine the correct network path.

## Key Information
- Each Resource is attached to exactly one Remote Network
- Duplicate Resources across Remote Networks are permitted by design
- Ambiguity occurs at resolution time when Twingate cannot identify the correct network path for a given IP, hostname, or FQDN

## Conditions That Trigger Ambiguity
- Identical Resources are mapped to different Remote Networks **and** at least one Group grants access to those identical Resources
- Users belong to Groups that contain identical (overlapping) Resources

## Gotchas
- Ambiguity is not a configuration error by itself — it only causes issues when Group access policies expose conflicting Resources to the same user
- Symptoms manifest as connectivity issues, not necessarily explicit error messages
- Overlapping CIDR ranges can cause the same ambiguity as identical exact-match Resources

## Resolution
Follow the **Best Practices guide on overlapping IP addresses** (linked from the original page) for detailed remediation steps.

## Related Docs
- Best Practices guide on overlapping IP addresses (referenced in-page)
- Twingate troubleshooting guide (parent document)