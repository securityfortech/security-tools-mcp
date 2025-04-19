# tools/nuclei.py
import subprocess
import json
from typing import List, Optional, Dict, Any


def run_nuclei(
    target: str,
    templates: Optional[List[str]] = None,
    severity: Optional[str] = None,
    output_format: str = "json",
) -> str:
    """Run a Nuclei security scan on the specified target.
    
    Args:
        target: The target URL or IP to scan
        templates: List of specific template names to use (optional)
        severity: Filter by severity level (critical, high, medium, low, info)
        output_format: Output format (json, text)
    
    Returns:
        str: JSON string containing scan results
    """
    try:
        # Build the command
        cmd = ["nuclei", "-u", target, "-json"]
        
        # Add template filters if specified
        if templates:
            cmd.extend(["-t", ",".join(templates)])
        
        # Add severity filter if specified
        if severity:
            cmd.extend(["-s", severity])
        
        # Run the scan
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
                "target": target,
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