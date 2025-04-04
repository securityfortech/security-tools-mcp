FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install required system dependencies for security tools
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    git \
    curl \
    nmap \
    wfuzz \
    sqlmap \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up tools directory
RUN mkdir -p /tools
ENV PATH="/tools:${PATH}"

# Install Nuclei
RUN wget -q https://github.com/projectdiscovery/nuclei/releases/download/v2.9.10/nuclei_2.9.10_linux_amd64.zip && \
    unzip -o nuclei_2.9.10_linux_amd64.zip -d /tools && \
    rm nuclei_2.9.10_linux_amd64.zip && \
    chmod +x /tools/nuclei

# Install FFUF
RUN wget -q https://github.com/ffuf/ffuf/releases/download/v2.0.0/ffuf_2.0.0_linux_amd64.tar.gz && \
    tar -xzf ffuf_2.0.0_linux_amd64.tar.gz -C /tools && \
    rm ffuf_2.0.0_linux_amd64.tar.gz && \
    chmod +x /tools/ffuf

# Install HTTPX
RUN wget -q https://github.com/projectdiscovery/httpx/releases/download/v1.3.4/httpx_1.3.4_linux_amd64.zip && \
    unzip -o httpx_1.3.4_linux_amd64.zip -d /tools && \
    rm httpx_1.3.4_linux_amd64.zip && \
    chmod +x /tools/httpx

# Install Subfinder
RUN wget -q https://github.com/projectdiscovery/subfinder/releases/download/v2.6.2/subfinder_2.6.2_linux_amd64.zip && \
    unzip -o subfinder_2.6.2_linux_amd64.zip -d /tools && \
    rm subfinder_2.6.2_linux_amd64.zip && \
    chmod +x /tools/subfinder

# Install TLSX
RUN wget -q https://github.com/projectdiscovery/tlsx/releases/download/v1.1.2/tlsx_1.1.2_linux_amd64.zip && \
    unzip -o tlsx_1.1.2_linux_amd64.zip -d /tools && \
    rm tlsx_1.1.2_linux_amd64.zip && \
    chmod +x /tools/tlsx

# Install XSStrike
RUN git clone https://github.com/s0md3v/XSStrike.git /opt/XSStrike \
    && pip install -r /opt/XSStrike/requirements.txt || true

# Copy requirements.txt
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app
WORKDIR /app

# Command to run the application
CMD ["python", "server.py"] 