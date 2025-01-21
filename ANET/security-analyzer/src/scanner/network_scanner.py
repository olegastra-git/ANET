import socket

def scan_network(ip_range):
    active_hosts = []
    for ip in ip_range:
        try:
            socket.gethostbyaddr(ip)
            active_hosts.append(ip)
        except socket.herror:
            continue
    return active_hosts

if __name__ == "__main__":
    # Пример использования
    ip_range = ["192.168.1." + str(i) for i in range(1, 255)]
    active_hosts = scan_network(ip_range)
    print("Активные хосты в сети:", active_hosts)