"""Security tools package for secops-mcp."""

from typing import Dict, Callable, Any

# Import all tool functions
from .nuclei import run_nuclei, nuclei
from .ffuf import run_ffuf, ffuf
from .nmap import run_nmap, nmap
from .wfuzz import run_wfuzz, wfuzz
from .sqlmap import run_sqlmap, sqlmap
from .hashcat import run_hashcat, hashcat
from .httpx import run_httpx, httpx
from .subfinder import run_subfinder, subfinder
from .tlsx import run_tlsx, tlsx
from .xsstrike import run_xsstrike, xsstrike
from .ipinfo import run_ipinfo, ipinfo

# Tool registry dictionary with function name as key and function as value
TOOL_REGISTRY: Dict[str, Callable] = {
    "nuclei_scan_wrapper": run_nuclei,
    "ffuf_wrapper": run_ffuf,
    "nmap_wrapper": run_nmap,
    "wfuzz_wrapper": run_wfuzz,
    "sqlmap_wrapper": run_sqlmap,
    "hashcat_wrapper": run_hashcat,
    "httpx_wrapper": run_httpx,
    "subfinder_wrapper": run_subfinder,
    "tlsx_wrapper": run_tlsx,
    "xsstrike_wrapper": run_xsstrike,
    "ipinfo_wrapper": run_ipinfo
}

# Define the function to register all tools with an MCP server
def register_all_tools(mcp_server):
    """Register all tools with the MCP server.
    
    Args:
        mcp_server: An instance of FastMCP
    """
    for tool_name, tool_function in TOOL_REGISTRY.items():
        mcp_server.tool(name=tool_name)(tool_function) 