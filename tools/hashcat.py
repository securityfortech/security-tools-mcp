import subprocess
from typing import Optional


def run_hashcat(
    hash_file: str,
    wordlist: str,
    mode: Optional[int] = 0,  # Default to MD5
) -> str:
    """Run Hashcat to crack hashes.
    
    Args:
        hash_file: Path to file containing hashes
        wordlist: Path to wordlist file
        mode: Hash type (e.g., 0 for MD5, 1000 for NTLM)
    
    Returns:
        str: Hashcat output
    """
    print(f"[debug] run_hashcat({hash_file}, {wordlist}, mode={mode})")
    
    if not subprocess.run(["which", "hashcat"], capture_output=True).returncode == 0:
        return "Error: Hashcat is not installed. See https://hashcat.net/hashcat/"
    
    cmd = ["hashcat", "-m", str(mode), hash_file, wordlist]
    
    print(cmd)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Error executing Hashcat: {str(e)}"