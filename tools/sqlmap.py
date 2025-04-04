import subprocess
from typing import List, Optional


def run_sqlmap(
    url: str,
    options: Optional[List[str]] = None,
) -> str:
    """Run sqlmap to test for SQL injection vulnerabilities.
    
    Args:
        url: Target URL to scan
        options: Additional sqlmap options (e.g., ["--dbs", "--batch"])
    
    Returns:
        str: sqlmap output
    """
    print(f"[debug] run_sqlmap({url}, options={options})")
    
    if not subprocess.run(["which", "sqlmap"], capture_output=True).returncode == 0:
        return "Error: sqlmap is not installed. See https://sqlmap.org/"
    
    cmd = ["sqlmap", "-u", url]
    if options:
        cmd.extend(options)
    
    print(cmd)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing sqlmap: {str(e)}"