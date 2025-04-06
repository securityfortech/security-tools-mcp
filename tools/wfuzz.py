from typing import Optional
from .base import ToolWrapper


class WfuzzWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("wfuzz")
        
    def is_available(self) -> bool:
        """Check if wfuzz is installed and accessible.
        
        Returns:
            bool: True if wfuzz is available, False otherwise
        """
        return self._check_installed()
        
    def fuzz(
        self,
        url: str,
        wordlist: str,
        filter_code: Optional[str] = "404",
    ) -> str:
        """Run wfuzz to fuzz web application endpoints.
        
        Args:
            url: Target URL with FUZZ keyword (e.g., "http://example.com/FUZZ")
            wordlist: Path to wordlist file
            filter_code: HTTP status code to hide (e.g., "404")
        
        Returns:
            str: wfuzz output
        """
        base_cmd = ["wfuzz", "-w", wordlist]
        
        options = {
            "hc": filter_code
        }
        
        cmd = self._build_command(base_cmd, options)
        
        # URL is added at the end of the command
        cmd.append(url)
        
        return self._execute(cmd)


# Create a singleton instance
wfuzz = WfuzzWrapper()


def run_wfuzz(
    url: str,
    wordlist: str,
    hide_code: Optional[str] = "404",
) -> str:
    """Backward-compatible function that uses the WfuzzWrapper class."""
    return wfuzz.fuzz(url, wordlist, hide_code)


def check_wfuzz_available() -> str:
    """Check if wfuzz is installed and available.
    
    Returns:
        str: Success message if available, error message if not
    """
    if wfuzz.is_available():
        return "Wfuzz is installed and accessible."
    else:
        return "Wfuzz is not installed or not accessible."