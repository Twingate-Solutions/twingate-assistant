# Remote LLM Access with Twingate

## Summary
Secure private access to self-hosted LLM servers using Twingate as a zero-trust network layer, eliminating the need to expose LLM endpoints publicly. The guide uses Ollama on a remote server with the Continue VS Code extension as the client. Traffic routes through a Twingate Connector installed on the LLM server without opening inbound firewall ports.

## Key Information
- Twingate Connector runs on the LLM server, initiates outbound-only connection — no inbound firewall rules needed
- LLM server (Ollama) binds to `localhost` only, never `0.0.0.0`
- Ollama default port: `11434`
- Works with any cloud VM (DigitalOcean, AWS, GCP, Azure) or on-premises server
- Compatible with VS Code Continue extension, JetBrains, and Cursor

## Prerequisites
- Twingate account (free tier available)
- Remote Linux server with GPU (e.g., DigitalOcean GPU droplet)
- VS Code with [Continue extension](https://continue.dev) installed
- Ollama installed on remote server

## Step-by-Step

### 1. Remote Server — Install Ollama
```bash
curl https://ollama.ai/install.sh | sh
ollama run llama3   # downloads model and starts service on localhost:11434
```

### 2. Twingate — Configure Network
1. Create a Remote Network in Twingate admin console (name: e.g., `llm-dev-network`)
2. Add a Connector — run the generated script on the LLM server:
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="{token}" \
  TWINGATE_REFRESH_TOKEN="{refresh_token}" \
  TWINGATE_NETWORK="{network_name}" \
  TWINGATE_LABEL_DEPLOYED_BY="linux" bash
```
3. Define a Resource:
   - **Address**: internal IP of LLM server
   - **Port**: `11434`
   - **Protocol**: TCP
4. Assign user access to the Resource

### 3. Local Machine — Configure Client
1. Install Twingate client, sign in via identity provider
2. Edit Continue `config.json` (Command Palette → "Continue: Edit Config"):
```json
{
  "models": [
    {
      "title": "My Secure Llama3",
      "provider": "ollama",
      "model": "llama3",
      "apiBase": "http://{internal_ip}:11434"
    }
  ]
}
```

## Configuration Values

| Parameter | Value |
|-----------|-------|
| `apiBase` | `http://{internal_ip}:11434` |
| `provider` | `ollama` |
| `model` | `llama3` (or any pulled model) |
| Ollama default port | `11434` |
| Connector env: `TWINGATE_ACCESS_TOKEN` | From admin console |
| Connector env: `TWINGATE_REFRESH_TOKEN` | From admin console |
| Connector env: `TWINGATE_NETWORK` | Your network name |

## Gotchas
- **Do not** set Ollama to listen on `0.0.0.0` — keep it bound to `localhost`; Twingate handles external routing
- Twingate client must be running and connected on local machine before making LLM requests
- The `apiBase` uses the server's **internal IP**, not a public IP or hostname
- Each developer needing access must be individually granted the Resource in Twingate admin

## Related Docs
- [Twingate Connector Setup](https://www.twingate.com/docs/connectors)
- [Ollama Documentation](https://ollama.ai)
- [Continue Extension](https://continue.dev/docs)