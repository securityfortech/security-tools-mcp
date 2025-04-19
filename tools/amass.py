import subprocess
import json
from typing import Optional, Dict, Any

def amass_wrapper(domain: str, passive: bool = True) -> Dict[str, Any]:
    """
    Wrapper for Amass subdomain enumeration tool.
    
    Args:
        domain (str): Target domain to enumerate
        passive (bool): Whether to perform passive enumeration only
    
    Returns:
        Dict[str, Any]: Results containing discovered subdomains and related information
    """
    try:
        # Build the command
        cmd = ["amass", "enum"]
        if passive:
            cmd.append("-passive")
        cmd.extend(["-d", domain, "-json", "-"])
        
        # Run the command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the output
        subdomains = []
        for line in result.stdout.splitlines():
            if line.strip():
                try:
                    data = json.loads(line)
                    subdomains.append({
                        "name": data.get("name"),
                        "domain": data.get("domain"),
                        "addresses": data.get("addresses", []),
                        "sources": data.get("sources", [])
                    })
                except json.JSONDecodeError:
                    continue
        
        return {
            "success": True,
            "subdomains": subdomains,
            "count": len(subdomains)
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