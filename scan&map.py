import socket

def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((ip, port))
            s.shutdown(socket.SHUT_RDWR)
            return True
        except:
            return False

def scan_ports(ip, start=1, end=1024):
    open_ports = []
    for port in range(start, end+1):
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports