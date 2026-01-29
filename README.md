# Port-Scanner

# Python Port Scanner (Educational Project)

This project is a simple TCP port scanner developed in Python using the built-in `socket` library.  
It was created for educational purposes to understand how port scanning works at a low level, without relying on tools like Nmap as a black box.

---

## Features
- TCP port scanning using Python sockets  
- Customizable list of ports  
- Configurable timeout  
- Clear open/closed port identification  
- Lightweight and dependency-free  

---

## What This Project Demonstrates
- Basic network reconnaissance techniques  
- Understanding of TCP connections  
- How port scanners detect open services  
- Foundations of tools used during the recon phase  

---

## Ports Tested
The scanner tests common ports frequently found during real-world pentests, including:

- **FTP**: 21  
- **SSH**: 22  
- **Telnet**: 23  
- **SMTP**: 25, 587  
- **DNS**: 53  
- **HTTP / HTTPS**: 80, 443, 8080, 8443  
- **POP3 / IMAP**: 110, 143, 993, 995  
- **SMB**: 139, 445  
- **Databases**:  
  - MySQL: 3306  
  - PostgreSQL: 5432  
  - MSSQL: 1433  
  - MongoDB: 27017  
- **Remote Access / Management**:  
  - RDP: 3389  
  - VNC: 5900  
- **Other common services**:  
  - 20, 69, 111, 161, 389, 636, 8000, 9000  

You can easily modify the port list inside the script to fit your testing scenario.

---

## Requirements
- Python 3.x  

No external libraries are required.

---

## Usage
Run the scanner with:
```bash
python3 port_scanner.py
