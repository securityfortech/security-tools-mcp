from typing import Optional
from .base import ToolWrapper


class XSStrikeWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("python")  # XSStrike is typically run with python
        
    def scan(
        self,
        url: str,
        crawl: bool = False,
    ) -> str:
        """Run XSStrike to detect XSS vulnerabilities.
        
        Args:
            url: Target URL to scan
            crawl: Whether to crawl the website for additional URLs
        
        Returns:
            str: XSStrike output
        """
        # XSStrike is typically installed in /opt/XSStrike
        base_cmd = ["python", "/opt/XSStrike/xsstrike.py", "--url", url]
        
        # Build options
        options = {}
        
        # Add crawl flag if specified
        if crawl:
            base_cmd.append("--crawl")
            
        return self._execute(base_cmd)


# Create a singleton instance
xsstrike = XSStrikeWrapper()


def run_xsstrike(
    url: str,
    crawl: bool = False,
) -> str:
    """Backward-compatible function that uses the XSStrikeWrapper class."""
    return xsstrike.scan(url, crawl)