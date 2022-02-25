def odd(a):
    print(str(a)+" "+ "is odd number")
def even(a):
    print(str(a)+" "+"is even number")
name=int(input("enter the number"))
if name%2==0:
    even(name)
else:
    odd(name)