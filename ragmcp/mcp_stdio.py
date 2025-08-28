#!/usr/bin/env python3
"""
Standalone MCP stdio server for agent communication
This runs a proper MCP server over stdio that agents can connect to
"""

import asyncio
import sys
import os
from pathlib import Path

# Add the parent directory to Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from mcp.server.stdio import stdio_server
from mcp.server import Server
from mcp.types import Tool, TextContent
import importlib.util

# Import the main server wrapper
from main import MCPServerWrapper

def get_tool_description(tool_name: str) -> str:
    """Get a basic description for a tool"""
    descriptions = {
        "getBillSummary": "Get bill summary for given congress, bill type, and bill number",
        "getBillSponsors": "Get bill sponsors information",
        "getBillCosponsors": "Get bill cosponsors information", 
        "getBillCommittees": "Get committees associated with a bill",
        "get_committee_members": "Get members of a specific committee",
        "get_committee_actions": "Get actions taken by committees on a bill",
        "getCongressMember": "Get information about a congress member by bioguide ID",
        "extractBillActions": "Get timeline of actions taken on a bill",
        "getBillAmendments": "Get amendments to a bill",
        "getAmendmentSponsors": "Get sponsors of an amendment",
        "getRelevantBillSections": "Get bill sections relevant to a company using RAG"
    }
    return descriptions.get(tool_name, f"Tool: {tool_name}")

async def main():
    # Create standard MCP server for stdio communication
    server = Server("rag-congress-mcp")
    
    # Create wrapper instance to access methods
    wrapper = MCPServerWrapper()
    
    # Register tool call handler
    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        try:
            # Get the method from wrapper instance
            if hasattr(wrapper, name):
                method = getattr(wrapper, name)
                # Call the method with proper arguments
                if name in ['getBillSummary', 'getBillSponsors', 'getBillCosponsors', 'getBillCommittees', 
                           'extractBillActions', 'getBillAmendments', 'get_committee_actions']:
                    result = method(arguments)
                elif name == 'get_committee_members':
                    result = method(arguments.get('committee_name'), arguments.get('congress'))
                elif name == 'getCongressMember':
                    result = method(arguments.get('bioguideId'))
                elif name == 'getRelevantBillSections':
                    result = method(arguments.get('congress_index'), arguments.get('company_name'))
                else:
                    result = method(arguments)
                
                return [TextContent(type="text", text=str(result))]
            else:
                return [TextContent(type="text", text=f"Error: Tool '{name}' not found")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error calling {name}: {str(e)}")]
    
    # Register tool listing handler
    @server.list_tools()
    async def list_tools() -> list[Tool]:
        tools = []
        # Get all MCP tool methods from the wrapper
        tool_methods = [
            'getBillSummary', 'getBillSponsors', 'getBillCosponsors', 'getBillCommittees',
            'get_committee_members', 'get_committee_actions', 'getCongressMember',
            'extractBillActions', 'getBillAmendments', 'getAmendmentSponsors',
            'getRelevantBillSections'
        ]
        
        for tool_name in tool_methods:
            if hasattr(wrapper, tool_name):
                tools.append(Tool(
                    name=tool_name,
                    description=get_tool_description(tool_name),
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                ))
        
        return tools
    
    # Run stdio server
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())