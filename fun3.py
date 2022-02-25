# function declaratiion
def add(*a):
    sum=0
    for i in a:
        sum+=i
        i+=1
    return sum
# function end 
a=int(input("enter the mark1:"))
b=int(input("enter the mark2:"))
c=int(input("enter the mar3:"))
print(" the total mark is "+str(add(a,b,c)))
# end of the program