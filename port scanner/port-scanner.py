import socket
import threading

# Function to scan a single port
def scan_port(target, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set timeout for connection
        result = s.connect_ex((target, port))  # Attempt to connect
        
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Function to scan a range of ports
def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    
    threads = []  # List to store threads
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# User input
target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# Run the port scanner
scan_ports(target, start_port, end_port)

