# -*- coding: cp949 -*-
import requests as re
from bs4 import BeautifulSoup as bs
import os,time

#Ŭ����� ����Ʈ ��ǰ : https://front.wemakeprice.com/special/5000265
#Ŭ����� ���� ��ǰ : https://front.wemakeprice.com/special/5000254
#���� ������ ��ǰ : https://front.wemakeprice.com/special/5000119
#90%���� : https://front.wemakeprice.com/special/5000257

def crawl_init(url):
    request_headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')
    }
    res = re.get(url , headers=request_headers)
    soup = bs(res.text, "html.parser")
    return soup
def get_product(url):
    product_name=list()
    product_sale=list()
    ago_price=list()
    after_price=list()
    soup = crawl_init(url)
    for x in soup.findAll("p",{"class":"text"}): #��ǰ �� 
       product_name.append(x.text)
    for x in soup.findAll("span",{"class":"num"}): #���� �� ���� ����
       ago_price.append(x.text)
    for x in soup.findAll("span",{"class":"sale"}): #���� ��
       product_sale.append(x.text)
    for x in soup.findAll("em",{"class":"num"}): #���ε� ���� ���Ű���
       after_price.append(x.text)
    return [product_name, product_sale, ago_price, after_price]

if __name__=="__main__":
    clear_best="https://front.wemakeprice.com/special/5000265"
    clear_today="https://front.wemakeprice.com/special/5000254"
    super_today="https://front.wemakeprice.com/special/5000119"
    discount_ninety="https://front.wemakeprice.com/special/5000257"
    tag_name=""
    
    for url in [clear_best, clear_today, super_today, discount_ninety]:  
        try:
            print(url)
            v_data=get_product(url)
            if url == clear_best: #tag name
                tag_name="����Ʈ ��ǰ"
            elif url == clear_today: #tag name
                tag_name="������ ��ǰ"
            elif url == super_today: #tag name
                tag_name="����������"
            elif url == discount_ninety: #tag name
                tag_name="90%������"
            print("#### {} ####".format(tag_name))
            for x in range(len(v_data[0])):
                print("{} : ������({}) ���� : {}�� --> {}��".format(v_data[0][x], v_data[1][x], v_data[2][x], v_data[3][x]))
                with open("��������������.txt","a") as f:
                    f.write("#### {} ####".format(tag_name))
                    f.write("{} : ������({}) ���� : {}�� --> {}��".format(v_data[0][x], v_data[1][x], v_data[2][x], v_data[3][x]))
                    f.write("\n")
        except IndexError as s:
            #print(s)
            pass
            

