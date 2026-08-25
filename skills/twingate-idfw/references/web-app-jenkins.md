---
source: https://www.twingate.com/docs/web-app-jenkins
type: docs
fetched: 2026-08-23
source_version: 650a7821393109f5e2dbb6fe5c6814b177c0782aaa1dd85e725ad4191f468ba2
---

# Jenkins SSO with Reverse Proxy Auth

## Summary
Integrate Twingate Identity Firewall with Jenkins using the Reverse Proxy Auth plugin for authentication and Role-Based Strategy for authorization. The Gateway injects identity headers on every request; Jenkins reads them to authenticate users and assign permissions based on Twingate Groups. No code changes required.

## Key Information
- Three plugins required: `configuration-as-code`, `reverse-proxy-auth-plugin`, `role-strategy`
- Users auto-provision on first request—no pre-created accounts needed
- Group membership changes take effect on the next request
- Gateway overwrites any client-supplied headers, preventing header forgery
- Built-in groups `twingate:authenticated` and `Everyone` are always included in `{{groups}}`—they grant no permissions unless explicitly mapped

## Prerequisites
- Jenkins instance with admin access (verified against `jenkins/jenkins:lts-jdk17`)
- Twingate Web App Resource configured for Jenkins, network-isolated so only the Gateway can reach it

## Step-by-Step

1. **Install plugins** via Manage Jenkins → Plugins:
   - `configuration-as-code`
   - `reverse-proxy-auth-plugin` (not `reverse-proxy-auth`—shorter name returns 404)
   - `role-strategy`

2. **Apply JCasC configuration file**

3. **Configure Gateway request headers** on the Jenkins Web App Resource

4. **Name Twingate Groups** to match `entries` values in JCasC

## Configuration Values

### JCasC File
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
            permissions: ["Overall/Administer"]
            entries:
              - group: "jenkins-admin"
          - name: "viewer"
            permissions: ["Overall/Read", "Job/Read", "View/Read"]
            entries:
              - group: "jenkins-viewer"
```

### Gateway Request Headers
| Header Key | Value Template |
|---|---|
| `X-Forwarded-User` | `{{username}}` |
| `X-Forwarded-Groups` | `{{groups}}` |

### Group-to-Role Mapping
| Twingate Group | Jenkins Role | Permissions |
|---|---|---|
| `jenkins-admin` | admin | `Overall/Administer` |
| `jenkins-viewer` | viewer | `Overall/Read`, `Job/Read`, `View/Read` |

## Gotchas
- Use `reverse-proxy-auth-plugin` (full artifact ID)—`reverse-proxy-auth` returns 404
- Use `headerGroups` field, not `forwardedGroups` (that's for display name/email)
- Use `entries` in JCasC, not `assignments` (deprecated, rejected)
- Set `headerGroupsDelimiter: ","` — plugin default is `|`, which would treat the entire comma-separated group list as one group name
- Avoid naming role entries `twingate:authenticated` or `Everyone`—use app-specific names like `jenkins-admin`

## Related Docs
- [Identity Firewall for Web Apps overview](https://www.twingate.com/docs/identity-firewall-web-apps) — all header template variables
- [Web App Integrations](https://www.twingate.com/docs/web-app-integrations) — trusted-header security model
- Grafana integration guide — similar trusted-header pattern