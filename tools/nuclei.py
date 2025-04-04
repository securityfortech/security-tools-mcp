# tools/nuclei.py
import subprocess
from typing import List, Optional


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
        str: The scan results in the specified format
    """
    print(f"[debug] run_nuclei({target}, templates={templates}, severity={severity})")
    
    # Check if Nuclei is installed
    if not subprocess.run(["which", "nuclei"], capture_output=True).returncode == 0:
        return "Error: Nuclei is not installed. Please install it from https://github.com/projectdiscovery/nuclei#installation"
    
    # Build the command
    cmd = ["nuclei", "-u", target]
    
    # Add template filters if specified
    if templates:
        cmd.extend(["-t", ",".join(templates)])
    
    # Add severity filter if specified
    if severity:
        cmd.extend(["-s", severity])
    
    # Add output format
    if output_format == "json":
        cmd.extend(["-j"])
    
    print(cmd)
    try:
        # Run the scan
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error running Nuclei scan: {result.stderr}"
            
    except Exception as e:
        return f"Error executing Nuclei scan: {str(e)}"