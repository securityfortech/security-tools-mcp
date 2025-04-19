import subprocess
import json
from typing import List, Optional, Dict, Any


def run_sqlmap(
    url: str,
    options: Optional[List[str]] = None,
) -> str:
    """Run sqlmap to test for SQL injection vulnerabilities.
    
    Args:
        url: Target URL to scan
        options: Additional sqlmap options (e.g., ["--dbs", "--batch"])
    
    Returns:
        str: JSON string containing scan results
    """
    try:
        # Build the command
        cmd = ["sqlmap", "-u", url, "--batch", "--output-dir=/tmp/sqlmap"]
        if options:
            cmd.extend(options)
        
        # Run the command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the output
        return json.dumps({
            "success": True,
            "url": url,
            "results": {
                "output": result.stdout,
                "options": options or []
            }
        })
        
    except subprocess.CalledProcessError as e:
        return json.dumps({
            "success": False,
            "error": str(e),
            "stderr": e.stderr
        })
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e)
        })