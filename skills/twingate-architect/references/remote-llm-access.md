# Remote LLM Access with Twingate

## Summary
Twingate enables secure, private access to self-hosted LLM servers (e.g., Ollama) without exposing ports to the public internet. Traffic is tunneled through Twingate's network between a local dev machine and the remote LLM server. Demonstrated using the Continue extension in VS Code.

## Key Information
- Ollama listens on port `11434` on `localhost` by default — do **not** bind to `0.0.0.0`
- Twingate Connector runs on the LLM server, making only **outbound** connections (no inbound firewall ports required)
- Works with any cloud/on-prem Linux server (DigitalOcean, AWS, GCP, Azure, bare metal)
- Continue extension supports VS Code, JetBrains, and Cursor

## Prerequisites
- Twingate account (free tier available)
- Remote Linux server with GPU (e.g., DigitalOcean GPU droplet)
- Ollama installed on remote server
- VS Code with Continue extension installed locally

## Step-by-Step

1. **Remote server**: Install Ollama (`curl https://ollama.ai/install.sh | sh`), pull model (`ollama run llama3`)
2. **Twingate Admin**: Create network → Add Remote Network → Deploy Connector on LLM server
3. **Twingate Admin**: Define Resource with internal IP, port `11434`, protocol TCP → Assign to user
4. **Local machine**: Install Twingate client, sign in
5. **Continue config**: Set `apiBase` to `http://{internal_ip}:11434` in `config.json`

## Configuration Values

**Connector install command:**
```bash
curl "https://binaries.twingate.com/connector/setup.sh" | sudo \
  TWINGATE_ACCESS_TOKEN="{token}" \
  TWINGATE_REFRESH_TOKEN="{refresh_token}" \
  TWINGATE_NETWORK="{network_name}" \
  TWINGATE_LABEL_DEPLOYED_BY="linux" bash
```

**Continue `config.json`:**
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

**Twingate Resource settings:**
- Address: internal IP of LLM server
- Port: `11434`
- Protocol: TCP

## Gotchas
- Never expose Ollama on `0.0.0.0` — keep it bound to localhost/internal IP only
- Twingate client must be **actively connected** on local machine before making LLM requests
- `apiBase` uses the machine's **internal** IP, not a public address
- Continue config file opened via Command Palette → "Continue: Edit Config"

## Related Docs
- [Twingate Connector setup](https://www.twingate.com/docs/connectors)
- [Ollama documentation](https://ollama.ai)
- [Continue extension](https://continue.dev)