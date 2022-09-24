from binascii import a2b_base64


a=int(input())
b=int(input())
print(len(a),len(b))
if len(a)>len(b):
    print(a)
else:
    print(b)
