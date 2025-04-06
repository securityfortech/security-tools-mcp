from typing import Optional
from .base import ToolWrapper


class XSStrikeWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("python")  # XSStrike is typically run with python
        
    def is_available(self) -> bool:
        """Check if XSStrike is installed and accessible.
        
        Returns:
            bool: True if XSStrike is available, False otherwise
        """
        # Check for XSStrike script instead of python
        import os
        return os.path.exists("/opt/XSStrike/xsstrike.py")
        
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


def check_xsstrike_available() -> str:
    """Check if XSStrike is installed and available.
    
    Returns:
        str: Success message if available, error message if not
    """
    if xsstrike.is_available():
        return "XSStrike is installed and accessible."
    else:
        return "XSStrike is not installed or not accessible."