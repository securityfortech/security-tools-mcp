import random
import subprocess
import json
from typing import List, Optional

import requests
from mcp.server.fastmcp import FastMCP

# Import the tool registry function
from tools import register_all_tools

# Create server
mcp = FastMCP(name="secops-mcp",
    version="1.0.0",
    host="0.0.0.0",
    port=9001
)

# Register all tools using the registry
register_all_tools(mcp)

# The individual tool registrations are removed and replaced with the registry

if __name__ == "__main__":
    mcp.run(transport="sse")