import requests
import sys
import threading
import time
import subprocess
import shutil
import re
from tqdm import tqdm
from collections import defaultdict

lock = threading.Lock()
progress_bars = {}  # Dictionary to store progress bars per target
result_dict = defaultdict(lambda: defaultdict(list))  # Stores results in structured format


def get_bar_width():
    """Get half of the terminal width for progress bars."""
    terminal_width = shutil.get_terminal_size((80, 20)).columns  # Default to 80 columns if unavailable
    return max(terminal_width // 2, 20)  # Ensure a minimum width of 20


def track_scanning(data, domain, ip):
    """Update progress bars dynamically based on Nmap output."""
    match = re.search(r'About (\d+\.\d+)% done', data)  # Capture decimal progress
    if match:
        progress = float(match.group(1))

        with lock:
            if ip not in progress_bars:  # Create progress bar for each IP
                bar_width = get_bar_width()
                progress_bars[ip] = tqdm(
                    total=100,
                    desc=f"[Tracking] Nmap scan progress for [{domain}:{ip}]",
                    bar_format=f"{{l_bar}}{{bar:{bar_width}}} {{n_fmt}}/{{total_fmt}}%"
                )

            progress_bars[ip].n = progress
            progress_bars[ip].refresh()  # Refresh without causing multiple animations


def nmap(domain, ip):
    """Run Nmap scan and track progress in real-time, then return results."""
    global result_dict  # Ensure global scope access

    if not shutil.which("nmap"):
        print("\n[Error]: Nmap not found. Please install it and try again.")
        sys.exit(1)

    command = ["nmap", "-Pn", "-p-", "--open", "-sV", "--stats-every", "3s", ip]

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,  # Force line buffering
            universal_newlines=True
        )

        output_lines = []  # Store Nmap output

        # **Forcing unbuffered real-time output processing**
        while True:
            line = process.stdout.readline()
            if line == "" and process.poll() is not None:
                break  # Stop when process is done

            sys.stdout.flush()  # Force immediate output
            track_scanning(line.strip(), domain, ip)  # Update progress

            if "/tcp" in line.strip():  
                output_lines.append(line.strip())  # Store output for final print

            time.sleep(0.5)  # Reduce CPU load slightly

        process.stdout.close()
        process.wait()

        if process.returncode != 0:
            print(f"\n[Error]: Nmap exited with status {process.returncode}")
            return None  # Return None instead of exiting to avoid breaking execution

        # Process Nmap Output
        for line in output_lines:
            if " open " in line:
                q = line.split()
                result_dict[domain][ip].append({
                    "Port": q[0],
                    "Service": q[2],
                    "Version": " ".join(q[3:]) if len(q) >= 3 else "N/A"
                })

        return result_dict[domain][ip]  # Return structured data

    except Exception as e:
        print(f"\n[Error]: An unexpected error occurred - {str(e)}")
        return None  # Avoid breaking execution


def handle_targets(targets=None, user_agent=None):
    """Handle multiple scanning threads and return results."""
    try:
        if not targets:
            print("[Info] 0 targets to scan, exiting...")
            return None

        if user_agent:
            requests.Session().headers.update({"User-Agent": user_agent})

        threads = []
        for key, target_list in targets.items():
            for target in target_list:
                th = threading.Thread(target=nmap, args=(target[0], target[1]))  # Convert IP to string
                th.start()
                threads.append(th)

        print(f"\n[Info]: Starting target scan, {sum(len(v) for v in targets.values())} target(s) to scan...")

        for t in threads:
            t.join()

        return result_dict  # Return structured results

    except KeyboardInterrupt:
        print("\n[Error]: Scan interrupted by user.")
        sys.exit(1)
