<!-- triage: unassigned URL: https://www.twingate.com/docs/how-sessions-work -->

# How Sessions Work

## Summary
Twingate uses two independent authentication timers—Sign In Policy and Resource Policy—to control re-authentication frequency. Re-authentication leverages a stored IdP session copy to minimize user friction when possible. Understanding timer interactions and IdP session alignment is essential for balancing security with usability.

## Key Information
- **Sign In Policy session**: Baseline timer; expiry signs user out of Twingate Client entirely
- **Resource Policy session**: Per-resource timer; expiry requires re-auth before accessing that resource
- **Rolling window**: Successful Resource Policy re-authentication resets the Sign In Policy timer
- **Device-only policies** do NOT reset the Sign In Policy timer
- Twingate checks stored IdP session on timer expiry before redirecting to IdP
- Stored IdP session lifetime is controlled by the IdP, not Twingate

## Re-authentication Flow
| Stored IdP Session | Result |
|---|---|
| Still valid | Silent re-auth via Twingate-hosted page; no user action required (unless MFA mandated) |
| Expired | Redirect to IdP for full sign-in; all timers reset after success |

## Configuration Values
- **Sign In Policy default**: 30 days (recommended: keep long, up to 30 days)
- **Resource Policy recommended**: 12–16 hours for long-lived connections (RDP/SSH); shorter for high-sensitivity resources
- **Access revocation SLA**: ~5 minutes for device blocks and user disables

## User Offboarding (Step-by-Step)

**Enterprise IdPs:**
1. Block user's devices in Twingate (Admin Console or API) → enforced within 5 minutes
2. Suspend user in IdP and revoke active sessions → syncs to Twingate (up to 1 hour)

**Social IdPs (Google, Microsoft, LinkedIn, GitHub):**
1. Block user's devices in Twingate
2. Disable user in Twingate (Admin Console or API) → revokes sessions within ~5 minutes

## Gotchas
- Social IdP session lifetimes (Google, Microsoft, LinkedIn, GitHub social) cannot be configured by admins
- SCIM is not available for social IdP users—device block + Twingate disable are the only revocation mechanisms
- Deactivate (suspend) enterprise IdP users rather than delete to preserve audit logs
- Other SSO applications accessed through Twingate manage their own sessions independently; Twingate does not influence their session state
- Device-only Resource Policy access does not extend the Sign In Policy timer—users accessing only device-gated resources will eventually be signed out

## Policy Design Quick Reference
| Resource Type | Recommended Auth Frequency |
|---|---|
| Sign In Policy | Up to 30 days |
| RDP/SSH (long sessions) | 12–16 hours |
| Internal web apps | 12–16 hours |
| Business-critical/sensitive | Shorter (org risk tolerance) |
| System services/monitoring | Device-only policy |

## Related Docs
- Session Evaluation Walkthrough
- How to Offboard Users
- Device-only Resource Policies