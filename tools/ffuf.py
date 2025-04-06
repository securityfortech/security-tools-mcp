from typing import Optional
from .base import ToolWrapper


class FfufWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("ffuf")
        
    def is_available(self) -> bool:
        """Check if ffuf is installed and accessible.
        
        Returns:
            bool: True if ffuf is available, False otherwise
        """
        return self._check_installed()
        
    def fuzz(
        self,
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
        base_cmd = ["ffuf", "-u", url, "-w", wordlist]
        
        options = {
            "fc": filter_code
        }
        
        cmd = self._build_command(base_cmd, options)
        return self._execute(cmd)


# Create a singleton instance
ffuf = FfufWrapper()


def run_ffuf(
    url: str,
    wordlist: str,
    filter_code: Optional[str] = "404",
) -> str:
    """Backward-compatible function that uses the FfufWrapper class."""
    return ffuf.fuzz(url, wordlist, filter_code)


def check_ffuf_available() -> str:
    """Check if ffuf is installed and available.
    
    Returns:
        str: Success message if available, error message if not
    """
    if ffuf.is_available():
        return "Ffuf is installed and accessible."
    else:
        return "Ffuf is not installed or not accessible."