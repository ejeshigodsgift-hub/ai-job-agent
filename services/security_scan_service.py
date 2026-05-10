blocked_ips = []


def block_ip(ip):
    blocked_ips.append(ip)


def is_blocked(ip):
    return ip in blocked_ips