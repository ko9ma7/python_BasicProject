#pip install netaddr pyping
#��ĵ�� �����Ǵ뿪 : 192.168.25.0 ~ 192.168.25.255
#���� ��� C:\Users\namki\AppData\Local\Programs\Python\Python36\Lib\site-packages
import netaddr, pyping
import threading
#, pyping
iplist = '172.30.1.1/24'
threadLock = threading.Lock()
threads = list()
print('start scan')
def ip_scan(ip):
        try:
                #IP�� ����ִ��� Ȯ������.
                if not pyping.ping(str(ip)).ret_code:
                        threadLock.acquire()
                        print("Alive Host : {}".format(ip))
                        threadLock.release()
        except:
                pass
for ip in netaddr.IPNetwork(iplist):
        th = threading.Thread(target=ip_scan(str(ip)), args=str(ip))
        #ping�� ������ ret_code�� ���� ���� ����(������ 0�̰� ���д� 1)
        threads.append(th)
        th.start()

for x in threads:
        x.join()
                
print("end")
