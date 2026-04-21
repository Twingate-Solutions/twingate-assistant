## Remote LLM Access with Twingate (Ollama + Continue.dev)

Step-by-step guide to securing a private Ollama LLM server behind Twingate and connecting to it from VS Code via the Continue.dev extension. The Connector runs on the LLM server; the Resource uses the server's internal IP and port 11434; Continue's `apiBase` points to that internal IP through the Twingate tunnel.

**Key Information**
- Ollama default port: 11434
- Do NOT configure Ollama to listen on `0.0.0.0` or expose it publicly -- Connector handles secure access using the internal IP
- Connector deployed on the same host as the Ollama server (or same LAN)
- Resource: internal IP of LLM server, port 11434, TCP
- Continue.dev config: `apiBase: "http://{internal_ip}:11434"` in `config.json`
- Works with any cloud (DigitalOcean GPU droplets, AWS, GCP, Azure) or on-prem GPU server
- Pattern extends beyond VS Code: JetBrains, Cursor also support Continue

**Prerequisites**
- Linux server with GPU running Ollama (or other inference engine)
- Twingate account with Connector deployed on the server
- Continue.dev extension installed in VS Code

**Step-by-Step**
1. Install Ollama on the GPU server: `curl https://ollama.ai/install.sh | sh`
2. Pull a model: `ollama run llama3` (or any model)
3. Deploy Twingate Connector on the LLM server (follow Admin Console instructions)
4. Create Twingate Resource: internal IP of server, port 11434, TCP; assign to your user
5. Install Twingate Client locally; sign in and connect
6. In Continue's `config.json`, add model entry with `"apiBase": "http://{internal_ip}:11434"`
7. Select the model in Continue and start using it

**Configuration Values**
- Ollama listen address: keep as `localhost` or internal IP only (not 0.0.0.0)
- Continue config: `provider: "ollama"`, `model: "llama3"`, `apiBase: "http://{internal_ip}:11434"`

**Gotchas**
- If Ollama is bound to localhost only, the Resource address must be the server's internal IP (not localhost) -- the Connector routes traffic from the Client to Ollama via the server's local interface
- Exposing Ollama on 0.0.0.0 is a security risk even with Twingate -- bind to internal IP and let the Connector handle routing

**Related Docs**
- /docs/llms
- /docs/remote-mcp-access
- /docs/resources
- /docs/service-accounts-guide
