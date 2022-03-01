count=int(input("enter the total number of subjects"))
print(" Enter the marks")
a=[]
sum=0
for i in range(0,count):
    c=int(input())
    a.append(c)
print(a)
for i in a:
    sum+=i
print("The total mark is "+str(sum))
avg=sum/count
print("the average mark is "+str(avg))
