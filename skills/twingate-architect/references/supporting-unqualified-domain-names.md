---
source: https://www.twingate.com/docs/supporting-unqualified-domain-names
type: docs
fetched: 2026-11-13
source_version: 268dbcc97d6284b05c93b9114a3cdde78079028e45bbf3ad05a57c833d4d3325
trust: official
---

# Supporting Unqualified Domain Names

## Summary
Twingate only permits connections to FQDNs by default. To use short names (e.g., `http://employeeportal`), define the unqualified name as its own Resource and set a DNS search domain on the machine running the Connector.

## Key Information
- Add the unqualified name as a **separate Resource in addition to** the FQDN, not instead of it. Defining only one can cause connection errors.
- The unqualified name must be its own Resource because Twingate uses split-tunneling. Without it, the Client does not know to intercept traffic for that name.
- The Connector uses the search domains configured on its host machine. No Connector restart is needed for changes to take effect.

## Prerequisites
- Admin Console access to create Resources.
- Administrative access to the Connector host (VM, container, or ECS task).

## Step-by-Step
1. In the Admin Console, create two Resources, e.g., `employeeportal` and `employeeportal.yourcompany.com`.
2. Set the search domain on the Connector host (see the per-platform instructions below).

### AWS ECS
Set it under **Network Settings** in **Advanced Container Configuration** when adding or editing a container instance.

### Docker (non-ECS)
Before running the generated deploy script, add this flag before `--restart=unless-stopped`:
```
--dns-search yoursearchdomain.com
```

### Ubuntu
1. Edit `/etc/systemd/resolved.conf` and set `Domains=yourcompany.com`.
2. Run `sudo systemctl restart systemd-resolved`.

### CentOS / Fedora
1. Run `nmcli dev status` to find the Connection used for Internet access.
2. Run `sudo nmcli con mod "YOUR CONNECTION NAME" ipv4.dns-search "yourcompany.com"`.
3. Run `sudo systemctl restart NetworkManager`.

## Configuration Values
- Docker flag: `--dns-search <domain>`
- Ubuntu: `Domains=` in `/etc/systemd/resolved.conf`
- NetworkManager: `ipv4.dns-search`
- Twingate virtual IP range: `100.96.0.0/12`

## Gotchas
- In the `nmcli` command, use the Connection name, not the Device name. Keep the quotation marks.
- Browsers may treat a bare name as a search term. Type the full `http://employeeportal` the first time. The browser usually remembers it afterward.

## Troubleshooting Checklist
1. On the Connector host, run `nslookup employeeportal`. If it does not resolve there, it will not work through Twingate.
2. On a Client device, run the same lookup. It should return an IP in `100.96.0.0/12`.
3. If the Resource is a web page, enter it with the `http://` prefix.

## Related Docs
- Twingate Connector deployment guides (Docker, AWS ECS, Linux)
- Twingate Resource configuration in the Admin Console