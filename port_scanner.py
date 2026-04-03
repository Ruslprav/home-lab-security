import socket

# Список критических портов для проверки
# 22 - SSH, 80 - HTTP, 443 - HTTPS, 3389 - RDP
target_ports = [22, 80, 443, 3389]
target_host = "127.0.0.1" # Сканируем себя (локальный хост)

def scan_host(host, ports):
    print(f"--- Scanning Target: {host} ---")
    for port in ports:
        # Создаем сокет для попытки подключения
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Ждем ответ 1 секунду
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"[!] Port {port}: OPEN (Warning: Service detected)")
        else:
            print(f"[-] Port {port}: CLOSED")
        sock.close()

if __name__ == "__main__":
    scan_host(target_host, target_ports)
