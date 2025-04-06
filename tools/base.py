import subprocess
from typing import List, Dict, Any, Optional, Union


class ToolWrapper:
    """Base class for security tool wrappers to reduce code duplication."""
    
    def __init__(self, tool_name: str):
        """Initialize the tool wrapper.
        
        Args:
            tool_name: Name of the security tool
        """
        self.tool_name = tool_name
        
    def _check_installed(self) -> bool:
        """Check if the tool is installed."""
        return subprocess.run(["which", self.tool_name], capture_output=True).returncode == 0
    
    def _build_command(self, base_cmd: List[str], options: Dict[str, Any]) -> List[str]:
        """Build command with options.
        
        Args:
            base_cmd: Base command list
            options: Dictionary of option name to value
            
        Returns:
            List[str]: Complete command
        """
        cmd = base_cmd.copy()
        
        for option, value in options.items():
            if value is None:
                continue
                
            if isinstance(value, bool) and value:
                cmd.append(f"-{option}")
            elif isinstance(value, list):
                cmd.extend([f"-{option}", ",".join(map(str, value))])
            else:
                cmd.extend([f"-{option}", str(value)])
                
        return cmd
    
    def _execute(self, cmd: List[str]) -> str:
        """Execute the command and return the result.
        
        Args:
            cmd: Command to execute
            
        Returns:
            str: Command output or error message
        """
        if not self._check_installed():
            return f"Error: {self.tool_name} is not installed."
            
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                return result.stdout or "Command executed successfully"
            else:
                return f"Error running {self.tool_name}: {result.stderr}"
                
        except Exception as e:
            return f"Error executing {self.tool_name}: {str(e)}" 