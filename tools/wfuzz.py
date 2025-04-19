import subprocess
import json
from typing import Optional, Dict, Any


def run_wfuzz(
    url: str,
    wordlist: str,
    hide_code: Optional[str] = "404",
) -> str:
    """Run wfuzz to fuzz web application endpoints.
    
    Args:
        url: Target URL with FUZZ keyword (e.g., "http://example.com/FUZZ")
        wordlist: Path to wordlist file
        hide_code: HTTP status code to hide (e.g., "404")
    
    Returns:
        str: JSON string containing fuzzing results
    """
    try:
        # Build the command
        cmd = ["wfuzz", "-w", wordlist, "--hc", hide_code, "-f", "json", url]
        
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
                "url": url,
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