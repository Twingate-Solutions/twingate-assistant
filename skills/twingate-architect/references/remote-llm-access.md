# Remote LLM Access with Twingate

## Summary
Twingate enables secure, private access to self-hosted LLM servers (e.g., Ollama) without exposing ports to the public internet. Traffic is routed through a Twingate Connector installed on the LLM server, making the server invisible externally while accessible to authorized clients. Designed for use with the Continue VS Code extension.

## Key Information
- Ollama default port: `11434`, bound to `localhost` only
- Twingate Connector runs on the LLM server, making inbound firewall rules unnecessary
- Works with any cloud VM (DigitalOcean, AWS, GCP, Azure) or on-premises server
- Compatible with VS Code, JetBrains, and Cursor via Continue extension

## Prerequisites
- Twingate account (free tier available)
- Remote Linux server with GPU (e.g., DigitalOcean GPU droplet)
- Ollama installed on remote server
- Continue extension installed in VS Code
- Twingate client installed on local machine

## Step-by-Step

1. **Install Ollama on remote server**
   ```bash
   curl https://ollama.ai/install.sh | sh
   ollama run llama3
   ```

2. **Create Twingate Remote Network** in admin console (name: e.g., `llm-dev-network`)

3. **Deploy Connector on remote server**
   ```bash
   curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
     TWINGATE_ACCESS_TOKEN="{token}" \
     TWINGATE_REFRESH_TOKEN="{refresh_token}" \
     TWINGATE_NETWORK="{network_name}" \
     TWINGATE_LABEL_DEPLOYED_BY="linux" bash
   ```

4. **Define Resource in Twingate admin**
   - Address: internal IP of LLM server
   - Port: `11434`
   - Protocol: TCP

5. **Assign user access** to the Resource

6. **Install and connect Twingate client** on local machine

7. **Configure Continue `config.json`**
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
   Access via: `Cmd+Shift+P` → "Continue: Edit Config"

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `apiBase` | `http://{internal_ip}:11434` |
| `provider` | `ollama` |
| `model` | `llama3` (or any pulled model) |
| Ollama default port | `11434` |

## Gotchas
- **Do not** bind Ollama to `0.0.0.0` — keep it on `localhost`/internal IP only
- Twingate client must be running and connected on local machine before making LLM requests
- Resource address must use the server's **internal** IP, not public IP
- Connector must show as "connected" in admin console before testing

## Related Docs
- [Twingate Connector Setup](https://www.twingate.com/docs/connectors)
- [Ollama](https://ollama.ai)
- [Continue Extension](https://continue.dev)