## Upgrade systemd Connectors (Linux)

Instructions for updating Twingate Connectors deployed as Linux systemd services, including manual and automated (cron) update methods.

**Check Current Version:**
```
twingate-connector -V
```

**Manual Update:**
- Ubuntu/Debian (apt):
  ```
  sudo apt update && sudo apt install -yq twingate-connector && sudo systemctl restart twingate-connector
  ```
- Fedora/CentOS (dnf):
  ```
  sudo dnf update && sudo dnf --best install twingate-connector && sudo systemctl restart twingate-connector
  ```

**Automated Updates — Simple Cron (Ubuntu weekly example):**
```bash
sudo tee -a /etc/cron.weekly/update-twingate-connector > /dev/null <<EOF
#!/bin/bash
sudo -- sh -c 'apt update && apt install -yq twingate-connector && systemctl restart twingate-connector'
EOF
sudo chmod +x /etc/cron.weekly/update-twingate-connector
```

**Automated Updates — Stay One Version Behind (advanced):**
- Downloads `keep-one-behind.sh` from Twingate-Solutions/general-scripts
- Identifies latest and second-latest APT versions; installs second-latest with downgrade support
- Useful for cautious rollout strategies
- Install as weekly cron at 2 AM Sunday; logs to `/var/log/keep-one-behind.log`

**Gotchas:**
- Never update all Connectors in a Remote Network simultaneously — stagger updates to maintain availability
- Schedule updates during off-peak hours

**Related Docs:**
- /docs/upgrading-connectors -- General upgrade principles
- /docs/connectors-on-linux -- systemd deployment reference
