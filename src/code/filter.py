
import requests
import vulners
if  __name__ == "__main__" : 
     result = [
    '21/tcp  open  ftp           ProFTPD 1.3.3c',
    '22/tcp  open  ssh           OpenSSH 5.3p1 Debian 3ubuntu7',
    '25/tcp  open  smtp          Exim smtpd 4.69',
    '80/tcp  open  http          Apache httpd 2.2.14',
    '110/tcp open  pop3          Dovecot pop3d 1.2.9',
    '143/tcp open  imap          Courier imapd 4.8.1',
    '443/tcp open  ssl/http      Apache httpd 2.2.14',
    '3306/tcp open  mysql         MySQL 5.0.51a-3ubuntu5',
    '8080/tcp open  http-proxy    Squid http proxy 2.7.STABLE7'
    ]




     API_KEY =  "WTK5PJ10W8XAQ2UL6DFO6L96AWH57ZWLTRZHCCB3FVM1VLRF2A3ILD6CG90O570Y"
     vulners_api = vulners.Vulners(api_key=API_KEY)
    

     query = []
     for line in result:
        if "open" in line:
            q = line.split()
            q = " ".join(q[3:])  # This extracts "HAProxy http proxy 1.3.1 - 1.9.0"
            print(f"Querying: {q}")

            search_result = vulners_api.find_all(f"type:cve AND {q}")

            # Display results
            if search_result:
                for vuln in search_result:
                    print(f"CVE: {vuln['id']}, Description: {vuln['description']}")
            else:
                print("No vulnerabilities found for", q)






# Example query: Searching vulnerabilities for HAProxy