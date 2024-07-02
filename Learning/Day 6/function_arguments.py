def add(a,b):
    return a+b

print(add(1,2))

def add(*n):
    total=0
    for i in n:
        total+=i
    print(total)

add(1,2,3,4,5,6,7,8,9,10)
