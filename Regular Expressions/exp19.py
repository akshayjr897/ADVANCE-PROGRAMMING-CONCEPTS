# check IPv4 and IPv6 Pattern 

import re

def validate_ip(ip):

    # IPv4 pattern
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    
    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')

        
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False

        return True

    # IPv6 pattern
    ipv6_pattern = r'^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$'

    if re.match(ipv6_pattern, ip):
        return True

    return False


ip = input("Enter an IP address: ").strip()


if validate_ip(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")