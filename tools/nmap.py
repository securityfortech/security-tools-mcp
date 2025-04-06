from typing import List, Optional
from .base import ToolWrapper


class NmapWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("nmap")
        
    def scan(
        self,
        target: str,
        ports: Optional[str] = None,
        scan_type: Optional[str] = "sV",
    ) -> str:
        """Run an Nmap network scan on the specified target.
        
        Args:
            target: The target IP or hostname to scan
            ports: Specific ports to scan (e.g., "22,80,443")
            scan_type: Scan type (e.g., "sV" for service detection)
        
        Returns:
            str: The scan results
        """
        base_cmd = ["nmap", target]
        
        # Build options
        options = {}
        
        if ports:
            # Port handling is special in nmap
            base_cmd.extend(["-p", ports])
            
        if scan_type:
            # Add scan type with dash
            base_cmd.append(f"-{scan_type}")
            
        return self._execute(base_cmd)


# Create a singleton instance
nmap = NmapWrapper()


def run_nmap(
    target: str,
    ports: Optional[str] = None,
    scan_type: Optional[str] = "sV",
) -> str:
    """Backward-compatible function that uses the NmapWrapper class."""
    return nmap.scan(target, ports, scan_type)