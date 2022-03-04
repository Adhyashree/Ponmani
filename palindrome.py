name=input("Enter  the name: ")
name_1=name.lower()
rev=name_1[::-1]
if name_1==rev:
    print("Given string is palindrome")
else:
    print("Given string is not a palindrome")