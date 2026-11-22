---
source: https://www.twingate.com/docs/remote-llm-access
type: docs
fetched: 2026-11-22
source_version: a1e516644cd3bb281f2a0cf37708331539732f8b1eec3888e2df0ffd6b30e59e
trust: official
---

# Remote LLM Access with Twingate

## Summary
Guide to securing communication between a local editor (VS Code with the Continue extension) and a remote self-hosted LLM (Ollama) using Twingate. The LLM server is never exposed to the public internet. A Twingate Connector on the server makes outbound-only connections, and the local Twingate Client routes traffic to a private Resource.

## Key Information
- Architecture: local machine (VS Code + Continue + Twingate Client) → Twingate network → Connector on the LLM server → Ollama.
- Benefits: no inbound firewall ports, no traditional VPN, only authenticated and authorized users can reach the LLM, traffic is encrypted.
- Reasons to avoid public exposure: protecting IP in prompts and code, preventing abuse of the endpoint, compliance, and preventing man-in-the-middle tampering.
- The example server is a Digital Ocean GPU droplet, but any Linux VM or physical server works (AWS, GCP, Azure, on-prem).
- The same approach works anywhere Continue is supported, including JetBrains IDEs and Cursor.

## Prerequisites
- A Twingate account (free sign-up available).
- A Linux server with enough GPU/compute for the chosen model.
- Twingate Client installed on the dev machine (Windows, macOS, or Linux).
- The Continue extension installed in the editor.

## Step-by-Step
1. **Set up the LLM server.** Install Ollama using the install script from the Ollama site, then run `ollama run llama3` to download the model and start the service. Ollama listens on `localhost:11434` by default. The page's install command pipes a script from ollama.ai into a shell, so see the Ollama site for the official install instructions.
2. **Set up Twingate.**
   - Create a Remote Network (the page's example name is `llm-dev-network`) and choose On-Premise or the matching cloud option.
   - Deploy a Connector on the LLM server using the script generated in the admin console. The script is unique to your account and includes your tokens and network name.
   - Confirm the Connector shows as connected.
   - Add a Resource and grant access to the users who need it.
3. **Configure the local machine.** Install the Twingate Client and sign in with your identity provider. Then run "Continue: Edit Config" from the command palette (Cmd/Ctrl+Shift+P) to open Continue's `config.json`.
4. **Test.** Confirm the Client is connected, select the model in Continue, and send a prompt.

## Configuration Values
**Twingate Resource**
- Label: e.g., `Ollama LLM`
- Address: internal IP of the LLM machine
- Port: `11434`
- Protocol: TCP

**Connector environment variables** (from the generated script)
- `TWINGATE_ACCESS_TOKEN`
- `TWINGATE_REFRESH_TOKEN`
- `TWINGATE_NETWORK`
- `TWINGATE_LABEL_DEPLOYED_BY`

**Continue `config.json` model entry**
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

## Gotchas
- Do **not** bind Ollama to `0.0.0.0` or expose it publicly. Use the machine's internal IP so only the Connector can reach it.
- The Twingate Client must be running and connected, or Continue cannot reach `apiBase`.
- The Resource address and the `apiBase` host must match.
- Connector tokens are account-specific. Use the script from your own admin console, not the example.
- Connector install commands use `binaries.twingate.com`, which is Twingate's official host.

## Related Docs
- Continue (https://continue.dev/)
- Ollama (https://ollama.ai/)
- Twingate (https://www.twingate.com/)