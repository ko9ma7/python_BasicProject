# -*- coding: cp949 -*-

a=[1,2,3,'apple']
b={'aa':'apple', 'bb':'banana','cc':'c#','dd':'dictman'}
'''
1. list type �� ��� �ʰ��� �ߴ� �������ڴ� ����?  ��: IndexError    
    ##print a[8]

    sample_result
    Traceback (most recent call last):
  File "E:/NamKi/python_class/python/ex0726/ex_except2.py", line 9, in <module>
    print a[8]
IndexError: list index out of range

########################################################################
2. list�� �ε��� ��ȣ�� ���ڷ� �޴� �Լ� get_element�� �ۼ��մϴ�.
    - ��ȯ�� ���� list�� ���� ��� ��, ���ڷ� �޴� �ε����� �ִ� ���
    - �ε��� ���� �߻���, �⺻ ������ None ��ȯ
########################################################################    
3. dict Ÿ���� ����� ��, �������� �ʴ� Ű�� �����Ϸ��� �� �� �߻��ϴ� ������
�������� Ȯ���սô�.

Traceback (most recent call last):
  File "E:/NamKi/python_class/python/ex0726/ex_except2.py", line 48, in <module>
    print get_element2(b, 'aaa')
  File "E:/NamKi/python_class/python/ex0726/ex_except2.py", line 41, in get_element2
    dicts[key_name] = key_name
NameError: global name 'dicts' is not defined

########################################################################
4. dict�� Ű�� ���ڷ� �޴� �Լ� get_value�� �ۼ��մϴ�
    - ��ȯ�� ���� dict�� ���� ��� ��, ���ڷ� �޴� Ű�� ��ġ�Ǵ� ��
    - Ű ���� �߻���, �⺻ ������ None ��ȯ

'''


def get_element(listsss ,index_num):
    #comment='Index Error!!!!'    
    try:        
        print listsss[index_num]
    except IndexError:
        return None
    return listsss #list�� ���� ��� ��, ���ڷ� ���� �ε����� �ִ� ��� 

def get_value(dictsss ,key_name):    
    try:        
        dicts[key_name] = ' '
    except NameError:
        return None
    return dicts 

if __name__=="__main__":
    print get_element(a, 2)
    print get_value(b, 'aaa')

'''
���ʽ� ����

import requests
res = requests.get(url)

5. ����ڷκ��� �Է� ���� �� url�� �������� ������ �����ϴ� ���α׷��� �����
    - �������� �ʾ� ������Ʈ�� �����ϸ�, �ٽ� �Է��϶�� �޽����� ����ϰ�, �ٽ� �Է� ����
    - ����� �� url�� �Է� �޾Ұ�, ���� ���忡 �����ϸ�, ���α׷� ����
    
6. ����� ��ġ�Ǿ� ���� �ʾ� ImportError�� �߻��� ��, �ش� ����� ��ġ�� �� ������ ��带 �����ϵ���, ����ó���� �ۼ��غ���

'''
