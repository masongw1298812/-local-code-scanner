# -local-code-scanner
"Free local AI-powered code security scanner. No API costs — runs entirely on your machine with Ollama."
# Local Code Security Scanner

A free, local AI-powered security scanner for your code. 
No API costs — runs entirely on your machine using Ollama.

## What it does
Analyzes your code files and flags:
- Hardcoded secrets or API keys
- SQL injection risks
- Insecure functions or imports
- Suspicious logic
- Dependency vulnerabilities

## Requirements
- Python 3
- Ollama (ollama.com)
- Phi3 model

## Installation
git clone https://github.com/masongw1298812/-local-code-scanner.git
cd -local-code-scanner
pip install ollama
ollama pull phi3

## Usage
python3 scanner.py yourfile.py

## Why local?
No data leaves your machine. Free forever.
