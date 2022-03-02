#This program regards converting lower to upper,upper to lower case letter in a single string
a=input("enter the string: ")
b=""
for i in range(0,len(a)):
    if a[i].isupper():
        b+=a[i].lower()
    elif a[i].islower():
        b+=a[i].upper()
    else:
        b+=a[i]
print(b)

