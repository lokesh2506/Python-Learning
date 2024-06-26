def invertedfull_pyaramid(n):
    for i in range(0,n):
        print(" "*i,end="")
        for k in range((n*2)-(i*2)-1):
            if i==0 or i==n-1 or k==0 or k==(n*2)-(i*2)-2:
                print("*",end="")
            else:
                print("",end=" ")
        print()

invertedfull_pyaramid(int(input("Enter the Number :")))