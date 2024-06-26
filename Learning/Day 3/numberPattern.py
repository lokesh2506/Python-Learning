def number_pattern(num):
    for i in range(1,num+1):
        value=1
        print(" "*(num-i),end="")
        for j in range(0,(i*2)-1):
            print(value,end="")
            value+=1
        print()

number_pattern(int(input("enter the value : ")))