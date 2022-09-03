"""#range=어떤 수의 범위
#기본 식
a=list(range(5))
print(a)

b=list(range(1,5)) #1부터 5까지 출력
print(b)

c=list(range(1,10,2)) # 1부터10까지 2씩 커진수
print(c)

for i in c:
    print(i)

#7부터 15까지 순서대로 출력
for i in range(7,16):
    print(i)
#2 4 6 8 10 12 출력
for i in range(2,13,2):
    print(i)"""

#while(뒤에 값이 참이면 계속 출력한다) 기본꼴
a=0        #a를 변수 0으로 정하기
while a<10:    #a 값이 10보다 작으면
    print(a)  #a값 출력
    a=a+1   #a 값에 1씩 더하기
 
while True:   
    print(a)  
    a=a+1 
    if a>10:
        break 
#복합대입
a=10
a+= 10 # 자기 자신에 10을 더하라

 


