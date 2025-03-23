def gethelp () : 
  h = """
  N2V - Nmap & Vulners Vulnerability Scanner
  ==========================================

  Description:
  ------------
  N2V is a cybersecurity tool designed to automate vulnerability detection using Nmap and Vulners.com.

  Usage:
  ------
  python3 n2v.py -t <target_domain> [OPTIONS]

  Options:
  --------
    -t              Specify the target domain
    -h              Show this help message
    -user-agent    Set a custom User-Agent header
    -vulners-api   Set the Vulners API key

  Examples:
  ---------
    Scan a domain for vulnerabilities:
      python3 n2v.py -t example.com

    Scan with a custom User-Agent:
      python3 n2v.py -t example.com --user-agent "Mozilla/5.0"

    Scan with a Vulners API key:
      python3 n2v.py -t example.com --vulners-api YOUR_API_KEY

  Notes:
  ------
  - Requires Python 3.x and Nmap installed.
  - Vulners API key is needed for full vulnerability detection.
  - Run with sudo if needed.

  Developed by: Oussama A. Belaiche  
  GitHub: https://github.com/Oussama-A-Belaiche
  """
  print(h)