# Remote LLM Access with Twingate

## Summary
Twingate secures connections between local development machines and remote/self-hosted LLM servers without exposing ports to the public internet. Uses a Connector on the LLM server to create an outbound-only encrypted tunnel. Guide uses Ollama + Continue VS Code extension as the reference implementation.

## Key Information
- Twingate Connector runs on the LLM server and makes **outbound-only** connections — no inbound firewall ports required
- LLM server (Ollama) stays bound to `localhost`/internal IP only — never exposed to public internet
- Traffic is end-to-end encrypted; LLM server is invisible to public internet
- Works with any VS Code-compatible Continue setup, JetBrains, and Cursor

## Prerequisites
- Twingate account (free tier available)
- Remote Linux server (cloud VM or on-prem) with GPU for LLM workloads
- Ollama installed on remote server
- Continue extension installed in VS Code
- Twingate client installed on local machine

## Step-by-Step

1. **Install Ollama on remote server** — bind to localhost only (port `11434`)
2. **Pull LLM model**: `ollama run llama3`
3. **Create Twingate Network** in admin console (name it, e.g., `llm-dev-network`)
4. **Deploy Connector** on remote LLM server via generated script
5. **Define Resource** in Twingate admin pointing to internal IP:11434
6. **Grant user access** to the Resource
7. **Install Twingate client** on local machine and sign in
8. **Configure Continue** `config.json` with internal IP as `apiBase`

## Configuration Values

**Connector install command (example):**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="{token}" \
  TWINGATE_REFRESH_TOKEN="{refresh_token}" \
  TWINGATE_NETWORK="{network_name}" \
  TWINGATE_LABEL_DEPLOYED_BY="linux" bash
```

**Continue `config.json` model entry:**
```json
{
  "title": "My Secure Llama3",
  "provider": "ollama",
  "model": "llama3",
  "apiBase": "http://{internal_ip}:11434"
}
```

**Twingate Resource settings:**
| Field | Value |
|-------|-------|
| Address | Internal IP of LLM server |
| Port | `11434` |
| Protocol | TCP |

## Gotchas
- **Do NOT** configure Ollama to listen on `0.0.0.0` — keep it on localhost/internal IP only
- Twingate client must be running and connected on local machine before making LLM requests
- Each user needing LLM access must be explicitly granted access to the Resource in Twingate admin
- Connector install script is unique per deployment — generate fresh from admin console

## Related Docs
- [Twingate Connectors](https://www.twingate.com/docs/connectors)
- [Ollama documentation](https://ollama.ai)
- [Continue extension](https://continue.dev)
- Twingate Resources configuration