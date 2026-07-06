# How Sessions Work

## Summary
Twingate controls authentication frequency via two independent timers: the Sign In Policy session and per-Resource Policy sessions. Re-authentication checks a stored IdP session copy before redirecting users to the IdP. The Sign In Policy uses a rolling window that resets on successful Resource Policy re-authentication.

## Key Information
- **Sign In Policy**: Global timer; when expired, user is signed out of Twingate Client entirely
- **Resource Policy**: Per-resource timer; expiry requires re-auth before continuing resource access
- **Stored IdP session**: Captured at last sign-in; used to silently re-authenticate if still valid (no user action required unless MFA mandated)
- **Rolling window**: Successful Resource Policy re-auth resets the Sign In Policy timer to full duration
- **Device-only policies do NOT reset the Sign In Policy timer**

## Prerequisites
- Enterprise IdP (Okta, Entra ID, Google Workspace, JumpCloud, OneLogin) for configurable IdP session lifetimes
- Social IdPs (Google, Microsoft, LinkedIn, GitHub): session lifetimes fixed by provider

## Re-authentication Flow
1. Timer expires → Twingate checks stored IdP session
2. **IdP session valid**: Browser briefly opens Twingate-hosted page, confirms session silently, timers reset
3. **IdP session expired**: User redirected to IdP login; all Twingate timers reset after success

## Configuration Values
| Setting | Recommended Value | Notes |
|---|---|---|
| Sign In Policy frequency | Up to 30 days | Acts as baseline gate only |
| Resource Policy (RDP/SSH) | 12–16 hours | Avoids mid-session disconnects |
| Resource Policy (web apps) | 12–16 hours | Adjust down for high sensitivity |
| Business-critical resources | Shorter (org-defined) | Risk-tolerance dependent |

## User Offboarding (Revocation)

**Enterprise IdP users** (revoke within ~5 min):
1. Block user's devices in Admin Console or API (effective within 5 min)
2. Suspend user in IdP + revoke active sessions (SCIM sync; up to 1 hour)

**Social IdP users** (no SCIM):
1. Block devices in Twingate
2. Disable user in Admin Console or API (~5 min average)

**Note**: Deactivate/suspend in IdP rather than delete—preserves audit logs, same access revocation effect.

## Gotchas
- Twingate does **not** influence session state of other SSO-linked apps accessed through Twingate
- Device-only Resource Policies skip authentication—they do **not** satisfy Sign In Policy auth requirements and won't extend its timer
- IdP session lifetime is an implicit variable admins may overlook; a short IdP session causes more frequent full IdP redirects even with long Twingate timers
- For social IdPs, SCIM is unavailable—device blocking and manual Twingate user disable are the only fast revocation paths

## Policy Design Quick Reference
| Resource Type | Recommended Frequency |
|---|---|
| Sign In Policy | 30 days |
| RDP/SSH servers | 12–16 hours |
| Internal web apps | 12–16 hours |
| High-sensitivity resources | Shorter (risk-based) |
| System services/monitoring | Device-only policy |

## Related Docs
- Session Evaluation Walkthrough
- How to Offboard Users
- Device-only Resource Policies
- Sign In Policy configuration
- Resource Policy configuration