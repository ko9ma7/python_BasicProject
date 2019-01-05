# -*- coding: cp949 -*-
import time, random
#ù ��° �迭�� ���� -> D F Y M J T U Q K Z
#(��, ���� �빮��)
#1���� �迭�� ù ��° �ε����� [0]=D�� ��  1���� �迭�� ������ ����صд�.  (1)(2)
#�ش� ������ �迭���� �� ��° �ε��� [1]=F�� ��  ��ġ�ϴ� ������ ����ص���.
#�ش� ������ �迭���� �� ��° �ε��� [2]=Y�϶� ��ġ�ϴ� ������ ����ص���.
def rendom_str(): #ó�� �񱳸� �ϱ� ���� �������� ����� �������(10���� ��̸� ����)
    res= '' #����� ���ڿ�
    for x in range(10): #�� �� �ݺ�
        ran=random.randrange(65,90+1) #65~90 index���
        res+=chr(ran) #�ش� �ε����� �ش��ϴ� ascii ���� ��ȯ
    return list(res) #10�� ��̸� �迭�� ����
'''
���� ����Ʈ ���
1) ������ ����Ʈ(���)
2) ������ ����Ʈ�� ���ؼ� ��ġ�ϴ� ����Ʈ(���)���� �ε����� ��� ����Ʈ(��Ī�� ����Ʈ)
3) ������ ����Ʈ�� ���� ������ ����Ʈ��(�̹� ��� ��Ī�� ����� ����Ʈ)
4) ���ϰ� �� ���� ��ġ�ϴ��� ����� ����Ʈ
*2�� 4���� { dict } �� ��Ƶ���.
'''
def manage_overlap(list_data):
    w_count = {}
    #lists = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 31, 31, 31, 32, 33, 33, 33, 33, 34, 34, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 40, 40, 40, 41, 41, 41, 42, 42, 42, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 45, 45, 46, 46, 46, 46, 47, 47, 47, 47, 48, 48, 48, 49, 49, 49, 50, 50, 50, 51, 51, 51, 51, 51, 51, 52, 52, 52, 53, 53, 53, 54, 54, 54, 54, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 57, 57, 57, 58, 58, 58, 59, 59, 59, 59, 60, 60, 60, 61, 61, 61, 61, 62, 62, 62, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 65, 65, 65, 66, 66, 66, 66, 67, 67, 67, 67, 67, 68, 68, 68, 68, 69, 69, 69, 70, 70, 70, 71, 71, 71, 71, 71, 72, 72, 72, 72, 73, 73, 73, 73, 74, 74, 74, 74, 75, 75, 75, 75, 75, 76, 76, 77, 77, 77, 77, 78, 78, 78, 78, 78, 79, 79, 79, 79, 80, 80, 81, 81, 81, 81, 82, 82, 82, 83, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 87, 87, 88, 88, 88, 88, 89, 89, 89, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 94, 94, 94, 94, 95, 95, 95, 95, 96, 96, 96, 97, 97, 97, 97, 98, 98, 98, 98, 99]
    for lst in list_data: #����Ʈ ������ �ݺ��ϱ�
        #��ȯ�� dict Ÿ���� �ε����� ����.(ù ��° : �ߺ�����, �� ��°, )
        try: w_count[lst] += 1  
        except: w_count[lst]=1 
    print(w_count)
    return w_count #��ųʸ� ����
#�ش� ������ �迭���� �� ��° �ε��� [9]=Z�� ��  ��ġ�ϴ� ������ ����ص���.


def get_file_lines():
    data=''
    with open("C:/Users/namki/Desktop/python_BasicProject/algorithm/bridview_test/�����_500x10.txt", "r") as f:
        data=f.read()
    return data

def res_num_compare(data):
    res={}
    for x in data: #��ųʸ� �����͸� �ݺ� ���
        #value���� ���ؼ� 10����~1���� �����Ͱ� �ִ��� ��
        for y in range(10,0,-1): 
            if data[x] == y: #value�� (10~7)�� ��ġȮ��
                #print(y) #��ġ�ϴ� ���� Ȯ��  #print(x)#��ġ�ϴ� ������ �ش��ϴ� key�� ���
                #print("key : {}, value: {}".format(x, y))
                res[x]=y
                #time.sleep(0.1)
            else: #��ġ���� ����
                pass
    return res
def high_match_index(datas):
    num_index=1
    while(True):
        if datas[0] == datas[num_index]:
            num_index += 1  #�������� ������ ���ֱ� ������ ��� +1
        else:  #���� ������ num_index��ȯ
            print("high_match_index�Լ����� ��ȯ�� �ְ� ��Ī��: {} ��".format(num_index))
            return num_index
    
def result_formating(datas):
    #num_index���� ���� ��Ī�� ��������ְ� �� ������ �˷��� 
    result = list()
    datas=sorted(datas, key=lambda k : datas[k], reverse=True) #value�� �������� ������ȭ
    num_index = high_match_index(datas) #������ ��Ī�ο�
    #join���� ��µ����� ���̿� '-'�� ������ ���� �̸� �迭�� �����ص���.
    #num_index���� ��ŭ �������
    compare = 0
    for only_key in datas: #�̸� ���ĵ� dict�� �ϳ��� ����
        result.append(only_key)
        if compare == num_index: #�� ���ǹ��� �� �ְ�� ��Ī�� ���(key)��ŭ ����ϱ� ���ؼ� ����
            return result#��Ī���� �ʴ� ����� ������ �ȴ�
        else: 
            compare += 1 #�������� ó������ ������ ���ϰ��� 1�����̴� 2���� �̱� ���� 0���� ��
    pass 
    '''
    ���� ��ġ�ϴ� ����� 2�� ���
    ���� 3���̻��̸� ��� ���
    [���] value�� �ش��ϴ� key�� ��ȯ (formatting��)
    3���̻� ��ġ�ϳ�?--��ġ�ϴµ� �ش��ϴ� data(dict Ÿ��)�� ���� �迭
    '''
if __name__=="__main__":
    play_cnt = 0#�÷��� ī��Ʈ
    try: #�߸��� input���� ����ó��
        coin = input("input : ")
    except:
        coin = 1
        print("�߸��� �Է����� ������ ���� '1' �� �ԷµǾ����ϴ�.")        
    coin = int(coin)
    while(play_cnt < coin):  #�Էµ� ������ ��ŭ �ݺ�
        play_cnt+=1
        print("coin : {} play_cnt: {}".format(coin, play_cnt))
        data=rendom_str() #['Z', 'C', 'Y', 'A', 'F', 'X', 'U', 'Q', 'K', 'G']
        print("���� : {}".format(data))
        pass_person=list()
        with open("C:/Users/namki/Desktop/python_BasicProject/algorithm/bridview_test/�����_500x10.txt", "r") as f:
            res = f.readlines()
            for x in range(len(res)): #���Ͽ��� ������ row �� ��ŭ �ݺ��ؼ� ��
                for y in data:
                    if y in res[x]:
                       print("����� true   ��� �ε��� {} ({})   ��ġ ���� : {}".format(x, res[x], y))
                       pass_person.append(x)#�ε����� ����
                    else:
                        pass
            true_ing_list =manage_overlap(pass_person)#true�� ��ȯ�� ����Ʈ ����
            res_dict = res_num_compare(true_ing_list) #true�߿� ���� �����͸� ���ڷ� �־ ��ųʸ� ���ϰ�(�ߺ������Ϳ� : �ߺ�����)
            matched = result_formating(res_dict) #���� ��Ī�� �� �� ����� �迭�� ��µȴ�.
            #print("matched ����غ���")
            #print(matched)
            #print(type(matched))
            print('-'.join(str(v) for v in matched))
        
            
                   
'''
    list_standard=list()
    list_already_usage=list()
    dict_result = dict()
    
        res_data = f.readline() #ù ��° ���ػ��
        res_datas=f.readlines() #�� ��° ���� ����� ����Ʈ
        list_standard = res_data.split()
        print(res_datas)
        for l_stand in f.readlines(): #�񱳵� ��� �����
            print(l_stand)
            time.sleep(0.2)
            for t_num in range(len(res_data.split())): #�� ����� ��� ������ŭ �ݺ�
                print(res_data.split()[t_num]) #�� ����� ���� ��̸� �迭�� ����� -> ���ع迭�� �ֱ�
                #�� ����(������° ������ �ε����� ������ ����Ʈ�� �ε���)
                
                #if res_data.split()[t_num] == l_stand[t_num]
        
        #for x in  f.readlines():
         #   time.sleep(0.2)
         #   print(x)
'''         
        
'''
    res[0]==res[1]
    res[0]==res[2]
    res[0]==res[3]
    res[0]==res[4]
    res[0]==res[5]
    0��°���� ���� ���� ���� ���´�?
    -> res[1]==res[1]
    -> res[1]==res[2]
    -> res[1]==res[3]
    -> res[1]==res[4]
    -> res[1]==res[5]
    1��°���� ���� ���� ���� ���´�?
    ---> res[2]==res[1]
    ---> res[2]==res[2]
    ---> res[2]==res[3]
    ---> res[2]==res[4]
    ---> res[2]==res[5]
    2��°���� ���� ���� ���� ���´�?
    -----> res[3]==res[1]
    -----> res[3]==res[2]
    -----> res[3]==res[3]
    -----> res[3]==res[4]
    -----> res[3]==res[5]
    '''        

