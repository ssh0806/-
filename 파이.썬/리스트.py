a=[1,2,3,4]
b=[3,4,5,6]
for i in range(4):
    a[i]+=b[i]
print(a)
#자주 사용되는 함수
a=[1,2,3,4]

#추가 append(추가 값)
a.append(100)
print(a)

#삭제 pop(삭제할 수)
a.pop(0) #0번째 수 삭제
print(a)

#개수,합,가장 큰수, 가장 작은수
개수=len(a)
합=sum(a)
큰수=max(a)
작은수=min(a)
print(개수,합,큰수,작은수)

#정렬(오름차순)
b=[1,6,2,4,7]
b.sort()
print(b)

#뒤집기

b.reverse()
print(b)


