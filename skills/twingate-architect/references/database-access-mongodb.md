## MongoDB Access with Twingate

Twingate secures access to MongoDB Atlas and self-hosted MongoDB by routing connections through Connectors. For Atlas, the Connector's public IP is added to the Atlas IP Access List; for self-hosted instances, the Connector's private IP is used in firewall or mongod.conf bind rules. Atlas supports PrivateLink (AWS/Azure) and Private Service Connect (GCP) for fully private connectivity.

**Key Information**
- Atlas default port: TCP 27017; `mongodb+srv://` also requires UDP 53 for DNS SRV lookup
- Atlas IP Access List: add Connector public IP per Connector (Network Access in Atlas console)
- Atlas Admin Console (`cloud.mongodb.com`): separate org-level IP access list; Resource port 443
- Self-hosted: restrict with `net.bindIp` in `mongod.conf` or firewall rule from Connector private IP
- PrivateLink (AWS/Azure) / Private Service Connect (GCP): Connector connects to private endpoint; no public IP allowlisting needed
- `mongodb+srv://`: SRV-based discovery; requires DNS access (UDP 53) + TCP 27017 -- both must be in Resource definition
- `mongodb://`: connects directly to listed hosts/IPs; no DNS SRV required

**Prerequisites**
- Remote Network and Connector deployed
- MongoDB Atlas project/cluster or self-hosted MongoDB server
- Connector public IP (Atlas path) or private IP (self-hosted / PrivateLink path)

**Step-by-Step (Atlas)**
1. Create Resource: host `*.mongodb.net`, ports TCP 27017 + UDP 53; assign to groups
2. In Atlas -> Network Access, add Connector public IP for each Connector
3. Connect: `mongosh "mongodb+srv://cluster0.abc123.mongodb.net/mydb" --username <u> --password <p>`

**Step-by-Step (Self-hosted)**
1. Create Resource: MongoDB server IP or DNS, port 27017
2. Restrict firewall inbound to Connector private IP, or set `net.bindIp` in `mongod.conf`
3. Connect via `mongosh` with Twingate Client running

**Gotchas**
- **Connection string mismatch is the most common failure**: `mongodb+srv://` needs DNS (UDP 53); `mongodb://` does not -- confirm Resource covers both if using SRV
- Atlas IP Access List is per-project; Admin Console IP Access List is per-organization -- configure both if also securing admin access
- TLS is required by Atlas; enable TLS on self-hosted deployments as well
- If using PrivateLink/PSC, remove Connector public IP from Atlas IP Access List -- it is not needed

**Related Docs**
- /docs/database-access-guide
- /docs/saas-app-gating
- /docs/connector-best-practices
