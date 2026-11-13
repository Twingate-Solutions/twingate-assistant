---
source: https://www.twingate.com/docs/example-cicd-configurations
type: docs
fetched: 2026-11-13
source_version: 46e94bbee7af7551e43289b08f116f1a853e8dd1970b5be405aefc4ba1c82ec5
trust: official
---

# CI/CD Configuration (Twingate)

## Summary
Twingate provides sample CI/CD configurations (GitHub Actions and CircleCI) that install the Twingate headless Client, authenticate it with a Service Key, and give pipeline jobs access to Resources assigned to that Service. Samples live in a public GitHub repo and are covered by Twingate's automated testing. Treat them as guides, not production-ready configs.

## Key Information
- A published "Connect to Twingate" GitHub Action (GitHub Marketplace) installs the headless Client, configures it with your Service Key, and starts it.
- The examples install the Linux Client from the Twingate apt repo (`https://packages.twingate.com/apt/`) using a `deb [trusted=yes]` source entry.
- Once connected, the job can reach Resources assigned to the Service.
- Pipeline pattern: install, setup and start, test access, stop.
- Versions of software and container images in the samples may be outdated; check official docs.

## Prerequisites
- A Twingate Service Account and Service Key, with the target Resources assigned to that Service.
- The Service Key stored as a CI secret (`SERVICE_KEY` in the examples).
- A Debian/Ubuntu-based runner (the Linux Client may not work on other distributions).
- sudo access on the runner.

## Step-by-Step (GitHub Actions)
1. Add the apt source list entry for `packages.twingate.com`, run `sudo apt update`, then `sudo apt install twingate`.
2. Set `TWINGATE_SERVICE_KEY` from `secrets.SERVICE_KEY`. Run `echo "$TWINGATE_SERVICE_KEY" | sudo twingate setup --headless=-`, then `sudo twingate start`.
3. Optionally run `twingate status` and `journalctl -u twingate` for diagnostics.
4. Access protected Resources (e.g. `curl -v $TEST_URL`).
5. Run `sudo twingate stop` at the end.

## Step-by-Step (CircleCI)
1. Use `machine` executor with image `ubuntu-2204:current`.
2. Install `ca-certificates`, add the apt source, and install `twingate`.
3. Run `echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-`, then `sudo twingate start`.
4. Collect logs with `sudo journalctl -u twingate --no-pager | tail -n 20`.
5. Test with `curl -v -m 10 "$TEST_URL"` against a protected Resource and a public one.
6. Run `sudo twingate stop`, then confirm public access still works.

## Configuration Values
- `SERVICE_KEY` / `TWINGATE_SERVICE_KEY`: the Service Key (JSON) secret.
- `TEST_URL`: a URL for a Resource reachable only while Twingate is connected.
- `twingate setup --headless=-`: reads the Service Key from stdin.
- `twingate start`, `twingate stop`, `twingate status`: Client control commands.

## Gotchas
- CircleCI requires the Service Key to be stored base64 encoded; decode it before passing to `twingate setup`.
- The Linux Client may not be compatible with non-Ubuntu/Debian distributions.
- `[trusted=yes]` in the apt source skips signature verification. Consider stronger verification for production.
- Use `-m 10` timeouts on curl tests so failed connections don't hang the pipeline.
- Follow your own security best practices before using these samples in production.

## Related Docs
- Twingate Services and Service Keys
- Twingate Linux headless Client
- "Connect to Twingate" GitHub Action (GitHub Marketplace)
- Twingate public GitHub repo of CI/CD sample configs