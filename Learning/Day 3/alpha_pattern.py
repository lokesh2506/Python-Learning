def alpha_pattern(num):
    alpha=64
    for i in range(1, num + 1):
        alpha+=1
        for j in range(0, i):
            print(chr(alpha), end=" ")
        print()

alpha_pattern(5)