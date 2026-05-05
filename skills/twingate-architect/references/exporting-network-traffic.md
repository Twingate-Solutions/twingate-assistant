## Network Traffic Export

Overview of the four ways to view and export Connector-routed network activity in Twingate. Only traffic flowing through deployed Connectors is captured; Twingate does not see other internet-bound traffic.

**Export Methods:**
- **Admin Console viewer** -- per-User or per-Resource event view with filters (Resource, user, date, activity type)
- **CSV export** -- manual export from Admin Console (Settings → Reports)
- **AWS S3 sync** -- continuous JSON stream to an S3 bucket
- **Real-time Connector logging** -- live output from the Connector process via advanced config

**Log Retention by Plan:**
- Starter: 24 hours
- Teams: 7 days
- Business: 30 days
- Enterprise: 12 months

**Gotchas:**
- Client IP is not shown in the Admin Console viewer (planned for future release)
- Access-denied events are indistinguishable from non-existent Resources -- zero-trust design means clients only know about Resources they can access; denied access looks the same as "doesn't exist"

**Related Docs:**
- /docs/detailed-network-event-schema -- CSV and JSON field schemas
- /docs/network-events-ac-export -- CSV export walkthrough
- /docs/syncing-data-to-s3 -- S3 sync setup
