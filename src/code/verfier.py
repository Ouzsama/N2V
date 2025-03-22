
# TODO : integerat information gathering on targets , using whois or other tools
import requests
import socket
import sys
import itertools
import threading
import time
import ipaddress
import subprocess
from collections import defaultdict 

lock = threading.Lock()
validated = defaultdict(list)

# Function to check if the target is reachable using ping
def is_reachable(target):
    try:
        param = "-n" if sys.platform.startswith("win") else "-c"
        subprocess.run(["ping", param, "1", target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Function to verify a single target
def verify(target):
    global validated

    # Check if target is reachable
    if not is_reachable(target):
        print(f"\n{'':<10}[Warning]: {target} is unreachable. Skipping...")
        return

    for port in [80, 443, 8080, 8443]:  # Try multiple ports
        try:
            response = requests.get(f'http://{target}:{port}', timeout=5)
            if response.status_code < 400:
                try:
                    ip = ipaddress.ip_address(target)
                    validated["IP address"].append(target)
                except ValueError:
                    try:
                        cidr = ipaddress.ip_network(target, strict=False)
                        validated["CIDR"].append([target] + [str(c) for c in cidr])
                    except ValueError:
                        try:
                            domain = socket.gethostbyname(target)
                            validated["Domain names"].append([target, domain])
                        except socket.gaierror:
                            print(f"\n{'':<10}[Warning]: {target} cannot be resolved to an IP address.")
                return  # Stop once a valid port is found
        except requests.exceptions.RequestException:
            continue  # Try next port

    print(f"\n{'':<10}[Error]: {target} is not a valid HTTP target.")

# Function to verify multiple targets with animation
def verify_targets(targets, user_agent):
    if not targets:
        print(f"{'':<10}[Info]: 0 targets to verify, quitting..")
        sys.exit()

    if user_agent:
        session = requests.Session()
        session.headers.update({"User-Agent": user_agent})  # Set custom User-Agent

    print(f"[Info]: Starting target verification, {len(targets)} to verify")

    Threads = []
    for target in targets:
        t = threading.Thread(target=verify, args=(target,))
        t.start()
        Threads.append(t)

    animation = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])

    while any(t.is_alive() for t in Threads):
        with lock:
            scanned = len([t for t in Threads if not t.is_alive()])
            sys.stdout.write(f"\r{'':<10}{next(animation)} {scanned} out of {len(targets)} targets verified ")
            sys.stdout.flush()
        time.sleep(0.3)

    for t in Threads:
        t.join()


    print(f"\n{'':<10}[Info]: Validated targets ")
    for k ,v  in validated.items() : 
        if k == "Domain names" : 
            for t in  v : 
                print (f"{'':<10}{t[0]} : {t[1]}")
        else  :
            for t in  v : 
                print (f"{'':<10}{t[0]}")
    
    return validated


