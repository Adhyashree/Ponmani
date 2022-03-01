a=int(input("Enter the starting number for prime"))
b=int(input("Enter the ending number for prime"))
for num in range (a,b+1):
    if num>1:
        for i in range(2, num):
            if num%i==0:
                break
        else:
            print(num)
    else:
        print("enter correct value")



