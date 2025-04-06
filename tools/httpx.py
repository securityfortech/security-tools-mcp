from typing import List, Optional
from .base import ToolWrapper


class HttpxWrapper(ToolWrapper):
    def __init__(self):
        super().__init__("httpx")
        
    def scan(
        self,
        urls: List[str],
        status_codes: Optional[List[int]] = None,
    ) -> str:
        """Run httpx to probe HTTP servers.
        
        Args:
            urls: List of target URLs or IPs
            status_codes: Filter results by status codes
        
        Returns:
            str: httpx output
        """
        base_cmd = ["httpx"]
        
        options = {}
        
        # Add status code filter if specified
        if status_codes:
            options["mc"] = status_codes
        
        # Add silent mode and json output for cleaner results
        options["silent"] = True
        options["json"] = True
        
        cmd = self._build_command(base_cmd, options)
        
        # Special handling for URLs
        input_text = "\n".join(urls)
        
        # Use subprocess directly as _execute doesn't support input
        if not self._check_installed():
            return f"Error: {self.tool_name} is not installed."
            
        try:
            import subprocess
            result = subprocess.run(cmd, input=input_text, capture_output=True, text=True)
            
            if result.returncode == 0:
                return result.stdout or "Command executed successfully"
            else:
                return f"Error running {self.tool_name}: {result.stderr}"
                
        except Exception as e:
            return f"Error executing {self.tool_name}: {str(e)}"


# Create a singleton instance
httpx = HttpxWrapper()


def run_httpx(
    urls: List[str],
    status_codes: Optional[List[int]] = None,
) -> str:
    """Backward-compatible function that uses the HttpxWrapper class."""
    return httpx.scan(urls, status_codes)