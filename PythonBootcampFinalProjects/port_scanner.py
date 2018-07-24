## Port Scanner
### Networking

##Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections ##mark the port as open.

import socket

ip_address = '127.0.0.1'  # initialize as localhost
port_start = 0
port_end = 65535

net_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = input('Please, provide IP address - in format A.B.C.D: ')
port_start = input('Please, provide starting port to scan: ')
port_end = input('Please, provide ending port for scan: ')

for port in range(port_start, port_end):
    scan_result = net_socket.connect_ex((ip_address, port))

    if (scan_result == 0):
        print('Port {} on machine {} is open.'.format(port, ip_address))
    else:
        print('Port {} on machine {} is closed.'.format(port, ip_address))