## Google Cloud Database Access with Twingate

Twingate routes traffic to Cloud SQL, AlloyDB, Memorystore, Spanner, Bigtable, and Firestore through secure Connectors. The preferred path uses Private Service Connect (PSC) or Private Service Access (PSA) so all traffic stays on Google's internal network fabric. When private connectivity is unavailable, Connector public IPs are added to Authorized Networks.

**Key Information**
- Supported services: Cloud SQL (MySQL/PostgreSQL/SQL Server), AlloyDB, Memorystore (Redis/Memcached), Spanner, Bigtable, Firestore
- Default ports: MySQL 3306, PostgreSQL 5432, SQL Server 1433, Redis 6379
- Private path: Connector in same VPC as database; use private IP or PSC endpoint
- Public path: add Connector public IP in `/32` CIDR to Authorized Networks
- Memorystore: only accessible via internal IP; requires VPC Network Peering at creation time
- API-only services (BigQuery, Spanner): create a PSC endpoint inside your VPC
- Cloud Console gating: no native IP allowlist; gate via SSO/SaaS App Gating

**Prerequisites**
- Remote Network and Connector deployed (same VPC or peered VPC for private path)
- Cloud SQL instance, AlloyDB cluster, Memorystore instance, or other GCP database
- Connector private IP (PSC/private path) or public IP (Authorized Networks path)

**Step-by-Step (Private IP / PSC)**
1. Enable Private IP on instance: Cloud SQL -> Instance -> Connections -> Networking; disable Public IP
2. Create Twingate Resource: private IP or private DNS name, correct port, assign to groups
3. Connect: `psql -h <private-ip> -U <user> -d <db>` or equivalent client

**Step-by-Step (Public / Authorized Networks)**
1. Create Twingate Resource: public IP or FQDN of database, correct port
2. Add Connector public IP in `/32` to Authorized Networks in GCP Console
3. Connect with Twingate Client running

**Gotchas**
- Memorystore instances must be created with VPC Network Peering; it cannot be added after creation
- PSC/PSA requires Connector in the same or peered VPC -- cross-project peering needs explicit configuration
- Authorized Networks fallback exposes a public endpoint; restrict to Connector IPs only, never 0.0.0.0/0

**Related Docs**
- /docs/database-access-guide
- /docs/database-access-aws
- /docs/saas-app-gating
