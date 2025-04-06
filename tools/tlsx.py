from typing import Optional
from .base import ToolWrapper


class TlsxWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("tlsx")
        
    def is_available(self) -> bool:
        """Check if tlsx is installed and accessible.
        
        Returns:
            bool: True if tlsx is available, False otherwise
        """
        return self._check_installed()
        
    def scan(
        self,
        host: str,
        port: Optional[int] = 443,
    ) -> str:
        """Run tlsx to analyze TLS configurations.
        
        Args:
            host: Target host to analyze
            port: Port to connect to
        
        Returns:
            str: tlsx output
        """
        # Build target with port
        target = f"{host}:{port}"
        base_cmd = ["tlsx", "-u", target]
        
        options = {
            "json": True,  # Always use JSON for consistent output
            "scan-mode": "full"  # More comprehensive scan
        }
            
        cmd = self._build_command(base_cmd, options)
        return self._execute(cmd)


# Create a singleton instance
tlsx = TlsxWrapper()


def run_tlsx(
    host: str,
    port: Optional[int] = 443,
) -> str:
    """Backward-compatible function that uses the TlsxWrapper class."""
    return tlsx.scan(host, port)


def check_tlsx_available() -> str:
    """Check if tlsx is installed and available.
    
    Returns:
        str: Success message if available, error message if not
    """
    if tlsx.is_available():
        return "Tlsx is installed and accessible."
    else:
        return "Tlsx is not installed or not accessible."