def halfpyramid(num):
    for i in range(1,num+1):
        value=1
        for j in range(0,i):
            print(value,end=" ")
            value+=1
        print()
halfpyramid(5)