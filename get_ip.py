import socket

def get_ip_address():
    try:
        # Connect to an external server to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        # This IP and port are arbitrary; we're not making a real connection
        s.connect(('8.8.8.8', 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return f"Unable to get IP address: {e}"

if __name__ == "__main__":
    ip = get_ip_address()
    print(f"My IP address is: {ip}")

    #350dc44365914a27b85fc19a5241e3c4
