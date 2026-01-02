# Advanced Autonomous Network Scanner

## 📌 Project Overview

The **Advanced Autonomous Network Scanner** is a powerful cybersecurity reconnaissance and scanning tool built in **Python** for **authorized security testing and educational purposes**. It automates multiple industry‑standard tools to perform **subdomain enumeration, port scanning, service detection, vulnerability checks, and SSL/TLS analysis** with detailed and verbose output.

This project is ideal for **cybersecurity students, ethical hackers, SOC analysts, and penetration testers** who want an all‑in‑one automated reconnaissance solution on **Kali Linux**.

---

## 🚀 Features

* 🔍 Automated **subdomain enumeration** (Amass)
* 🌐 **Live host & port scanning** (Nmap)
* 🧠 **Service & OS detection**
* 🛡️ **Vulnerability scanning** (Nmap vuln scripts & Nikto)
* 🔐 **SSL/TLS security analysis** (SSLScan)
* 🧾 **Web technology fingerprinting** (WhatWeb)
* 📂 Organized output saved automatically
* 📊 Terminal preview of scan results
* ⏱️ Timed execution with summary report

---

## 🛠️ Tools & Technologies Used

* **Language:** Python 3
* **OS:** Kali Linux
* **Security Tools Integrated:**

  * Amass
  * Nmap
  * WhatWeb
  * Nikto
  * SSLScan
* **Python Modules:**

  * os
  * subprocess
  * sys
  * time

---

## 📂 Project Structure

```
advanced-network-scanner/
│── scanner.py
│── output/
│   ├── subdomains.txt
│   ├── nmap.txt
│   ├── nmap.xml
│   ├── whatweb.txt
│   ├── whatweb_verbose.txt
│   ├── nikto.txt
│   └── sslscan.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/gagandeep180/netvibe.git
cd advanced-network-scanner
```

### 2️⃣ Install Required Tools

```bash
sudo apt update
sudo apt install amass nmap whatweb nikto sslscan -y
```

### 3️⃣ Make Script Executable

```bash
chmod +x scanner.py
```

---

## ▶️ How to Run

### Run with Domain as Argument

```bash
./scanner.py example.com
```

### Or Run Interactively

```bash
python3 scanner.py
```

---

## 📊 Output & Results

All scan results are stored in the **output/** directory:

| File                | Description                    |
| ------------------- | ------------------------------ |
| subdomains.txt      | Discovered subdomains          |
| nmap.txt            | Detailed port & service scan   |
| nmap.xml            | XML output for browser viewing |
| whatweb.txt         | Web technologies detected      |
| whatweb_verbose.txt | Detailed WhatWeb output        |
| nikto.txt           | Web vulnerabilities            |
| sslscan.txt         | SSL/TLS security analysis      |

Preview results directly in terminal or open XML reports in a browser.

---

## 🔐 Ethical Use Disclaimer

⚠️ **This tool must only be used on systems you own or have explicit permission to test.**

Unauthorized scanning is illegal and unethical. The author is not responsible for misuse.

---

## 📚 Learning Outcomes

* Automated reconnaissance techniques
* Real‑world usage of Nmap, Amass, and Nikto
* Python scripting for cybersecurity
* Understanding ports, services, vulnerabilities, and SSL security

---

## 🔮 Future Enhancements

* 📄 Export reports to PDF/HTML
* 🧠 Add vulnerability correlation
* 📊 GUI dashboard
* ☁️ Cloud scan support
* 🔔 Alert & logging system

---

## 👤 Author

**Gagandeep Singh**
Cybersecurity Enthusiast | Ethical Hacker | SOC Analyst (Aspiring)

---

## ⭐ GitHub

If you find this project useful, please ⭐ star the repository and share feedback.
