import asyncio
import os
import shutil
import subprocess
import time
from typing import Any

from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse
from agents.model_settings import ModelSettings


async def main():
    # Create the MCP server instance
    mcp_server = MCPServerSse(
        name="SSE Python Server",
        params={
            "url": "http://localhost:9001/sse",
        }
    )
    
    try:
        # Explicitly connect and await the connection
        await mcp_server.connect()
        print("MCP server successfully connected")
        
        # Create agent after server is connected
        agent = Agent(
            name="Assistant",
            instructions="You are a helpful cybersecurity expert.",
            mcp_servers=[mcp_server],
            model_settings=ModelSettings(tool_choice="required"),
        )

        message = "can you run nmap sV scan on localhost ?"
        print(f"Running: {message}")
        
        result = await Runner.run(starting_agent=agent, input=message)
        print(result.final_output)
    
    finally:
        # Make sure to disconnect the server when done
        await mcp_server.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
    