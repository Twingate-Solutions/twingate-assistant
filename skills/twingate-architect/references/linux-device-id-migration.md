## Linux Device ID Migration (v1.0.79)

One-time migration guide for Linux Client v1.0.79, which changed internal device ID generation. All Linux devices appear as new after upgrading; users with Trusted Profiles must re-verify their devices to maintain access.

**Key Information:**
- Affects: Linux Client v1.0.79 (stable release March 27, 2023; twingate-latest from March 15, 2023)
- Impact: existing device trust is lost after upgrade -- devices appear as new in Admin Console
- Only users with Trusted Profile requirements experience access interruption
- Old devices can be archived from Admin Console after all users have upgraded

**Migration Options:**
- **Small number of devices:** manually re-verify in Admin Console; optionally temporarily relax Trusted Profile requirements during transition
- **Large number of devices:** automate re-verification using the Twingate CLI

**CLI Automation:**
```bash
# Trust individual devices by serial or device ID
./tg device trust <deviceIdOrSerial>

# Batch trust from a serial number list
while read serial || [[ -n $serial ]]; do
  ./tg device trust "$serial"
done < serial-numbers.txt
```

**Bulk Migration Steps:**
1. Run `tg export` to get an XLSX with device info; extract trusted Linux device serial numbers
2. Write a batch trust script using the serial list
3. Schedule with cron (e.g., every 15 min) until all users have upgraded
4. Archive old devices from Admin Console after migration completes

**Gotchas:**
- Users on Trusted Profile-gated Resources lose access until their new device is re-verified
- Cron scheduling handles users who upgrade at different times

**Related Docs:**
- /docs/trusted-devices -- Trusted Profile configuration
- /docs/device-security-guide -- Device trust overview
- /docs/graphql-api -- API alternative for automation
