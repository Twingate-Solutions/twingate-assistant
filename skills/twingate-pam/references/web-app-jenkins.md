---
source: https://www.twingate.com/docs/web-app-jenkins
type: docs
fetched: 2026-11-19
source_version: 3b837aea30ad69da6811d63cfb1bd5e7329f37356aead7322902417b73494b76
trust: official
---

# Jenkins SSO with Reverse Proxy Auth

## Summary
Twingate Privileged Access Management can handle both authentication and authorization in Jenkins with no code changes. The Gateway injects identity and Group headers, the Reverse Proxy Auth plugin reads them, and the Role-Based Strategy plugin maps Groups to Jenkins permissions. Setup is three plugins plus a JCasC file.

## Key Information
- Jenkins trusts headers set by the Twingate Gateway. Users are provisioned on first request, so there is no need to pre-create accounts.
- Permissions come from the Group header, so moving a user between Twingate Groups changes their Jenkins access on the next request.
- The Gateway overwrites any client-supplied `X-Forwarded-User` and `X-Forwarded-Groups`, so forged headers never reach Jenkins, provided the Resource is reachable only through the Gateway.
- Verified against `jenkins/jenkins:lts-jdk17`.

## Prerequisites
- Jenkins instance with administrator access (to install plugins and apply config)
- Twingate Web App Resource for Jenkins, network-isolated so the Gateway is the only path to it

## Step-by-Step
1. Install the plugins from Manage Jenkins → Plugins, or bake them into your image:
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
               permissions: ["Overall/Administer"]
               entries:
                 - group: "jenkins-admin"
             - name: "viewer"
               permissions: ["Overall/Read", "Job/Read", "View/Read"]
               entries:
                 - group: "jenkins-viewer"
   ```
   (Each role may also include a `description`.)
3. On the Jenkins Web App Resource, add request headers (below).
4. Create Twingate Groups named `jenkins-admin` and `jenkins-viewer`, or edit `entries` to match your existing Group names.

## Configuration Values
| Header Key | Value Template |
|---|---|
| `X-Forwarded-User` | `{{username}}` |
| `X-Forwarded-Groups` | `{{groups}}` |

| JCasC field | Purpose |
|---|---|
| `forwardedUser` | Header that carries the username |
| `headerGroups` | Header that carries the Group list |
| `headerGroupsDelimiter` | Must be `","` to match the Gateway |
| `entries` | Assigns a Group to a role |

To add a permission tier, add another role block with its own `permissions` and `entries`.

## Gotchas
- **Plugin ID:** use `reverse-proxy-auth-plugin`. `reverse-proxy-auth` returns a 404 in the update center.
- **Delimiter:** the plugin default is `|`, but the Gateway joins Groups with commas. Without `headerGroupsDelimiter: ","`, the whole list is read as one Group name.
- **Field names:** use `headerGroups`, not `forwardedGroups`. The `forwarded*` attributes are for display name and email.
- **Role assignment:** use `entries`. The older `assignments` form is rejected as deprecated.
- **Built-in Groups:** `{{groups}}` always includes `twingate:authenticated` and `Everyone`. They match no role entries and grant nothing, so don't use them as `entries` values.
- If Jenkins is reachable by any path other than the Gateway, the header trust model is not safe.

## Related Docs
- Privileged Access for Web Apps overview (architecture, all header template variables)
- Web App Integrations (shared trusted-header security model)
- Grafana integration guide (another trusted-header app)