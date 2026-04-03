import re
from collections import Counter

# Эмуляция данных из системного лога /var/log/auth.log
log_samples = [
    "Jan 21 10:05:01 server sshd: Failed password for invalid user admin from 192.168.1.100 port 54321 ssh2",
    "Jan 21 10:05:05 server sshd: Failed password for invalid user admin from 192.168.1.100 port 54322 ssh2",
    "Jan 21 10:05:10 server sshd: Failed password for invalid user admin from 192.168.1.100 port 54323 ssh2",
    "Jan 21 10:06:01 server sshd: Accepted password for user root from 192.168.1.5"
]

def detect_bruteforce(logs, threshold=3):
    """Функция поиска IP-адресов с подозрительно частыми отказами в доступе."""
    failed_attempts = []
    
    for line in logs:
        # Регулярное выражение для поиска IP после слова 'from'
        ip_match = re.search(r'Failed password .* from ([\d\.]+)', line)
        if ip_match:
            failed_attempts.append(ip_match.group(1))
            
    # Подсчет попыток для каждого IP
    ip_counts = Counter(failed_attempts)
    
    print("--- Security Analysis Report ---")
    for ip, count in ip_counts.items():
        if count >= threshold:
            print(f"[ALERT] Potential Brute-force attack detected from IP: {ip}")
            print(f"[INFO] Total failed attempts: {count}")
        else:
            print(f"[OK] No critical issues for IP: {ip}")

if __name__ == "__main__":
    detect_bruteforce(log_samples)
