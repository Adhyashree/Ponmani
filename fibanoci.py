a=int(input("enter the number of count for fibanoci series"))
b=-1
c=1
d=0
for i in range(1,a+1):
    d=b+c
    print(d)
    b=c
    c=d
    