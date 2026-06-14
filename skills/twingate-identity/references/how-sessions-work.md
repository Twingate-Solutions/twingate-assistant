# How Sessions Work

## Summary
Twingate uses two independent authentication timers—Sign In Policy and Resource Policy—to control re-authentication frequency. When timers expire, Twingate checks a stored IdP session copy before deciding whether to silently re-authenticate or redirect to the IdP. Resource Policy re-authentications extend the Sign In Policy timer via a rolling window.

## Key Information
- **Sign In Policy session**: Controls baseline Twingate Client access; user is signed out when expired
- **Resource Policy session**: Per-resource timer; expires require re-auth before accessing that resource
- **Rolling window**: Successful Resource Policy re-auth resets the Sign In Policy timer to full duration
- **Device-only policies** do NOT reset the Sign In Policy timer
- Stored IdP session is internal—admins cannot configure it in Twingate; lifetime is set by the IdP

## Re-authentication Flow
- **Stored IdP session valid**: Silent browser re-auth (no user action required unless MFA mandated)
- **Stored IdP session expired**: User redirected to IdP; all timers reset after successful auth

## Configuration Values
| Control | Recommended Value | Notes |
|---|---|---|
| Sign In Policy | Up to 30 days | Acts as baseline, not primary control |
| Resource Policy (RDP/SSH) | 12–16 hours | Avoids mid-session disconnects |
| Resource Policy (web apps) | 12–16 hours | Shorter for high-sensitivity |

## User Offboarding (Access Revocation)

**Enterprise IdP users** — do both:
1. Block devices in Twingate (Admin Console or API) → enforced within **5 minutes**
2. Suspend user in IdP + revoke sessions → syncs to Twingate (up to **1 hour**)

**Social IdP users** (Google, Microsoft, LinkedIn, GitHub — no SCIM):
1. Block devices in Twingate
2. Disable user in Twingate → revoked within **5 minutes average**

## Gotchas
- Deactivate (suspend) rather than delete enterprise IdP users—preserves audit logs, identical access effect
- Social IdP session lifetimes cannot be controlled by the organization
- Other SSO-linked apps manage their own sessions independently; Twingate does not influence their session state
- Device-only policy access does NOT satisfy Sign In Policy auth requirements—timer does not roll

## Policy Design Best Practices
- Long Sign In Policy (30 days) reduces friction; Resource Policies are the primary security control
- Use device-only policies for system services/monitoring that need connectivity before user interactive login
- Business-critical resources warrant shorter Resource Policy intervals based on risk tolerance

## Related Docs
- Session Evaluation Walkthrough
- Device-only Resource Policies
- How to Offboard Users