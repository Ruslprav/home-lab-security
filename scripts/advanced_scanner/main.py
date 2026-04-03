import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from scanner import SecurityScanner
from utils import get_system_info

def main():
    print("--- Advanced Security Audit Tool ---")
    
    # 1. Инфо о системе
    sys_info = get_system_info()
    print(f"[SYSTEM] OS: {sys_info['os']} | User: {sys_info['user']}")
    
    # 2. Сканирование
    target = "127.0.0.1"
    scanner = SecurityScanner(target)
    critical_ports = [22, 80, 443, 3389]
    
    print(f"[SCAN] Starting scan for {target}...")
    report = scanner.run_audit(critical_ports)
    
    for port, status in report.items():
        print(f" Port {port}: {status}")

if __name__ == "__main__":
    main()
