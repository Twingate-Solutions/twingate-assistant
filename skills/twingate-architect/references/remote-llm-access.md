# Remote LLM Access with Twingate

## Summary
Twingate enables secure, private access to self-hosted LLM servers (e.g., Ollama) without exposing ports to the public internet. Traffic between local dev machines and remote LLM servers is routed through Twingate's zero-trust network, eliminating the need for VPNs or public firewall rules. Guide uses VS Code Continue extension as the client example.

## Key Information
- Twingate Connector installs on the LLM server and makes outbound-only connections (no inbound ports needed)
- Ollama default port: `11434`, binds to `localhost` only — do **not** bind to `0.0.0.0`
- Traffic flow: Continue → Twingate client → Twingate network → Connector → Ollama
- Works with any cloud VM (DigitalOcean, AWS, GCP, Azure) or on-premises server
- Applies beyond VS Code: JetBrains, Cursor also supported

## Prerequisites
- Twingate account (free tier available)
- Remote Linux server with GPU (e.g., DigitalOcean GPU droplet)
- Ollama installed on remote server
- VS Code with Continue extension installed locally
- Twingate client installed on local machine

## Step-by-Step

1. **Install Ollama on remote server**
   ```bash
   curl https://ollama.ai/install.sh | sh
   ollama run llama3
   ```

2. **Create Twingate Remote Network** — name it (e.g., `llm-dev-network`), select On-Premise or cloud

3. **Deploy Connector on remote server**
   ```bash
   curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
     TWINGATE_ACCESS_TOKEN="{token}" \
     TWINGATE_REFRESH_TOKEN="{token}" \
     TWINGATE_NETWORK="{network_name}" \
     TWINGATE_LABEL_DEPLOYED_BY="linux" bash
   ```

4. **Define Resource** in Twingate admin console:
   - Address: internal IP of LLM server
   - Port: `11434`
   - Protocol: TCP

5. **Assign user access** to the Resource

6. **Install Twingate client** on local machine, sign in

7. **Configure Continue** (`config.json`):
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
| `apiBase` | `http://{internal_ip}:11434` |
| Ollama port | `11434` |
| Resource protocol | TCP |
| Connector env: `TWINGATE_ACCESS_TOKEN` | From admin console |
| Connector env: `TWINGATE_REFRESH_TOKEN` | From admin console |
| Connector env: `TWINGATE_NETWORK` | Your network name |

## Gotchas
- **Never bind Ollama to `0.0.0.0`** — keep it on localhost/internal IP only
- Twingate client must be running and connected on local machine before requests work
- Use the server's **internal IP** (not public IP) as the Resource address and in `apiBase`
- Each user needing access must be explicitly granted access to the Resource in admin console

## Related Docs
- [Twingate Connector Setup](https://www.twingate.com/docs/connector)
- [Continue Extension Docs](https://continue.dev/docs)
- [Ollama Documentation](https://ollama.ai)