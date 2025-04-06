# tools/nuclei.py
from typing import List, Optional
from .base import ToolWrapper


class NucleiWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("nuclei")
        
    def scan(
        self,
        target: str,
        templates: Optional[List[str]] = None,
        severity: Optional[str] = None,
        output_format: str = "json",
    ) -> str:
        """Run a Nuclei security scan on the specified target.
        
        Args:
            target: The target URL or IP to scan
            templates: List of specific template names to use (optional)
            severity: Filter by severity level (critical, high, medium, low, info)
            output_format: Output format (json, text)
        
        Returns:
            str: The scan results in the specified format
        """
        base_cmd = ["nuclei", "-u", target]
        
        options = {}
        
        # Add template filters if specified
        if templates:
            options["t"] = templates
        
        # Add severity filter if specified
        if severity:
            options["s"] = severity
        
        # Add output format
        if output_format == "json":
            options["j"] = True
        
        cmd = self._build_command(base_cmd, options)
        return self._execute(cmd)


# Create a singleton instance
nuclei = NucleiWrapper()


def run_nuclei(
    target: str,
    templates: Optional[List[str]] = None,
    severity: Optional[str] = None,
    output_format: str = "json",
) -> str:
    """Backward-compatible function that uses the NucleiWrapper class."""
    return nuclei.scan(target, templates, severity, output_format)