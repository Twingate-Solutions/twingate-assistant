---
source: https://github.com/Twingate-Labs/saml_service_provider
type: github
fetched: 2026-08-06
source_version: 1489b6a33fcdd7d9242837db383c1c426e84e9a0
---

<!-- triage: unassigned -->

# Twingate-Labs/saml_service_provider

## Summary
A minimal Django-based SAML Service Provider (SP) demo using pysaml2. It demonstrates SAML SSO integration with JumpCloud as the Identity Provider (IdP). Intended as a reference implementation for SP-initiated SAML authentication flows.

## Key Information
- Language: Python 3.10.1
- Framework: Django with pysaml2
- Dependency manager: Poetry
- IdP tested against: JumpCloud (custom SAML app)
- SAML binding: Redirect/POST; ACS endpoint at `/saml2/acs/`

## Prerequisites
- Python 3.10.1 (via pyenv)
- Poetry
- `libxmlsec1` OS package (`brew install libxmlsec1`)
- JumpCloud administrator account

## Usage / Step-by-Step

1. **Install system dependencies**
   ```sh
   brew install pyenv poetry libxmlsec1
   pyenv install 3.10.1
   ```

2. **Clone and configure Python version**
   ```sh
   git clone git@github.com:inbalzelinger/saml_service_provider.git
   cd saml_service_provider
   pyenv local 3.10.1
   ```

3. **Set up virtual environment and install deps**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   poetry install
   ```

4. **Configure JumpCloud SSO app** (custom SAML app) — see Configuration Values below.

5. **Paste IdP certificate into `saml.py`**
   - Download `.pem` from JumpCloud
   - Convert to string format via [samltool.com](https://www.samltool.com/format_x509cert.php)
   - Set `x509_cert="<value>"` in `saml.py`

6. **Run and test**
   ```sh
   python3 manage.py runserver
   # Visit http://localhost:8000/saml2/login
   ```

## Configuration Values

| Parameter | Value |
|---|---|
| SP Entity ID | `http://localhost:8000/sample_sp` |
| IdP Entity ID | `jumpcloud/twingate/sample-sp` |
| ACS URL | `http://127.0.0.1:8000/saml2/acs/` |
| Login URL | `http://127.0.0.1:8000/saml2/login` |
| IdP SSO URL | `https://sso.jumpcloud.com/saml2/saml2` |
| NameID format | `urn:oasis:names:tc:SAML:1.0:nameid-format:unspecified` |
| NameID attribute | `email` |
| Signature algorithm | `RSA-SHA256` |
| Sign assertion | disabled |
| x509_cert (in `saml.py`) | Paste converted cert string from JumpCloud |

## Gotchas
- The certificate from JumpCloud must be reformatted to a single-line string before pasting into `saml.py`; the raw `.pem` will not work directly.
- ACS URL uses `127.0.0.1` while the SP Entity ID and login URL use `localhost` — keep these consistent with whatever JumpCloud has registered or assertions will fail.
- `libxmlsec1` must be installed at the OS level before `poetry install`; pysaml2 will fail to install without it.
- No `.env` or secrets management is shown; the IdP certificate is hardcoded in `saml.py`.

## Related Docs
- [pysaml2 installation docs](https://pysaml2.readthedocs.io/en/latest/install.html)
- [JumpCloud custom SAML app setup](https://support.jumpcloud.com/support/s/article/custom-saml-applications)
- [OneLogin SAML X.509 formatter](https://www.samltool.com/format_x509cert.php)