import ollama
import sys

def scan_file(filepath):
    with open(filepath, 'r') as f:
        code = f.read()

    prompt = f"""You are a security expert. Analyze the following code for security vulnerabilities including:
- Hardcoded secrets or API keys
- SQL injection risks
- Insecure functions or imports
- Suspicious or obfuscated logic
- Authentication weaknesses
- Any other security concerns

Code to analyze:
{code}

Provide a clear security report with findings and recommendations."""

    print(f"\n🔍 Scanning {filepath}...\n")
    
    response = ollama.chat(model='phi3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    print(response['message']['content'])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scanner.py <file_to_scan>")
    else:
        scan_file(sys.argv[1])

