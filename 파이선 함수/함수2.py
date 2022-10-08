from re import I, S
from unittest import removeResult


"""return a+b #함수를 사용했을 때 값을 함수 밖으로 내보는 것 , 함수 끝내기
a= func(10,20)
print(a)
list_1=[5,3,1,]"""

def 리스트합(a):
    s=0 
    for i in a:
        s+=i
    return S


def 리스트개수 (a):
    c=0
    for i in a:
        c+=1
    return c




def 평균(a):
    return 리스트합(a)/리스트개수(a) 
a=평균[1,2,3]
print(a)
    
