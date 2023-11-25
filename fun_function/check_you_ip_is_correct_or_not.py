import ipaddress

def check_ip_is_correct_or_not(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
    
if __name__ == '__main__':
    ip = input('Enter IP: ')
    print(check_ip_is_correct_or_not(ip))
    