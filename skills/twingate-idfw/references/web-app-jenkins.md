---
source: https://www.twingate.com/docs/web-app-jenkins
type: docs
fetched: 2026-11-13
source_version: fa9d96788d6deb8e25374e743b8b1ec8679f779eaf9b8c009396526716b41ef0
trust: official
---

# Jenkins SSO with Reverse Proxy Auth

## Summary
Twingate Gateway can drive both authentication and authorization in Jenkins using trusted headers. The Reverse Proxy Auth plugin reads the username and Groups from headers the Gateway injects, and the Role-Based Strategy plugin maps those Groups to Jenkins permissions. No code changes are needed, only three plugins and a JCasC file.

## Key Information
- Gateway injects `X-Forwarded-User` and `X-Forwarded-Groups` on every request.
- Users are provisioned on first request, so there is no need to pre-create accounts.
- Moving a user between Twingate Groups changes their Jenkins access on the next request.
- Verified against `jenkins/jenkins:lts-jdk17`.
- The Gateway overwrites client-supplied copies of these headers, so forged headers never reach Jenkins (provided Jenkins is reachable only through the Gateway).

## Prerequisites
- Jenkins instance with admin access (to install plugins and apply config).
- A Twingate Web App Resource for Jenkins, network-isolated so the Gateway is the only path to it.

## Step-by-Step
1. Install plugins (Manage Jenkins → Plugins, or bake into image):
   - `configuration-as-code`
   - `reverse-proxy-auth-plugin`
   - `role-strategy`
2. Apply this JCasC config:
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
               description: "Full administrative access (mapped from the 'jenkins-admin' group)."
               permissions:
                 - "Overall/Administer"
               entries:
                 - group: "jenkins-admin"
             - name: "viewer"
               description: "Read-only access (mapped from the 'jenkins-viewer' group)."
               permissions:
                 - "Overall/Read"
                 - "Job/Read"
                 - "View/Read"
               entries:
                 - group: "jenkins-viewer"
   ```
3. On the Jenkins Web App Resource, add request headers in Twingate:
   - `X-Forwarded-User` = `{{username}}`
   - `X-Forwarded-Groups` = `{{groups}}`
4. Create Twingate Groups named `jenkins-admin` and `jenkins-viewer` (or edit `entries` to match existing names).
5. To add a tier, add another role block with its own permissions and `entries`.

## Configuration Values
| Field | Purpose |
|---|---|
| `forwardedUser` | Header holding the username |
| `headerGroups` | Header holding the Group list |
| `headerGroupsDelimiter` | Must be `","` to match the Gateway |
| `entries` | Assigns a Group to a role |

| Twingate Group | Jenkins Role | Permissions |
|---|---|---|
| `jenkins-admin` | admin | Overall/Administer |
| `jenkins-viewer` | viewer | Overall/Read, Job/Read, View/Read |

## Gotchas
- Plugin ID is `reverse-proxy-auth-plugin`, not `reverse-proxy-auth` (the short name returns 404 in the update center).
- Use `headerGroups`, not `forwardedGroups`; the `forwarded*` attributes are for display name and email.
- Use `entries`; the older `assignments` form is rejected as deprecated.
- The plugin's default delimiter is `|`. Without `headerGroupsDelimiter: ","`, the whole comma-separated list is read as one Group name.
- `{{groups}}` always includes built-in `twingate:authenticated` and `Everyone`. They match no role `entries` and grant nothing, so don't name role entries after them.
- Jenkins must be network-isolated behind the Gateway, or the header trust model is unsafe.

## Related Docs
- Privileged Access for Web Apps overview (architecture, all header template variables)
- Web App Integrations (shared trusted-header security model)
- Grafana integration guide (another trusted-header app)