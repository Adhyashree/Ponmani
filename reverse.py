num=int(input("enter the number"))
a=0
while num>0:
    c=num%10
    a=a*10+c
    num=num//10
print(a)