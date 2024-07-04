class Bank:
    bankName="Axis Bank of India"
    #  static variable
    def __init__(self,name,balance=0.0):
        self.name=name  #instance variable
        self.balance=balance

    def widthraw(self,amt ):# amt is a local variable
        if amt>self.balance:
            print("Insufficient Balance. pls check u r balance and try again")
            exit()
        else:
            self.balance-=amt
            print("Balance in your account : ",self.balance)

    def deposit(self,amt):
        self.balance+=amt
        print("Balance in your account : ", self.balance)


print("Welcome to ",Bank.bankName)
name=input("Enter your Name : ")
b=Bank(name)



while True:
    option=input("Enter the one option give below\nW-Widthraw\nD-Deposit\nE-exit\noption : ")
    if option=='W' or option=='w':
        amt=float(input("Enter amount : "))
        b.widthraw(amt)
    elif option == 'D' or option == 'd':
        amt = float(input("Enter amount : "))
        b.deposit(amt)
    elif option == 'E' or option == 'e':
        exit()
    else:
        print("Pls enter the valid option metioned below")