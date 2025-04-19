import subprocess
import json
from typing import List, Optional, Dict, Any


def run_httpx(
    targets: List[str],
    options: Optional[List[str]] = None,
) -> str:
    """Run httpx to probe HTTP servers.
    
    Args:
        targets: List of target URLs or IPs
        options: Additional httpx options (e.g., ["-status-code", "-title"])
    
    Returns:
        str: JSON string containing probe results
    """
    try:
        # Build the command
        cmd = ["httpx", "-json", "-l", "-"]  # Use stdin for list input
        if options:
            cmd.extend(options)
        
        # Run the command
        result = subprocess.run(
            cmd,
            input="\n".join(targets),
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the output
        try:
            data = json.loads(result.stdout)
            return json.dumps({
                "success": True,
                "targets": targets,
                "results": data
            })
        except json.JSONDecodeError:
            return json.dumps({
                "success": False,
                "error": "Failed to parse JSON output",
                "raw_output": result.stdout
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