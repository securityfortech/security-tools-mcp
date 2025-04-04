# secops-mcp

All-in-one security testing toolbox that brings together popular open source tools through a single MCP interface. Connected to an AI agent, it enables tasks like pentesting, bug bounty hunting, threat hunting, and more.

## Getting Started

### Prerequisites

- Docker (for containerized deployment)
- Claude Desktop

### Installation

```bash
git clone https://github.com/securityfortech/secops-mcp
cd secops-mcp
docker build -t secops-mcp .
```
### Claude Desktop Integration

Edit your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "secops-mcp": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "secops-mcp"]
    }
  }
}
```

## Available Tools

- **Nuclei**: `nuclei_scan_wrapper(target, templates, severity, output_format)` - Vulnerability scanner with template-based detection
- **FFuf**: `ffuf_wrapper(url, wordlist, filter_code)` - Fast web fuzzer for content discovery
- **WFuzz**: `wfuzz_wrapper(url, wordlist, filter_code)` - Web application fuzzer
- **SQLMap**: `sqlmap_wrapper(url, risk, level)` - Automatic SQL injection detection and exploitation
- **Nmap**: `nmap_wrapper(target, ports, scan_type)` - Network discovery and security auditing
- **Hashcat**: `hashcat_wrapper(hash_file, wordlist, hash_type)` - Advanced password recovery
- **HTTPX**: `httpx_wrapper(urls, status_codes)` - Fast HTTP probing with concurrency
- **Subfinder**: `subfinder_wrapper(domain, recursive)` - Subdomain discovery tool
- **TLSX**: `tlsx_wrapper(host, port)` - TLS grabber and analyzer
- **XSStrike**: `xsstrike_wrapper(url, crawl)` - Advanced XSS detection suite
- **Amass**: `amass_wrapper(domain, passive)` - Network mapping of attack surfaces
- **Dirsearch**: `dirsearch_wrapper(url, extensions, wordlist)` - Web path scanner
- **Metasploit**: `metasploit_wrapper(target, exploit, payload)` - Exploitation framework
- **Nikto**: `nikto_wrapper(target, tuning)` - Web server scanner for vulnerabilities

## Security Considerations

- Only use for authorized security testing
- Follow responsible disclosure practices
- Keep all security tools updated

## License

This project is licensed under the MIT License.
