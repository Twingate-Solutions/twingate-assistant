---
source: https://www.twingate.com/docs/web-app-jenkins
type: docs
fetched: 2026-08-14
source_version: 43e5e92a491b571e0331bc53133906b0ffc44baba6f680697acc8e0dee427c50
---

<!-- triage: unassigned -->

# Jenkins Integration with Twingate SSO

## Summary
Integrates Twingate Identity Firewall with Jenkins using the Reverse Proxy Auth plugin for authentication and Role-Based Strategy for authorization. The Gateway injects identity headers on every request, enabling SSO without code changes. Requires three plugins and a JCasC configuration file.

## Key Information
- Authentication via `X-Forwarded-User` header; authorization via `X-Forwarded-Groups` header
- Users are provisioned automatically on first request—no pre-created accounts needed
- Group membership changes take effect on the next request
- Gateway overwrites any client-supplied headers, preventing header forgery
- Built-in groups `twingate:authenticated` and `Everyone` are always included in `{{groups}}`—don't map roles to these

## Prerequisites
- Jenkins instance with admin access (verified against `jenkins/jenkins:lts-jdk17`)
- Twingate Web App Resource for Jenkins, network-isolated so Gateway is the only access path

## Step-by-Step

### 1. Install Plugins
Install from **Manage Jenkins → Plugins**:
- `configuration-as-code`
- `reverse-proxy-auth-plugin` (**not** `reverse-proxy-auth`—shorter name returns 404)
- `role-strategy`

### 2. Apply JCasC Configuration
```yaml
jenkins:
  securityRealm:
    reverseProxy:
      forwardedUser: "X-Forwarded-User"
      headerGroups: "X-Forwarded-Groups"
      headerGroupsDelimiter: ","
      disableLdapEmailResolver: true
  authorizationStrategy:
    roleBased:
      roles:
        global:
          - name: "admin"
            permissions:
              - "Overall/Administer"
            entries:
              - group: "jenkins-admin"
          - name: "viewer"
            permissions:
              - "Overall/Read"
              - "Job/Read"
              - "View/Read"
            entries:
              - group: "jenkins-viewer"
```

### 3. Configure Gateway Headers
On the Jenkins Web App Resource, add request headers:

| Header Key | Value Template |
|---|---|
| `X-Forwarded-User` | `{{username}}` |
| `X-Forwarded-Groups` | `{{groups}}` |

### 4. Map Twingate Groups
Create Twingate Groups matching `entries` values:

| Twingate Group | Jenkins Role | Permissions |
|---|---|---|
| `jenkins-admin` | admin | `Overall/Administer` |
| `jenkins-viewer` | viewer | `Overall/Read`, `Job/Read`, `View/Read` |

## Configuration Values
| Field | Value | Note |
|---|---|---|
| `forwardedUser` | `X-Forwarded-User` | Username header |
| `headerGroups` | `X-Forwarded-Groups` | Groups header (not `forwardedGroups`) |
| `headerGroupsDelimiter` | `","` | Must match Gateway's comma-joining of `{{groups}}` |

## Gotchas
- Use plugin ID `reverse-proxy-auth-plugin` exactly; `reverse-proxy-auth` returns 404
- Use `headerGroups` not `forwardedGroups` in JCasC (`forwarded*` fields are for display name/email)
- Use `entries` not `assignments` for role mappings (`assignments` is rejected as deprecated)
- Default delimiter is `|` but Gateway uses `,`—mismatch causes entire group list to be read as one group name
- Don't name role `entries` after `twingate:authenticated` or `Everyone`; use app-specific names like `jenkins-admin`

## Related Docs
- [Identity Firewall for Web Apps overview](https://www.twingate.com/docs/identity-firewall-web-apps) — all header template variables
- [Web App Integrations](https://www.twingate.com/docs/web-app-integrations) — trusted-header security model
- [Grafana integration guide](https://www.twingate.com/docs/web-app-grafana) — similar trusted-header pattern