num=int(input("enter the number"))
sum=0
b=num
while b>0:
    c=b%10
    sum+=c*c*c
    b//=10
if num==sum:
    print("amstrong")
else:
    print("not amstrong")