a=int(input("enter the first number"))
b=int(input("eneter the second number"))
print("1.add\n2.sub\n3.multiplication\n4.division")
c=int(input("enter the choice"))
if c==1:
    d=a+b
    print("add value"+" "+str(d))
elif c==2:
    d=a-b
    print("sub value"+" "+str(d))
elif c==3:
    d=a*b
    print(" multiplication value is"+" "+str(d))
else:
    d=a/b
    print("divison value"+" "+str(d))


