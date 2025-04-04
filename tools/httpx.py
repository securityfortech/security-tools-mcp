import subprocess
from typing import List, Optional


def run_httpx(
    targets: List[str],
    options: Optional[List[str]] = None,
) -> str:
    """Run httpx to probe HTTP servers.
    
    Args:
        targets: List of target URLs or IPs
        options: Additional httpx options (e.g., ["-status-code", "-title"])
    
    Returns:
        str: httpx output
    """
    print(f"[debug] run_httpx({targets}, options={options})")
    
    if not subprocess.run(["which", "httpx"], capture_output=True).returncode == 0:
        return "Error: httpx is not installed. See https://github.com/projectdiscovery/httpx"
    
    cmd = ["httpx", "-l", "-"]  # Use stdin for list input
    if options:
        cmd.extend(options)
    
    print(cmd)
    try:
        result = subprocess.run(cmd, input="\n".join(targets), capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing httpx: {str(e)}"