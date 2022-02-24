mark=int(input("Enter your mark: "))
if mark<=100:
    if mark<=100 and mark>=90:
        print("first class")
    elif mark<=89 and mark>=50:
        print("second class")
    elif mark<=49 and mark>=35:
        print("third class")
    else:
        print("You are fail")
else:
    print("Your mark is out of range:")