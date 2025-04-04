import random
import subprocess
import json
from typing import List, Optional

import requests
from mcp.server.fastmcp import FastMCP

from tools.nuclei import run_nuclei
from tools.ffuf import run_ffuf
from tools.wfuzz import run_wfuzz
from tools.sqlmap import run_sqlmap
from tools.nmap import run_nmap
from tools.hashcat import run_hashcat
from tools.httpx import run_httpx
from tools.subfinder import run_subfinder
from tools.tlsx import run_tlsx
from tools.xsstrike import run_xsstrike
from tools.ipinfo import run_ipinfo

# Create server
mcp = FastMCP(name="security-tools-mcp",
    version="1.0.0"
)


@mcp.tool()
def nuclei_scan_wrapper(
    target: str,
    templates: Optional[List[str]] = None,
    severity: Optional[str] = None,
    output_format: str = "json",
) -> str:
    """Wrapper for running a Nuclei security scan."""
    return run_nuclei(target, templates, severity, output_format)


@mcp.tool()
def ffuf_wrapper(
    url: str,
    wordlist: str,
    filter_code: Optional[str] = "404",
) -> str:
    """Wrapper for running ffuf fuzzing."""
    return run_ffuf(url, wordlist, filter_code)


@mcp.tool()
def wfuzz_wrapper(
    url: str,
    wordlist: str,
    filter_code: Optional[str] = "404",
) -> str:
    """Wrapper for running wfuzz fuzzing."""
    return run_wfuzz(url, wordlist, filter_code)


@mcp.tool()
def sqlmap_wrapper(
    url: str,
    risk: Optional[int] = 1,
    level: Optional[int] = 1,
) -> str:
    """Wrapper for running SQLMap scan."""
    return run_sqlmap(url, risk, level)


@mcp.tool()
def nmap_wrapper(
    target: str,
    ports: Optional[str] = None,
    scan_type: Optional[str] = "sV",
) -> str:
    """Wrapper for running Nmap scan."""
    return run_nmap(target, ports, scan_type)


@mcp.tool()
def hashcat_wrapper(
    hash_file: str,
    wordlist: str,
    hash_type: str,
) -> str:
    """Wrapper for running Hashcat password cracking."""
    return run_hashcat(hash_file, wordlist, hash_type)


@mcp.tool()
def httpx_wrapper(
    urls: List[str],
    status_codes: Optional[List[int]] = None,
) -> str:
    """Wrapper for running HTTPX scan."""
    return run_httpx(urls, status_codes)


@mcp.tool()
def subfinder_wrapper(
    domain: str,
    recursive: bool = False,
) -> str:
    """Wrapper for running Subfinder subdomain enumeration."""
    return run_subfinder(domain, recursive)


@mcp.tool()
def tlsx_wrapper(
    host: str,
    port: Optional[int] = 443,
) -> str:
    """Wrapper for running TLSX scan."""
    return run_tlsx(host, port)


@mcp.tool()
def xsstrike_wrapper(
    url: str,
    crawl: bool = False,
) -> str:
    """Wrapper for running XSStrike scan."""
    return run_xsstrike(url, crawl)


@mcp.tool()
def ipinfo_wrapper(
    ip: Optional[str] = None,
) -> str:
    """Wrapper for getting IP information using ipinfo.io."""
    return run_ipinfo(ip)


if __name__ == "__main__":
    mcp.run(transport="stdio")