"""영화=["a", "b", "c"]
입장료=[3000,4000,5000]
인원수=[4,2,5]
합=0
for i in range(3):
    합 += 입장료[i]*인원수[i]
    print(i,영화[i],입장료[i]*인원수[i])
# 1부터 10까지 짝수만
for i in range (1,11):
    if i%2 == 0:
        print(i)
#1부터 10까지 홀수만
for i in range(1,11):
    if i%2==1:
        print(i)"""

#구구단 만들기

"""n=1
print(2,"x",n,"=",2*n)"""

for i in range(1,10): #i가 1부터 10까지 출력이니 아래처럼 표현함
    print(2,"x",i,"=",2*i)


"""n = int(input())
for i in range(0,n):
    print(n-i)"""
n = int(input())
while n>0:
    print(n)
    n-=1