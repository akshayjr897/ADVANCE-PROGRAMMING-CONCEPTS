server_ip = ("192.168.1.1",)
allowed_ips = ["192.168.1.2", "192.168.1.3"]

print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

ip = input("Enter new allowed IP: ")
allowed_ips.append(ip)

print("Updated allowed IPs:", allowed_ips)