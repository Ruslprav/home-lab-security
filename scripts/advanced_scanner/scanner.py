import socket

class SecurityScanner:
    def __init__(self, target):
        self.target = target

    def check_port(self, port):
        """Проверка конкретного TCP порта."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            return s.connect_ex((self.target, port)) == 0

    def run_audit(self, ports_to_scan):
        results = {}
        for port in ports_to_scan:
            results[port] = "OPEN" if self.check_port(port) else "CLOSED"
        return results
