---
source: https://www.twingate.com/docs/remote-llm-access
type: docs
fetched: 2026-08-14
source_version: 0080308e2cd6d97927174aa252b8fb407b061b1b6bb70d0b3159ced6e02166e8
---

# Remote LLM Access with Twingate

## Summary
Securely connect a local development machine to a self-hosted or cloud-hosted LLM (e.g., Ollama) using Twingate as a zero-trust network layer. The LLM server is never exposed to the public internet; Twingate's Connector handles all inbound routing. Example uses the Continue VS Code extension as the LLM client.

## Key Information
- Twingate Connector runs on the LLM server and makes **outbound-only** connections — no inbound firewall ports required
- LLM server (Ollama) listens on `localhost`/internal IP only, never `0.0.0.0`
- Traffic is end-to-end encrypted; LLM server is invisible to the public internet
- Works with any cloud VM (DigitalOcean, AWS, GCP, Azure) or on-premises server
- Continue extension supports VS Code, JetBrains, and Cursor

## Prerequisites
- Twingate account (free tier available)
- Remote Linux server with GPU (DigitalOcean droplet or equivalent)
- [Ollama](https://ollama.ai) installed on the remote server
- VS Code with [Continue](https://continue.dev) extension installed locally
- Twingate client installed on local machine

## Step-by-Step

### 1. Remote Server — Install Ollama
```bash
curl https://ollama.ai/install.sh | sh
ollama run llama3   # downloads model and starts service
```
Ollama defaults to `localhost:11434`. **Do not** bind to `0.0.0.0`.

### 2. Twingate Admin Console — Network Setup
1. Create a Remote Network (name: e.g., `llm-dev-network`; type: On-Premise or cloud)
2. Add a Connector → run the generated install script on the LLM server:
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="{token}" \
  TWINGATE_REFRESH_TOKEN="{refresh_token}" \
  TWINGATE_NETWORK="{network_name}" \
  TWINGATE_LABEL_DEPLOYED_BY="linux" bash
```
3. Add a Resource:
   - **Label**: `Ollama LLM`
   - **Address**: internal IP of the LLM server
   - **Port**: `11434`
   - **Protocol**: TCP
4. Assign the Resource to your Twingate user(s)

### 3. Local Machine — Client + Continue Config
1. Install and sign in to the Twingate client
2. Edit Continue config (`Cmd+Shift+P` → "Continue: Edit Config") — `config.json`:
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
| Ollama default port | `11434` |
| Ollama bind address | `localhost` / internal IP only |
| Continue `provider` | `ollama` |
| Continue `apiBase` | `http://{internal_ip}:11434` |
| Connector env: `TWINGATE_ACCESS_TOKEN` | From Twingate admin console |
| Connector env: `TWINGATE_REFRESH_TOKEN` | From Twingate admin console |
| Connector env: `TWINGATE_NETWORK` | Your Twingate network name |

## Gotchas
- **Never** expose Ollama on `0.0.0.0` — defeats the entire security model
- Twingate client must be running and connected on the local machine before making LLM requests
- Use the server's **internal** IP (not public IP) in both the Twingate Resource definition and `apiBase`
- Connector must show "connected" in admin console before traffic can flow

## Related Docs
- [Twingate Connector Setup](https://www.twingate.