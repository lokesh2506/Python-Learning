class Students:
# instance methods have self in the arguments
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print("Hi ",self.name)
        print("Your mark is ",self.mark)

    def Grade(self):
        if self.mark>=80 and self.mark<=100:
            print("Excelent")
        elif self.mark>=60 and self.mark<80:
            print("good")
        elif self.mark>=40 and self.mark<60:
            print("Fair")
        else:
            print("Fail")

n=int(input("Enter the number of students : "))

for i in range(n):
    name=input("Enter u r name : ")
    mark=int(input("Enter your mark : "))
    s = Students(name,mark)
    s.display()
    s.Grade()

