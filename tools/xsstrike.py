import subprocess
from typing import List, Optional


def run_xsstrike(
    url: str,
    options: Optional[List[str]] = None,
) -> str:
    """Run XSStrike to detect XSS vulnerabilities.
    
    Args:
        url: Target URL to scan
        options: Additional XSStrike options (e.g., ["--crawl", "--blind"])
    
    Returns:
        str: XSStrike output
    """
    print(f"[debug] run_xsstrike({url}, options={options})")
    
    if not subprocess.run(["which", "xsstrike"], capture_output=True).returncode == 0:
        return "Error: XSStrike is not installed. See https://github.com/s0md3v/XSStrike"
    
    cmd = ["xsstrike", "-u", url]
    if options:
        cmd.extend(options)
    
    print(cmd)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing XSStrike: {str(e)}"