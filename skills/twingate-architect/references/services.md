---
source: https://www.twingate.com/docs/services
type: docs
fetched: 2026-11-13
source_version: b97761489d9997da77cc34d80b2ed2a67c5a733dea5d34a854afabd7cca47a17
trust: official
---

# Services

## Summary
Twingate Services provide programmatic, centrally controlled access for automated processes such as CI/CD pipelines and custom applications. Resources are assigned to a Service, and access is authorized by a valid Service Key rather than Security Policies. The Linux or Windows client runs in headless mode to connect.

## Key Information
- Any Twingate Resource can be assigned to a Service, a User, or both.
- Security Policies do not apply to Services. Access is granted by a valid Service Key.
- Services are found in the Admin Console under Team > Services.
- Components:
  - **Service**: the container object holding configuration.
  - **Service Keys**: one or more keys; any non-revoked, non-expired key authorizes access to all Resources assigned to the Service.
  - **Resources**: one or more assigned Resources.
- Each Service Key is individually API rate-limited.

## Prerequisites
- Admin Console access to create Services.
- Existing Resources to assign.
- Twingate Linux or Windows client installed for headless use (see the headless mode guides).

## Step-by-Step: Create a Service
1. Go to Team > Services and select "Create Service Account".
2. Select "Generate Key" to create a Service Key.
3. Save the key immediately. It can only be viewed and copied once.
4. Select "Add Resource" to assign Resources to the Service.
5. Configure the Windows or Linux client in headless mode using the Service Key.

## Configuration Values
- **Service Key expiration**: set at creation only; default is 365 days; unlimited expiration is allowed.
- **Service Key name**: editable while the key is Active.

### Service Key lifecycle
| State | Allowed actions | Valid |
|---|---|---|
| Active | Revoke, edit name | Yes |
| Revoked | Delete | No |
| Expired | Delete | No |
| Deleted | None | No |

## Gotchas
- The Service Key is shown only once at creation. If lost, generate a new one.
- Any valid key grants access to all Resources on the Service, so scope Resources carefully.
- Avoid overprovisioning keys: since each key is rate-limited individually, use a unique key per high-traffic system to prevent throttling.
- Expiry cannot be changed after creation.
- Keys must be revoked before deletion. Revoked keys cannot be reactivated, and deleted keys cannot be recovered.
- Default 365-day expiry means keys will stop working unless rotated or created with unlimited expiration.

## Related Docs
- Headless mode configuration guide for Linux
- Headless mode configuration guide for Windows
- Twingate Resources and Admin Console documentation