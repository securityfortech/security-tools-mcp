import subprocess
from typing import List, Optional


def run_tlsx(
    targets: List[str],
    options: Optional[List[str]] = None,
) -> str:
    """Run tlsx to analyze TLS configurations.
    
    Args:
        targets: List of target domains or IPs
        options: Additional tlsx options (e.g., ["-scan-mode", "full"])
    
    Returns:
        str: tlsx output
    """
    print(f"[debug] run_tlsx({targets}, options={options})")
    
    if not subprocess.run(["which", "tlsx"], capture_output=True).returncode == 0:
        return "Error: tlsx is not installed. See https://github.com/projectdiscovery/tlsx"
    
    cmd = ["tlsx", "-l", "-"]  # Use stdin for list input
    if options:
        cmd.extend(options)
    
    print(cmd)
    try:
        result = subprocess.run(cmd, input="\n".join(targets), capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing tlsx: {str(e)}"