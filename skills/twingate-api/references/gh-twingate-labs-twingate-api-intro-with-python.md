---
source: https://github.com/Twingate-Labs/Twingate-API-Intro-with-Python
type: github
fetched: 2026-08-06
source_version: d525d2e6c5faabcde47c48729c06f128ffccef0f
---

<!-- triage: unassigned -->

# Twingate API Intro with Python

## Summary
A Jupyter Notebook tutorial for learning the Twingate GraphQL API using Python. Covers querying and mutating Twingate resources step-by-step, requiring no prior GraphQL or API knowledge. Assumes basic familiarity with Twingate concepts (Groups, Users, Resources).

## Key Information
- Language: Python (Jupyter Notebook)
- API type: GraphQL
- Beginner-friendly; no GraphQL experience required
- Topics: simple queries, variabilized queries, introspection, simple mutations, variabilized mutations, mutation introspection

## Prerequisites
- Jupyter Notebook installed locally
- Basic Python familiarity
- Active Twingate account with working knowledge of core concepts (Groups, Users, Resources)
- Twingate API key (implied for authenticated API calls)

## Usage / Step-by-Step
1. Install Jupyter Notebook on your machine
2. Clone the repository:
   ```bash
   git clone https://github.com/Twingate-Labs/Twingate-API-Intro-with-Python.git
   ```
3. Open the notebook:
   ```bash
   cd Twingate-API-Intro-with-Python
   jupyter notebook
   ```
4. Follow the notebook cells sequentially

## Configuration Values
| Value | Description |
|---|---|
| Twingate API Key | Required to authenticate GraphQL requests; set within the notebook |
| Twingate Network/Tenant URL | Your account's API endpoint (e.g., `https://<tenant>.twingate.com/api/graphql/`) |

*(Exact variable names are defined inside the notebook cells.)*

## Gotchas
- Notebook must be run in order; later cells depend on variables set in earlier ones
- Twingate API key must have sufficient permissions to perform mutations (creating/modifying resources)
- GraphQL introspection must be enabled on your Twingate tenant for the introspection sections to work

## Related Docs
- [Twingate GraphQL API Documentation](https://docs.twingate.com/docs/graphql-overview)
- [Jupyter Notebook Installation](https://jupyter.org/install)