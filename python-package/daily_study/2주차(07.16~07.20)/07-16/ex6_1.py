#-*- coding:cp949 -*-
network_port = {
    "well_known" : range(0,1024),
    "registed" : range(1024,49152),
    "dynamic" : range(49152,65336),
    }

port = input()
if port in network_port["well_known"]:
    print('well_known')
elif port in network_port["registed"]:
    print('registed')
elif port in network_port["dynamic"]:
    print('dynamic')
else:
    print('not found')


#������ ù ��ġ�� �˾Ƴ���(������ -1 ��ȯ���ش�)
#��, index�� ������ ����Ű�� ���α׷� ����ȵǴ� find���
