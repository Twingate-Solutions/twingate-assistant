## Services (Service Accounts)

Service Accounts provide programmatic, non-interactive access to Twingate Resources for automated processes like CI/CD pipelines and applications. Access is authorized by a Service Key -- Security Policies do not apply to Services.

**Key Information:**
- Service Keys authorize access to all Resources assigned to the Service; no Security Policy is evaluated
- Service Keys expire after 365 days by default; unlimited expiration can be configured at creation time
- Each Service Key is individually API rate-limited -- use a unique Service Key per high-traffic system to avoid throttling
- A Service Key can only be viewed/copied once at creation time -- store it securely immediately
- Found under Team > Services in the Admin Console

**Service Key Lifecycle:**
- `Active` -- valid and usable; name editable; expiry set at creation only
- `Revoked` -- invalid; cannot be reactivated; must be deleted separately
- `Expired` -- automatically expired; cannot be reactivated
- `Deleted` -- permanent; not recoverable

**Step-by-Step:**
1. Navigate to Team → Services → Create Service Account
2. Click Generate Key → copy and securely store the Service Key (shown once only)
3. Click Add Resource to assign Resources to the Service

**Gotchas:**
- Overprovisioning Service Keys causes API rate limiting -- provision one Service Key per high-traffic system, not many keys sharing one Service
- Revocation is required before deletion; revoked keys cannot be reactivated
- Security Policies do not apply to Services -- all Resources on the Service are accessible to any valid key

**Related Docs:**
- /docs/linux-headless -- Using Service Keys with headless Linux Client
- /docs/windows-headless -- Using Service Keys with headless Windows Client
- /docs/linux-userspace-networking -- Userspace (HTTP proxy) mode for containers
