import random
secretNumber=str(random.randint(10,99))

chances=7

while chances>0:
    plyGuess=input("Enter the number from 10 - 99 : ")
    if secretNumber==plyGuess:
        print("Congradulation !!! .you won the game.")
        break
    else:
        bull=0
        cow=0
        if secretNumber[0]==plyGuess[0] or secretNumber[1]==plyGuess[1]:
            bull+=1
        if secretNumber[0]==plyGuess[1] or secretNumber[1]==plyGuess[0]:
            cow+=1
        print("Bulls: ",bull," Cows: ",cow)
        chances-=1
        if chances<1:
            print("Sorry :( your chaces ends")
            print("The secret number is ", secretNumber)