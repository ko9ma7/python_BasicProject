# -*- coding: utf-8 -*-


def xx_age(age):
    """ ���� age�� ���̸� ���� �ް�, 
          60���� ũ��, ����⡱, 
          40~59 ���̸�, ���߳⡱, 
          20~39 ���̸�, ��û�⡱, 
          �� �ܿ��� �����⡱ �̶�� ����غ���.
    """
    # ���� �ۼ�
    if age>60:
        return '���'
    elif 40 <= age <60:
        return '�߳�'
    elif 20 <= age <40:
        return 'û��'
    elif age==60:
        return '60���� ���� ������ ������, ���(��)..."����� �̷��� �ص� �°���?"'
    else:
        return "����"
    


if __name__ == "__main__":
    print xx_age(50)
    print xx_age(20)
    print xx_age(55)
    print xx_age(60)
    print xx_age(10)
    print xx_age(2)
    print xx_age(34)
    pass

