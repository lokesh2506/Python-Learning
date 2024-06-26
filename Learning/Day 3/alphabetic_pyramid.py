def alphabetic_pyaramid(n,alph):
    for i in range(0,n):
        print(" "*(n-i),end="")
        for k in range(0,i+1):
            print(chr(alph),end=" ")
            alph+=1
        print()
alph=65
alphabetic_pyaramid(int(input("Enter the Number :")),alph)

def alphabetic_pyaramid(n):
    for i in range(0,n):
        alph=65
        print(" "*(n-i),end="")
        for k in range(0,i+1):
            print(chr(alph),end=" ")
            alph+=1
        print()

alphabetic_pyaramid(int(input("Enter the Number :")))