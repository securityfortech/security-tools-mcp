import subprocess
from typing import List, Optional


def run_nmap(
    target: str,
    ports: Optional[str] = None,
    options: Optional[List[str]] = None,
) -> str:
    """Run an Nmap network scan on the specified target.
    
    Args:
        target: The target IP or hostname to scan
        ports: Specific ports to scan (e.g., "22,80,443")
        options: Additional Nmap options (e.g., ["-sV", "-A"])
    
    Returns:
        str: The scan results
    """
    print(f"[debug] run_nmap({target}, ports={ports}, options={options})")
    
    if not subprocess.run(["which", "nmap"], capture_output=True).returncode == 0:
        return "Error: Nmap is not installed. Install it with 'sudo apt install nmap' or similar."
    
    cmd = ["nmap", target]
    if ports:
        cmd.extend(["-p", ports])
    if options:
        cmd.extend(options)
    
    print(cmd)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing Nmap scan: {str(e)}"