# -*-coding:cp949 -*-
"""
>>> w = 'hello world'
>>> w[w.index('h')+1]
'e'
>>> w[6]
'w'
"""

str_default = 'i want to lol now'

"""
>>> print str_default[-1]
w
>>> print str_default[0:2]
i 
>>> print str_default[2:5]
wan
>>> print str_default[2:6]
want
>>> print str_default[7:9]
to
>>> print str_default[10:13]
lol
"""

"""
>>> print str_default.replace('i', 'I')  �õ带 ã�Ƽ� ���� �ٲ��ش�
I want to lol now
"""

#1. ���ڿ��� �Է¹޾� 'h'�� �빮�� 'H'�� �ٲ� ����ϱ�
input_str = 'we are hacker of i2sec academy'

def trans():
    result=input_str.replace('h', 'H')
    print result

trans()   #1�� ������ ��


#2. ���ڿ��� �Է� �޾� ù��° ����(�����̽�) �������� ����ϱ�
s = "Hello World"

#�ε����� ���ڰ� �����̸� ��
for result2 in range(s.index('d')):
    if result2 == s.index(' '):
        print '������ ��ġ�� ',result2,'��° �̸�, ��� �����',s[:result2]        
    else:
        pass

#3. ���� �ϳ��� �Է� �޾� ���� ���ڿ��� 'e'�� �Է� ���� ���ڷ� �ٲ� ���
s = "we are hacker"
c = 'a'

num3 = s.replace('e',c) #num3 = s.replace('e',raw_input())
print num3






