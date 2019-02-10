import sys
from socket import *

host = sys.argv[1]
ports = sys.argv[2].split('-')
start_port = int(ports[0])
end_port = int(ports[1])
#host�� ���� ip�� ��ȯ����.
target_ip = gethostbyname(host)
#���µ� ��Ʈ�� ���� ����Ʈ
opened_ports = []
for port in range(start_port, end_port):
        sock = socket(AF_INET, SOCK_STREAM) #ipv4�� TCP��� sock��ü ������.
        sock.settimeout(3)
        result = sock.connect_ex((target_ip, port))
        if result == 0: #���࿡ ��Ʈ�� ������ return���� 0�� ���´�.
                opened_ports.append(str(port))

print('open port : '+', '.join(opened_ports))
