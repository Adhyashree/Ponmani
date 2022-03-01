num=int(input("Enter the number: "))
sum=1
if num!=0 and num>0:
    for i in range(1,num+1):
        sum*=i
    print("The factorial of "+str(num)+" is "+ str(sum))   
elif num==0:
    print("The factorial  of 0 is 1") 
else:
    print("Enter valid number")
