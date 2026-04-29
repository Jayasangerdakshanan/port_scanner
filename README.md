# 🔍 Python Port Scanner (with Banner Grabbing)

A simple Python-based port scanner built using socket programming.  
It supports IP and domain scanning, single port checks, port range scanning, and basic banner grabbing for open ports.

---

## ⚙️ Features

- 🌐 Scan domain names or IP addresses
- 🔢 Single port scanning (`-s` mode)
- 📊 Port range scanning (`-r` mode)
- 🛰️ Basic banner grabbing (when available)
- ⚡ Lightweight and built using Python standard libraries only

---

## 🚀 How it works

This tool works by:
1. Taking a target input (IP or domain)
2. Converting domain names into IP addresses (DNS resolution)
3. Scanning ports using TCP socket connections
4. Detecting open or closed ports
5. Attempting to retrieve service banners from open ports

---

## 🧪 How to Run

Run the script using Python:

```bash
python scanner.py
