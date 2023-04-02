import sys
import socket

# Get the IP address from the command-line arguments
ip_address = sys.argv[1]

# Use the socket module to get the hostname of the device
try:
    hostname = socket.gethostbyaddr(ip_address)[0]
except socket.herror:
    hostname = "Unknown"

# Print the hostname to the console
print(f"Hostname for {ip_address}: {hostname}")
