# Python Port Scanner

This is a simple multithreaded Python port scanner that scans a target IP or domain for open ports within a specified range.

## Features
- Scans a given range of ports.
- Uses threading for faster execution.
- Displays open ports in real-time.

## Prerequisites
- Python 3.x installed on your system.

## Installation
1. Clone this repository or download the script.
2. Ensure Python is installed by running:
   ```bash
   python --version
   ```
3. No additional libraries are required as it only uses built-in Python modules (`socket`, `threading`).

## Usage
1. Run the script:
   ```bash
   python port_scanner.py
   ```
2. Enter the target IP or domain and the range of ports to scan.
3. The script will display open ports found within the specified range.

### Example
```bash
Enter target IP or domain: scanme.nmap.org
Enter start port: 20
Enter end port: 100
```
Output example:
```bash
[+] Port 22 is open
[+] Port 80 is open
[+] Port 443 is open
```

## Code Overview
```python
import socket
import threading

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
scan_ports(target, start_port, end_port)
```

## Enhancements (Future Improvements)
- Add service detection (identify if it's HTTP, FTP, SSH, etc.).
- Save scan results to a file.
- Use `argparse` to accept command-line arguments.

## License
This project is open-source and available under the MIT License.

## Author
Developed by Itibi

