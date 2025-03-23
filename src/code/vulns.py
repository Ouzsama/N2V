import sys
import requests
import os
import json
import threading
from tabulate import tabulate
import time 
lock = threading.Lock()
config_api_path = os.path.join(os.path.dirname(__file__), "..", "config", "configApi.json")


def extract_vulnerability_info(json_data):
    vulnerabilities = []

    for item in json_data.get("data", {}).get("search", []):
        source = item.get("_source", {})

        vuln_info = {
            "CVE ID": source.get("id", "N/A"),
            "Title": source.get("title", "N/A"),
            "Severity": source.get("cvss", {}).get("severity", "N/A"),
            "Score": source.get("cvss", {}).get("score", "N/A"),
            "Link": source.get("href", "N/A"),
        }

        vulnerabilities.append(vuln_info)

    return vulnerabilities


def check_vulners():
    try:
        response = requests.get("https://vulners.com/")
        if response.status_code != 200:
            print("[Error]: vulners.com is unreachable!")
            sys.exit()
        return True
    except requests.exceptions.RequestException as e:
        print(f"[Error]: {e}")
        sys.exit()


def get_vulns(domain, ip, nmap_results, API_KEY):
    nmap_table = []
    vuln_table = []

    for result in nmap_results:
        # Store the Nmap scan data
        nmap_table.append([domain, ip, result["Port"], result["Service"], result["Version"]])

        # Query Vulners for vulnerabilities
        service, version = result["Service"], result["Version"]
        url = "https://vulners.com/api/v3/search/lucene/"
        query = f"{service} {version}"

        response = requests.get(url, params={"query": query, "apikey": API_KEY})

        try:
            data = response.json()
            if "error" in data and "no credits" in data["error"].lower():
                print("[Error]: API request failed due to insufficient credits.")
                sys.exit()

        except json.JSONDecodeError:
            print(f"[Error]: Invalid JSON response for {service} {version}")
            continue
        

        
        vulnerabilities = extract_vulnerability_info(data)

        for vuln in vulnerabilities:
            vuln_table.append([
                vuln["CVE ID"], vuln["Title"], vuln["Severity"], vuln["Score"], vuln["Link"]
            ])

    # Display Nmap Scan Information
    with lock:
        print(f"\n{'='*50}\n[Tracking]: Extracting vulnerabilities for {domain}:{ip}\n{'='*50}")
        print(tabulate(nmap_table, headers=["Domain", "IP", "Port", "Service", "Version"], tablefmt="grid"))

        # Display Vulners Results
        if vuln_table:
            print("\n[Results]: Found vulnerabilities")
            print(tabulate(vuln_table, headers=["CVE ID", "Title", "Severity", "Score", "Link"], tablefmt="grid"))
        else:
            print("\n[Results]: No known vulnerabilities found.")


def handle_vulns_targets(scan_result=None , user_agent = None  ):
    if not scan_result:
        print("[Info]: No Nmap results to retrieve information about.")
        time.sleep(1)
        sys.exit()

        
    if user_agent is not None : 
        requests.Session().headers.update({"User-Agent" : user_agent })
    
    try:
        if check_vulners():
            with open(config_api_path, "r") as file:
                config = json.load(file)

            API_KEY = config["Vulns"]
            Threads = []

            for domain, result in scan_result.items():
                for ip, r in result.items():
                    t = threading.Thread(target=get_vulns, args=(domain, ip, r, API_KEY))
                    t.start()
                    Threads.append(t)

            for t in Threads:
                t.join()
        else:
            sys.exit()

    except FileNotFoundError as e:
        print(f"[Error]: An error occurred: {e}")
        sys.exit()
