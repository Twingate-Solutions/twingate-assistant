## CI/CD Configuration Examples

Sample CI/CD pipeline configurations using the Twingate **headless Client** + Service Account keys to access private Resources from build runners.

### GitHub Actions

**Marketplace Action**: ["Connect to Twingate"](https://github.com/marketplace/actions/connect-to-twingate) (linked from this doc).

The action does three things:
1. Installs the Twingate headless Client
2. Configures it with your Service Key (passed via env / secret)
3. Starts the Twingate Client

After the action completes, the workflow can reach any Resources assigned to the Service Account.

**Example `github-actions-demo.yaml`:**

```
name: Twingate on GitHub Actions Demo
on: [push]
jobs:
  Twingate-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - name: Install Twingate
        run: |
          echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list
          sudo apt update -yq
          sudo apt install -yq twingate

      - name: Setup and start Twingate
        env:
          TWINGATE_SERVICE_KEY: ${{ secrets.SERVICE_KEY }}
        run: |
          echo $TWINGATE_SERVICE_KEY | sudo twingate setup --headless=-
          sudo twingate start

      - name: Access a secure resource
        env:
          TEST_URL: http://business.prod.beamreachinc.int/
        run: curl -v $TEST_URL

      - name: Stop Twingate
        run: sudo twingate stop
```

### CircleCI

Three steps: install + start, test, stop. The `$SERVICE_KEY` is **base64-encoded** in CircleCI (required by their variable storage), then decoded before passing to `twingate setup`.

**Example `config.yaml`:**

```
version: 2.1
jobs:
  headless_client:
    machine:
      image: ubuntu:jammy-20250530
    steps:
      - run:
          name: Start Twingate
          command: |
            sudo apt update -yq
            sudo apt install -yq ca-certificates
            echo "deb [trusted=yes] https://packages.twingate.com/apt/ /" | sudo tee /etc/apt/sources.list.d/twingate.list
            sudo apt update -yq
            sudo apt install -yq twingate
            echo "$SERVICE_KEY" | base64 --decode | sudo twingate setup --headless=-
            sudo twingate start
            sudo journalctl -u twingate --no-pager | tail -n 20

      - run:
          name: Test Access
          command: |
            curl -v -m 10 "$TEST_URL" > /dev/null
            curl -v -m 10 http://twingate.com > /dev/null

      - run:
          name: Stop Twingate
          command: sudo twingate stop

workflows:
  test:
    jobs:
      - headless_client
```

### Configuration Values

| Variable | Purpose |
|---|---|
| `TWINGATE_SERVICE_KEY` (or `SERVICE_KEY`) | The Twingate Service Account JSON key, stored as a CI/CD secret |
| `TEST_URL` | A Resource only reachable through Twingate -- proves access works |

For CircleCI, the key is base64-encoded due to platform variable constraints; decode in the pipeline.

### Decision Notes

- Use one Service Account **per pipeline / repo** for clean audit and least-privilege scope
- Set short Service Key expiry + automate rotation via the Admin API for production
- Place the `twingate stop` step in a `cleanup` job that always runs (CI failures shouldn't leave the runner connected)
- Linux Client compatibility: tested on Ubuntu; other distros may not work -- pin Ubuntu base images

### Gotchas

- `apt update` failures are common on fresh runners; run `apt update -yq` again before install
- The headless setup `--headless=-` reads the JSON key from stdin -- the `echo $TWINGATE_SERVICE_KEY |` pattern is required
- CircleCI base64 wrap is unique to CircleCI; GitHub Actions doesn't need it
- Service Keys are sensitive -- always store as masked secrets, never in workflow files

### Related Docs

- /docs/services-headless-clients -- Headless Client modes overview
- /docs/cicd-pipelines-with-twingate -- Use case overview
- /docs/service-accounts-guide -- Service Account + Service Key management
- /docs/linux-headless -- Linux headless install details
- /docs/aws-ecs-headless-configurations -- ECS-specific pattern (sibling)
