"""def 짝수 (a):
    새로운리스트=[]
    for i in a:
        if i%2==0:
            print(i)
            새로운리스트.append(i)  
    return 새로운리스트
짝수([1,2,3,4,5,6,])"""
 

def 옷사이즈(a):
    새로운리스트=[]
    s = 0
    e=0
    r=0
    q=0
    t=0
    for i in a:
        if i == "s":
            s+=1
        if i =="m":
            e+=1
        if i =="L":
            r+=1
        if i=="XS":
            q+=1
        if i=="XL":
            t+=1
    print(s,e,r,q,t)
    새로운리스트.extend([s,e,r,q,t])
    return 새로운리스트

        


a = 옷사이즈(["s","m","L","XL","XS","s","m","XS"])
print(a)