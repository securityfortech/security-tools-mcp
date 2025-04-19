import subprocess
import json
from typing import Optional, Dict, Any


def run_tlsx(host: str, port: Optional[int] = 443) -> str:
    """
    Run tlsx to analyze TLS configurations.
    
    Args:
        host: Target hostname or IP address
        port: Target port (default: 443)
    
    Returns:
        str: JSON string containing TLS analysis results
    """
    try:
        # Build the command
        cmd = ["tlsx", "-host", host, "-port", str(port), "-json"]
        
        # Run the command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the output
        try:
            data = json.loads(result.stdout)
            return json.dumps({
                "success": True,
                "host": host,
                "port": port,
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