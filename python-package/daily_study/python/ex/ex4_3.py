# -*- coding: cp949 -*-
##�۾������ ����Ʈ�� �����ϱ� ������,
##�̶� pop���� ó���ϰ� ó���ϰ� ������ �ϴ°� ����
'''
list �� �Լ���
    count �ۤ��� �Ұ�
    append ����Ʈ�� ���� �߰�
    extend ����Ʈ Ȯ���ҋ�
    index
    insert ���� ���� ��ġ ���Ҽ� �ִ�
    pop �� �ڿ� �ִ¾� ������
    sort �������ش�
    reverse �����Ѱ��� �ݴ�� �Ѵ�
    remove(value) �������ش�
    del ����


    sort()
    reverse()
    '''
#####my_list = [1,2,3,4,5]
#####print my_list[:-1]
##
##i2sec_urls = ["www.i2sec.co.kr","seoul.i2sec.co.kr","daegu.i2sec.co.kr",]
###print i2sec_urls[0].index('i2sec')
##i2sec_urls.append(1)
##i2sec_urls.append(10)
##i2sec_urls.append(100)
##
##
###print i2sec_urls.pop(-1)
##
##
##
###i2sec_urls.insert(i2sec_urls.index(100),3)
##i2sec_urls.remove(1)
##i2sec_urls.reverse()
##print i2sec_urls
##
##
##print len(i2sec_urls)
##
##i2sec_urls.sort()
##print i2sec_urls
##
##i2sec_urls.reverse()
##print i2sec_urls

############################################################
a = [1,2,6,7,8,9,10]
#a.append(3,4,5)
a.extend([3,4,5])
a.sort()
print '1�� ��',a
############################################################
well_known_port = [1,7,9,13,17,19,20,21,22,23,24,25]
############################################################
well_known_port.reverse()
print '3�� ��',well_known_port
############################################################
aa = [1,2,3,4, 1,2,3,4, 1,2,3,4]
   #[1,2,3,4, 2,3,4, 2,3,4] �� �����
aa.reverse()
aa.remove(1)
aa.remove(1)
aa.reverse()

print '4�� ��',aa
#reverse -> �۾� -> reverse



#str Ÿ���� ��ξ˾ƿͶ�




