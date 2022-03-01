a=int(input("Enter the number of count:  "))
name=[]
for i in range(0,a):
   string=input()
   name.append(string)
print(name)
#print("\t"+name[0].title())
for i in range(0,len(name)):
   if i==0:
      c=name[i].title()
      print("\t"+c)
   elif i%2==0:
      c=name[i].upper()
      print(c)
   else:
      c=name[i].lower()
      print(c)
