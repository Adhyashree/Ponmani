num=list(map(lambda x:x*x,range(1,11)))
print(num)
n=[x*x for x in range(1,12)]
print(n)
print("*************************")
temp=[12,23,41,56,13,19]
temp_1=[i  for i in temp if i<30]
print(temp_1)
temp_2=[i if i<30 else 0 for i in temp]
print(temp_2)
fruits=["apple","orangie","kiwi"]
new=[i for i in fruits if 'i' in i]
print(new)