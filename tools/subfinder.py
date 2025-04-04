import subprocess
from typing import Optional


def run_subfinder(
    domain: str,
    output_format: Optional[str] = "text",
) -> str:
    """Run subfinder to enumerate subdomains.
    
    Args:
        domain: Target domain to enumerate
        output_format: Output format (text or json)
    
    Returns:
        str: Subfinder output
    """
    print(f"[debug] run_subfinder({domain}, output_format={output_format})")
    
    if not subprocess.run(["which", "subfinder"], capture_output=True).returncode == 0:
        return "Error: subfinder is not installed. See https://github.com/projectdiscovery/subfinder"
    
    cmd = ["subfinder", "-d", domain]
    if output_format == "json":
        cmd.append("-json")
    
    print(cmd)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing subfinder: {str(e)}"