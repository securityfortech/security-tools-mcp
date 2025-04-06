from typing import Optional
from .base import ToolWrapper


class HashcatWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("hashcat")
        
    def crack(
        self,
        hash_file: str,
        wordlist: str,
        hash_type: str,
    ) -> str:
        """Run Hashcat to crack hashes.
        
        Args:
            hash_file: Path to file containing hashes
            wordlist: Path to wordlist file
            hash_type: Hash type code (e.g., "0" for MD5, "1000" for NTLM)
        
        Returns:
            str: Hashcat output
        """
        base_cmd = ["hashcat"]
        
        # Convert hash_type to a number for -m parameter
        hash_mode = int(hash_type) if hash_type.isdigit() else 0
        
        options = {
            "m": hash_mode
        }
        
        cmd = self._build_command(base_cmd, options)
        
        # Add hash_file and wordlist as positional arguments
        cmd.extend([hash_file, wordlist])
        
        return self._execute(cmd)


# Create a singleton instance
hashcat = HashcatWrapper()


def run_hashcat(
    hash_file: str,
    wordlist: str,
    hash_type: str,
) -> str:
    """Backward-compatible function that uses the HashcatWrapper class."""
    return hashcat.crack(hash_file, wordlist, hash_type)