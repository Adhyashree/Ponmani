a=input("name: ")
s=""
for i in range(len(a)):
    if a[i].isupper():
        z=a[i].lower()
        s+=z
    elif a[i].islower():
        z=a[i].upper()
        s+=z
    else:
        z=a[i]
        s+=z

print(s)
