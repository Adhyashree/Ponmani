def total(a):
    sum=0
    for i in a:
        sum+=i
    print("total mark is:"+str(sum))
name=input("enter the name of the student:")
d=[]
for i in range(0,5):
    a=int(input("enter the marks"))
    d.append(a)    
print("marks:"+str(d))
total(d)
