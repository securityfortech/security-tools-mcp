from typing import Optional
from .base import ToolWrapper


class FfufWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("ffuf")
        
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