def invertedfull_pyaramid(n):
    for i in range(0,n):
        print(" "*i,end="")
        for k in range((n*2)-(i*2)-1):
            print("*",end="")
        print()

invertedfull_pyaramid(int(input("Enter the Number :")))