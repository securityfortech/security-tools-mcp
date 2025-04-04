import subprocess
from typing import Optional


def run_ffuf(
    url: str,
    wordlist: str,
    filter_code: Optional[str] = "404",
) -> str:
    """Run ffuf to fuzz web application endpoints.
    
    Args:
        url: Target URL with FUZZ keyword (e.g., "http://example.com/FUZZ")
        wordlist: Path to wordlist file
        filter_code: HTTP status code to filter out (e.g., "404")
    
    Returns:
        str: ffuf output
    """
    print(f"[debug] run_ffuf({url}, {wordlist}, filter_code={filter_code})")
    
    if not subprocess.run(["which", "ffuf"], capture_output=True).returncode == 0:
        return "Error: ffuf is not installed. See https://github.com/ffuf/ffuf"
    
    cmd = ["ffuf", "-u", url, "-w", wordlist, "-fc", filter_code]
    
    print(cmd)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing ffuf: {str(e)}"