## Network Summary Export

Exports aggregate per-Resource connection statistics over a time range, rather than individual connection events. Same flow as Network Events export but with Report Type = Summary.

**Key Information:**
- Export path: Settings → Reports → Network Events tab → Generate Network Events Report → Report Type: Summary
- One row per Resource with aggregated stats across the selected time period
- Time range uses local timezone for selection; exported timestamps are UTC; filter uses connection end time
- Output: GZIP-compressed CSV; rename to `.csv` after decompression

**Summary Fields per Resource:**
- `resource_id`, `resource_address`, `remote_network`, `remote_network_id`
- `total_connections`, `success_connections`, `failed_connections`
- `failed_connections_dns`, `failed_connections_other` -- failure breakdown
- `total_bytes`, `bytes_transferred`, `bytes_received`
- `protocol` -- protocols used
- `percent_relay`, `percent_p2p` -- connection type distribution
- `top_10_address_accessed` -- top 10 addresses accessed within the Resource

**Gotchas:**
- `percent_relay` high on a Resource indicates P2P is failing -- investigate firewall or NAT traversal
- Safari auto-unpack may produce an empty file -- disable "Open 'safe' files after downloading" in Safari → Preferences → General

**Related Docs:**
- /docs/network-events-ac-export -- Per-connection event export
- /docs/detailed-network-event-schema -- Field schema reference
- /docs/syncing-data-to-s3 -- Continuous S3 sync
