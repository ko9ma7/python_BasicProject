# -*- coding: cp949 -*-

#print '\n'*25
#print "��", '��'
#print "1 + 1 =", 1+1
#print���� Print prinT �� ��ҹ��� �����Ѵ�
from datetime import datetime
now = datetime.now()

print '�̸���',
#val = input()  #���ڴ� raw_input()
val=1
print val
print('%s�� %s�� %s�� %s�� %s��'%(now.year, now.month, now.day, now.hour, now.minute))
print "i2sec���� ������ ����ֳ���?"
print "���ǽǿ� ���ڶ� ����", '�л� �� ��ŭ', '��ġ �Ǿ� ������', '���ڴ�'

#������ Ÿ�� �˾ƺ��� type()
#����,���ڸ� 16������ �ٲ܋� print hex(6511) / print bin(54444)

#print ord('h'),ord('e'),ord('l'),ord('l'),ord('o'),ord(' '),ord('w'),ord('o'),ord('r'),ord('l'),ord('d')
print chr(104),chr(101),chr(108),chr(108),chr(111),chr(32),chr(119),chr(111),chr(114),chr(108),chr(100)

#���ڸ� �ƽ�Ű�ڵ�� �˱� ���ؼ� print ord("a") �� ascll�ڵ带 ����
