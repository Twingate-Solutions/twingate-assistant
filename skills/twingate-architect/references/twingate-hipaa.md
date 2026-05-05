## Twingate & HIPAA

Detailed legal and technical explanation of why Twingate does not require a HIPAA Business Associate Agreement (BAA), and the conditions under which a BAA review is available.

**Core Position:**
- Twingate asserts it is not a "business associate" under HIPAA due to the conduit exception (similar to ISPs and the U.S. Postal Service)
- Twingate relays only route encrypted, transient traffic; no PHI is stored, decrypted, or inspected
- P2P connections (preferred) don't touch Twingate infrastructure at all; relays are a fallback only
- Control plane (admin operations, auth) does not involve PHI

**Conduit Exception:**
- DHHS guidance classifies conduit services (routing without processing or storing) as excluded from business associate status
- Applies to both covered entities and subcontractors of business associates

**BAA Review (limited availability):**
- Twingate will review customer-provided BAAs under two conditions: (1) BAA scope limited to where HIPAA actually applies; (2) liability tied to main services agreement limits
- Available only for annual plans above $75,000

**Related Docs:**
- /docs/hipaa-compliance -- HIPAA overview and contact
- /docs/twingate-security -- Security architecture details
- /docs/twingate-customer-data -- How Twingate handles data
