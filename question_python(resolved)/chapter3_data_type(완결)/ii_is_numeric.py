# -*- coding: cp949 -*-


def is_numeric(input_str):
    """ ���ڿ� �ϳ��� ���޹޾Ƽ�, ���ڿ��� ���ڸ� True��, �ƴϸ� False �� ��ȯ�ϴ� �Լ��� �ۼ�����

        sample data: "555"
        expected output: True

        sample data: "a55"
        expected output: False
    """
    #���� �ۼ�
    
    if type(input_str) != type(' '):
        result = 'True'
    else:
        result = 'False'
    return result


if __name__ == "__main__":
    num1 = 555
    num2 = 'a55'
    print('1�� ����(�Է°� : 555) : ',is_numeric(num1))
    print('2�� ����(�Է°� : a55) : ',is_numeric(num2))
    
    pass

