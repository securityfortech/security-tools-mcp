# Security Operations Multi-Tool Platform (MCP)

A comprehensive security operations platform that integrates multiple security tools into a unified interface. This platform provides a centralized way to run various security scanning and testing tools.

## Features

- **Unified Interface**: Single entry point for multiple security tools
- **Docker Support**: Easy deployment using Docker
- **JSON Output**: Consistent JSON output format across all tools
- **Error Handling**: Robust error handling and reporting
- **Extensible**: Easy to add new tools and functionality

## Included Tools

- **Nuclei**: Fast and customizable vulnerability scanner
- **FFUF**: Fast web fuzzer and content discovery tool
- **Amass**: In-depth attack surface mapping and external asset discovery
- **Dirsearch**: Web path scanner
- **Hashcat**: Advanced password recovery
- **HTTPX**: Fast and multi-purpose HTTP toolkit
- **IPInfo**: IP address information gathering
- **Nmap**: Network exploration and security auditing
- **SQLMap**: Automatic SQL injection and database takeover tool
- **Subfinder**: Subdomain discovery tool
- **TLSX**: TLS/SSL scanning and analysis
- **WFuzz**: Web application fuzzer
- **XSStrike**: Advanced XSS detection and exploitation

## Installation

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/securityfortech/secops-mcp.git
   cd secops-mcp
   ```

2. Build the Docker image:
   ```bash
   docker build -t secops-mcp .
   ```

3. Run the container:
   ```bash
   docker run -it --rm secops-mcp
   ```

### Manual Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/securityfortech/secops-mcp.git
   cd secops-mcp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install required tools:
   - Follow the installation instructions for each tool in the `tools/` directory
   - Ensure all tools are in your system PATH

## Usage

1. Start the application:
   ```bash
   python main.py
   ```

2. The application will provide a unified interface for running various security tools.

3. Each tool returns results in a consistent JSON format:
   ```json
   {
       "success": boolean,
       "error": string (if error),
       "results": object (if success)
   }
   ```

## Tool Configuration

Each tool can be configured through its respective wrapper in the `tools/` directory. Configuration options include:

- Output formats
- Timeouts
- Verbosity levels
- Custom wordlists
- Tool-specific parameters

## Security Considerations

- This tool is for authorized security testing only
- Always obtain proper authorization before scanning systems
- Be mindful of rate limiting and scanning intensity
- Respect robots.txt and terms of service
- Use appropriate wordlists and scanning parameters

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- All the security tools and their developers
- The security community for their contributions and support
