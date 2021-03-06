# -*- coding: utf-8 -*-


""" 정수 두개를 가진 튜플들을 가진 리스트를 전달받아,
두 수의 차가 가장 작은 튜플을 반환하는 함수 get_min를 작성하자
    
    sample in/out:
        get_min([(1,2), (3,5), (100, 10)]) -> (1, 2)
        get_min([(1,10), (3,5), (100, 10)]) -> (3, 5)
"""
def get_min(tu):
##      <시나리오>
##    tu[0][0] tu[0][1]
##    tu[1][0] tu[1][1]
##    tu[2][0] tu[2][1]
##    tu[3][0] tu[3][1]
##    tu[4][0] tu[4][1]  
    
    '''
    매개변수 tu는 튜플안에 리스트의 한종류
        tu[0] 을 출력하면 (1, 2)로 튜플이 출력.
        tu[0][0] 을 출력하면 (1)로 문자혹은 숫자가 출력.
    '''
    tmp = tu[0][0]-tu[0][1]
    x=0
    y=0
    for i in tu:                
        if abs(i[0]-i[1]) <= abs(tmp):
            tmp=i[0]-i[1]            
            x=i[0]
            y=i[1]
        else:
            ""
    result=(x,y)
    return result

if __name__ == "__main__":
    print(get_min([(1,2), (3,5), (100, 10), (3,4), (4,5)]))# -> (1, 2)
    print(get_min([(1,10), (3,5), (100, 10), (1,2)]))# -> (3, 5)
    pass


