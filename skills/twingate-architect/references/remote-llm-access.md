# Remote LLM Access with Twingate

## Summary
Securely connect a local development machine to a self-hosted or cloud-hosted LLM server using Twingate as a zero-trust network layer. Traffic is routed through a Twingate Connector on the LLM server, eliminating the need to expose any public ports. Example uses Ollama + VS Code Continue extension.

## Key Information
- Twingate Connector on the remote server initiates outbound-only connections — no inbound firewall rules required
- LLM server (Ollama) binds only to `localhost`/internal IP, never `0.0.0.0`
- Twingate client on local machine intercepts traffic to defined Resources and tunnels it automatically
- Works with any cloud provider (DigitalOcean, AWS, GCP, Azure) or on-prem server
- Applies beyond VS Code: JetBrains, Cursor, any Continue-supported editor

## Prerequisites
- Twingate account (free tier available)
- Remote Linux server with GPU (e.g., DigitalOcean GPU droplet)
- Ollama installed on remote server
- VS Code with Continue extension (local machine)
- Twingate client installed locally

## Step-by-Step

1. **Install Ollama on remote server**
   ```bash
   curl https://ollama.ai/install.sh | sh
   ollama run llama3
   ```
   Ollama defaults to `localhost:11434` — leave it there.

2. **Create Twingate network** in admin console → add Remote Network (On-Premise or cloud)

3. **Deploy Connector** on remote LLM server:
   ```bash
   curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
     TWINGATE_ACCESS_TOKEN="{token}" \
     TWINGATE_REFRESH_TOKEN="{token}" \
     TWINGATE_NETWORK="{network_name}" \
     TWINGATE_LABEL_DEPLOYED_BY="linux" bash
   ```

4. **Define Resource** in Twingate admin:
   - Address: internal IP of LLM server
   - Port: `11434`
   - Protocol: TCP
   - Assign access to relevant users

5. **Install Twingate client** locally, sign in

6. **Configure Continue** (`config.json`):
   ```json
   {
     "models": [{
       "title": "My Secure Llama3",
       "provider": "ollama",
       "model": "llama3",
       "apiBase": "http://{internal_ip}:11434"
     }]
   }
   ```

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Ollama default port | `11434` |
| Ollama bind address | `localhost` (do NOT use `0.0.0.0`) |
| Continue `provider` | `ollama` |
| Continue `apiBase` | `http://{internal_ip}:11434` |
| Connector env: `TWINGATE_ACCESS_TOKEN` | From Twingate admin console |
| Connector env: `TWINGATE_REFRESH_TOKEN` | From Twingate admin console |
| Connector env: `TWINGATE_NETWORK` | Your network name |

## Gotchas
- **Do not** set Ollama to listen on `0.0.0.0` — Twingate handles routing; public exposure defeats the security model
- Twingate client must be running and connected on local machine before making LLM requests
- Each access token/script generated in admin console is unique — don't reuse between Connectors

## Related Docs
- [Twingate Connector Setup](https://www.twingate.com/docs/connectors)
- [Continue Extension](https://continue.dev)
- [Ollama](https://ollama.ai)