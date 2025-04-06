from typing import Optional
from .base import ToolWrapper


class SqlmapWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("sqlmap")
        
    def is_available(self) -> bool:
        """Check if sqlmap is installed and accessible.
        
        Returns:
            bool: True if sqlmap is available, False otherwise
        """
        return self._check_installed()
        
    def scan(
        self,
        url: str,
        risk: Optional[int] = 1,
        level: Optional[int] = 1,
    ) -> str:
        """Run sqlmap to test for SQL injection vulnerabilities.
        
        Args:
            url: Target URL to scan
            risk: Risk level (1-3, higher = more dangerous tests)
            level: Level of tests to perform (1-5, higher = more tests)
        
        Returns:
            str: sqlmap output
        """
        base_cmd = ["sqlmap", "-u", url, "--batch"]
        
        options = {
            "risk": risk,
            "level": level
        }
        
        cmd = self._build_command(base_cmd, options)
        return self._execute(cmd)


# Create a singleton instance
sqlmap = SqlmapWrapper()


def run_sqlmap(
    url: str,
    risk: Optional[int] = 1,
    level: Optional[int] = 1,
) -> str:
    """Backward-compatible function that uses the SqlmapWrapper class."""
    return sqlmap.scan(url, risk, level)


def check_sqlmap_available() -> str:
    """Check if sqlmap is installed and available.
    
    Returns:
        str: Success message if available, error message if not
    """
    if sqlmap.is_available():
        return "SQLMap is installed and accessible."
    else:
        return "SQLMap is not installed or not accessible."