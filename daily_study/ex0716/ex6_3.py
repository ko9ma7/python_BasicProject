#-*- coding:cp949-*-
def translate(string):
    

    #��� �����϶� true
    #��� �����϶� true
    #Ư������ ������ true
    result=' '
    if string.isalpha():
        result = "alpha"
        return result
    elif string.isdigit():
        result = "digit"
        return result
    elif string.isalnum():
        result = "alnum"
        return result

    

if __name__=="__main__":
    str_tmp="6400"
    str_tmp2="milk"
    str_tmp3="lol5killor1dead"
    
    #print(translate(str_tmp))
    #print(translate(str_tmp2))
    print(translate(str_tmp3))

