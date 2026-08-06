---
source: https://www.twingate.com/docs/how-sessions-work
type: docs
fetched: 2026-08-05
source_version: 337accfb6faf3b5ed0e81f6abcf724396edbfcd9336d0353f812f4ed1220f487
---

# How Sessions Work

## Summary
Twingate uses two independent authentication timers—Sign In Policy and Resource Policy—to control re-authentication frequency. When timers expire, Twingate checks a stored IdP session copy before redirecting users to the IdP. Resource Policy re-authentications reset the Sign In Policy timer via a rolling window.

## Key Information
- **Sign In Policy session**: Global timer; expiry signs user out of Twingate Client entirely
- **Resource Policy session**: Per-resource timer; expiry blocks access to that resource's policy group
- Successful Resource Policy re-auth **resets** the Sign In Policy timer (rolling window)
- Device-only policies do **not** reset the Sign In Policy timer
- Twingate stores a copy of the user's IdP session internally; admins cannot configure this directly

## Re-authentication Flow
1. Timer expires → Twingate checks stored IdP session
2. **IdP session valid**: Browser briefly opens Twingate-hosted page, auto-completes re-auth (no user action unless MFA required)
3. **IdP session expired**: User redirected to IdP; all timers reset after successful auth

## Configuration Values
| Control | Recommended Value | Notes |
|---|---|---|
| Sign In Policy frequency | Up to 30 days | Acts as baseline gate only |
| Resource Policy (RDP/SSH) | 12–16 hours | Avoids mid-session disconnects |
| Resource Policy (web apps) | 12–16 hours | Adjust down for sensitive resources |
| Business-critical resources | Shorter than baseline | Based on org risk tolerance |

## IdP Session Lifetime
- **Enterprise IdPs** (Okta, Entra ID, Google Workspace, JumpCloud, OneLogin): Configurable by admin
- **Social IdPs** (Google, Microsoft, LinkedIn, GitHub): Fixed by provider, not configurable

## User Offboarding
**To revoke access within 5 minutes:**

**Enterprise IdP users:**
1. Block user's devices in Twingate (Admin Console or API) — enforced within 5 minutes
2. Suspend user in IdP + revoke active sessions — syncs to Twingate (up to 1 hour via SCIM)

**Social IdP users (no SCIM):**
1. Block user's devices in Twingate
2. Disable user in Twingate (Admin Console or API) — sessions revoked within ~5 minutes

**Deactivate vs. delete**: Deactivate/suspend in enterprise IdP rather than delete — preserves audit logs, same access revocation effect.

## Gotchas
- Other SSO applications accessed via Twingate manage their own sessions independently; Twingate does not influence their session state
- SCIM sync delays (up to 1 hour) mean device block + IdP suspension should be done together for enterprise IdP offboarding
- Device-only Resource Policies explicitly skip the rolling window extension for Sign In Policy
- Social IdP session lifetimes cannot be shortened by organizations

## Policy Design Rules
- Use **long Sign In Policy intervals**; it's a baseline gate, not the primary control
- Use **device-only policies** for system services/monitoring that need pre-login connectivity
- Shorter Resource Policy intervals for high-sensitivity resources regardless of connection type

## Related Docs
- Session Evaluation Walkthrough
- Device-only Resource Policies
- How to Offboard Users