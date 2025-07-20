
# **N2V - Nmap & Vulners Vulnerability Scanner**  

## **Description**  
**N2V** is a lightweight cybersecurity tool designed to automate vulnerability identification based on **Nmap** scan results. It extracts service and version data from scanned targets, queries a vulnerability API (**Vulners.com**), and displays associated **CVEs** — making it easier to assess risk quickly and efficiently.

- **By:** Oussama A. Belaiche (*Ouzsama*)  

## **Features**  
✅ Utilizes **Nmap** for network scanning.  
✅ Integrates with **Vulners.com** to identify known vulnerabilities.  
✅ Supports **custom User-Agent headers** for stealthier scans.  
✅ Allows setting a **Vulners API key** for enhanced vulnerability detection.  
✅ Simple and efficient **command-line interface**.  

---

## **Installation**  

### **Prerequisites**  
Ensure you have the following installed:  
- **Python 3.x**  
- **Nmap** installed on your system  
- Required Python dependencies:  

```bash
git clone https://github.com/Ouzsama/N2V
cd N2V
pip install -r requirements.txt
```

---

## **Usage**  
Run the tool with the required parameters:  

```bash
python3 n2v.py -t <target_domain>
```

### **Options**  
| Flag            | Description                           |
|----------------|--------------------------------------|
| `-t`          | Specify the target domain/IP         |
| `-h`          | Show help message                    |
| `--user-agent` | Set a custom User-Agent header      |
| `--vulners-api` | Set the Vulners API key            |

---

## **Example Usage**  

### **1. Scan a Domain for Vulnerabilities**  
```bash
python3 n2v.py -t example.com --vulners-api YOUR_API_KEY
```
📌 **Execution Result:**  
Two target execution results:  

![Execution Result 1](src/assets/n2vimage.png)  
![Execution Result 2](src/assets/n2vimage2.png)  
![Execution Result 3](src/assets/n2vimage3.png)  

---

### **2. Set a Custom User-Agent**  
```bash
python3 n2v.py -t example.com --user-agent "Mozilla/5.0"
```
📌 **Execution Result:**  
*(Insert image here)*  

---

## **Notes**  
⚠️ **Nmap must be installed** on your system.  
⚠️ The **Vulners API key** is required for full vulnerability detection.  
⚠️ Run the script with **sudo** if required by Nmap.  

---

## **Disclaimer**  
This tool is for **educational and security research** purposes only. The author is **not responsible for any misuse**.  

---

## **Follow Me**  
For more tools and updates, follow me on:  
🔗 [GitHub](https://github.com/Ouzsama)  

---

**🛠 Developed by:** Oussama A. Belaiche

