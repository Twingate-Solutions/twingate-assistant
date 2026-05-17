# Remote LLM Access with Twingate

## Summary
Twingate enables secure, private access to self-hosted LLM servers (e.g., Ollama) without exposing ports to the public internet. Traffic routes through a Twingate Connector installed on the LLM server, creating an encrypted tunnel accessible only to authorized users. Demonstrated with the Continue VS Code extension.

## Key Information
- Ollama default port: `11434`, bound to `localhost` only
- Twingate Connector installs on the remote LLM server and makes outbound-only connections (no inbound firewall rules needed)
- Works with any cloud VM (DigitalOcean, AWS, GCP, Azure) or on-prem server
- Continue extension supported in VS Code, JetBrains, and Cursor

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

2. **Deploy Twingate Connector on remote server**
   ```bash
   curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
     TWINGATE_ACCESS_TOKEN="{token}" \
     TWINGATE_REFRESH_TOKEN="{refresh_token}" \
     TWINGATE_NETWORK="{network_name}" \
     TWINGATE_LABEL_DEPLOYED_BY="linux" bash
   ```

3. **Define Twingate Resource** in admin console:
   - Address: internal IP of LLM server
   - Port: `11434`
   - Protocol: TCP

4. **Assign user access** to the Resource in Twingate admin console

5. **Configure Continue extension** (`config.json`):
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
| `provider` | `ollama` |
| `model` | `llama3` (or any pulled model) |
| Ollama default port | `11434` |

## Gotchas
- **Do NOT** configure Ollama to listen on `0.0.0.0` — bind to localhost only; Twingate handles external access
- Ollama must use the server's **internal IP** in the Twingate Resource definition, not `localhost` or `127.0.0.1`
- Twingate client must be running and connected on local machine before making LLM requests
- Each developer needing access must be individually granted access to the Resource

## Related Docs
- [Twingate Connector Setup](https://www.twingate.com/docs/connector)
- [Ollama Documentation](https://ollama.ai)
- [Continue Extension Configuration](https://continue.dev/docs)