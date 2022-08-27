a=bool(0)

b=bool(1)

c=bool(10>4)
print(a,b,c)

#더 큰 값을 출력하기
a=100
b=20
if a>b:
   print(a)
else:  # 위에 값이 거짓일때 
    print(b)

a=["a","c","e"]

if "c" in a:
    print("있다")
else:
    print("없다")
num=int(input())
print(num%2)
if num%2==0:
    print("짝수")
else:
    print("홀수")

    
print(num%3)
if num%3==0:
    print("3의 배수")
else:
    print("3의 배수가 아님")


