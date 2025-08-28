# Codebase of the Bachelor Thesis

Currently the codebase is organized in the following manner:

## Main base

- `ragmcp`: main logic of the MCP server
- `agentServer`: Contains the multi-agent experiments
- `frontend_demo`: Frontend logic

## Docker compose setups

- `prod.yml`: The **complete** docker compose setup for the remote deployment
- `docker-compose.yml`: The **complete and working** docker compose setup for local deployment
- `debug-mcp.yml`: Starting the MCP container only
- `debug-agents.yml`: Starting the MCP server/container and the agents container
- `debug-frontend.yml`: Starting MCP & Agents and frontend container (without actually starting the service)
- `debug-prod-XXX.yml`: Claude Code copies of the debug files above to test remote deployment

## Secrets.ini Structure

- Add a `secrets.ini` file with the following structure:

```
[API_KEYS]
CONGRESS_API_KEY = ...
OPENAI_API_KEY = ...
GOOGLE_API_KEY = ...
GPO_API_KEY = ...
LANGCHAIN_API_KEY = ...
```

The important ones are only LANGCHAIN, GPO, OPENAI and CONGRESS