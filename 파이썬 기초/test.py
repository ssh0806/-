a=[10,20,30]

if 30 in a:
    print(a.index(30))

지갑=[5000,"카드"]
a=지갑
if a[0]>=10000 or "카드" in a:
    print("택시를 탈 수 있다")
else:
    print("대중교통을 이용하기")

    지갑=[5000,"카드"]
a=지갑
if a[0]<=1000 or not "카드" in  a:
    print("걸어가기")
