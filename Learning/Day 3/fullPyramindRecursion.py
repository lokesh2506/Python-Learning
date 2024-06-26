def print_space(spaceNumber):
    if spaceNumber>0:
        print(" ",end="")
        print_space(spaceNumber-1)

def print_star(starNum):
    if starNum>0:
        print("* ",end="")
        print_star(starNum-1)


def full_pyramid_recursion(num,value):
    if num>0:

        print_space(num-1)
        print_star(value)
        print()
        full_pyramid_recursion(num-1,value+1)
value=1
num=int(input("Enter the Number : "))
full_pyramid_recursion(num,value)