a=int(input("Enter the value of 1st num : "))
b=int(input("Enter the value of 2st num : "))
c=int(input("Enter the value of 3st num : "))

if a<c and b<c:
    print("c is greater")
elif a<b and c<b:
    print("b is greater")
else:
    print("a is greater")

# ---------------------------------------------------

# nested if

boyName=input("Enter your boy name :")
girlName=input("Enter your Girl nmae : ")
if(boyName):
    if(girlName=="hari"):
        print(boyName)