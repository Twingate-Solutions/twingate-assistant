---
source: https://www.twingate.com/docs/tags
type: docs
fetched: 2026-11-13
source_version: 24ec91ef42086d8363411cb8968a3486231db5a7ea195d2ba763cc3c1c456282
trust: official
---

# Page Title
Resource Tags (Twingate Docs)

## Summary
Tags are key-value metadata pairs attached to Twingate Resources. They add context (owner, application, environment) and let admins filter Resources in the Admin Console. They can be managed in the Admin Console or through the Twingate API.

## Key Information
- Each tag is a key-value pair (e.g., `owner` = `devops`).
- Tags are used to label Resources and to filter the Resource table quickly.
- Tags can be managed from the Admin Console or the Twingate API.
- Terraform, Pulumi, and the Kubernetes operator support is described as "coming soon." With those tools, tags could be imported from AWS or GCP.
- While you type, the Admin Console suggests existing keys and values from your Network.

## Prerequisites
- An existing Twingate Network with Resources.
- Admin Console access, or API access, with permission to edit Resources.

## Step-by-Step

**Add tags (Admin Console)**
1. Create or edit a Resource.
2. Click **Add Tag**.
3. Set the key, then the value.
4. Repeat as needed, then save the Resource. Tags are saved when the Resource is saved.

**Remove a tag:** click the remove icon to the right of the tag.

**Filter by tags**
1. Go to **Network → Resources**.
2. Use the **Tags** filter and click **Select Key**.
3. Choose **in** (include) or **not in** (exclude).
4. Select the values to filter on.

## Configuration Values (Tag Constraints)
- Maximum 64 tags per Resource.
- Only one tag per key on a Resource.
- Keys and values are case sensitive and may contain any valid UTF-8 character.
- Keys and values cannot start or end with whitespace. Leading and trailing whitespace is trimmed automatically.
- Keys cannot start with `tg` (e.g., `tg_remote_network` is prohibited).
- Key length: 1–128 characters.
- Value length: 1–256 characters.

**Common keys:**
- Ownership: `owner`, `managed_by` (e.g., `admin_console`, `terraform`, `pulumi`, `k8s_operator`).
- Technical: `application`, `environment`, `location`, `region`.

## Gotchas
- A tag's key or value can only be set when the tag is created. To change one, remove the tag and add a new one.
- Case sensitivity means `Owner` and `owner` are different keys. Pick a convention and stick to it.
- Avoid near-duplicate keys such as `owner` and `owner-team`.
- Keys starting with `tg` are reserved and rejected.
- Terraform, Pulumi, and Kubernetes operator support is not yet available per the page, so use the API for automation.

## Best Practices
- Use a consistent, standardized set of keys across all Resources.
- Tag every Resource so filtering gives complete results.
- Use tags for varied context: technical details, ownership, and security requirements.

## Related Docs
- Resources
- Twingate API
- Terraform provider, Pulumi, and Kubernetes operator docs
- Admin Console: Network → Resources