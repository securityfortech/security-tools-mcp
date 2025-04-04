import subprocess
from typing import Optional


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
        str: wfuzz output
    """
    print(f"[debug] run_wfuzz({url}, {wordlist}, hide_code={hide_code})")
    
    if not subprocess.run(["which", "wfuzz"], capture_output=True).returncode == 0:
        return "Error: wfuzz is not installed. Install with 'pip install wfuzz'"
    
    cmd = ["wfuzz", "-w", wordlist, "--hc", hide_code, url]
    
    print(cmd)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing wfuzz: {str(e)}"