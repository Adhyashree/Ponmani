num=int(input("enter the number for multiplication table:"))
print("Multiplication table of: "+str(num))
for i in range(1,11):
    a=i*num
    print(str(i)+"  x "+str(num)+" = "+str(a))
print("Table completed")