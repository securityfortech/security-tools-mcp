import subprocess
import json
from typing import Optional, List, Dict, Any

def dirsearch_wrapper(url: str, extensions: Optional[List[str]] = None, wordlist: Optional[str] = None) -> Dict[str, Any]:
    """
    Wrapper for Dirsearch directory and file brute forcer.
    
    Args:
        url (str): Target URL to scan
        extensions (List[str], optional): File extensions to check
        wordlist (str, optional): Path to custom wordlist
    
    Returns:
        Dict[str, Any]: Results containing discovered paths and their status codes
    """
    try:
        # Build the command
        cmd = ["dirsearch", "-u", url, "--json-report", "-"]
        
        if extensions:
            cmd.extend(["-e", ",".join(extensions)])
        
        if wordlist:
            cmd.extend(["-w", wordlist])
        
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
            return {
                "success": True,
                "results": data.get("results", []),
                "total": len(data.get("results", []))
            }
        except json.JSONDecodeError:
            return {
                "success": False,
                "error": "Failed to parse JSON output",
                "raw_output": result.stdout
            }
        
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": str(e),
            "stderr": e.stderr
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        } 