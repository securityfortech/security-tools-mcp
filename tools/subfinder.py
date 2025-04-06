from typing import Optional
from .base import ToolWrapper


class SubfinderWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("subfinder")
        
    def enumerate(
        self,
        domain: str,
        recursive: bool = False,
    ) -> str:
        """Run subfinder to enumerate subdomains.
        
        Args:
            domain: Target domain to enumerate
            recursive: Whether to recursively enumerate subdomains
        
        Returns:
            str: Subfinder output
        """
        base_cmd = ["subfinder"]
        
        options = {
            "d": domain,
            "json": True  # Always use JSON for consistent output
        }
        
        # Add recursive flag if specified
        if recursive:
            options["recursive"] = True
            
        cmd = self._build_command(base_cmd, options)
        return self._execute(cmd)


# Create a singleton instance
subfinder = SubfinderWrapper()


def run_subfinder(
    domain: str,
    recursive: bool = False,
) -> str:
    """Backward-compatible function that uses the SubfinderWrapper class."""
    return subfinder.enumerate(domain, recursive)