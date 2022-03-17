num=int(input("enter the number for addition table:"))
print("addition table of: "+str(num))
for i in range(1,11):
    a=i+num
    print(str(i)+"  + "+str(num)+" = "+str(a))
print("Table completed")