# Codebase of the Bachelor Thesis

Currently the codebase is organized in the following manner:

## Main base

- `agents`: Contains the multi-agent experiments
- `ragmcp`: main logic of the MCP server

## Analysis & Experiments

- `mcp_analysis`: Where the experiments for the MCP functions are done. Contains more functions than in `congressMCP`
- `helper`: Experiments that give us helpful information for all the subdirectories

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