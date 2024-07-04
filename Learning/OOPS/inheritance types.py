# single inheritance

class Parent:
    def display(self):
        print("Parent method")
class Child (Parent):
    def display1(self):
        print("child Method")

c=Child()
c.display()
c.display1()

# mutlilevel inheritance
class Parent1:
    def display(self):
        print("Parent method")
class Child1 (Parent):
    def display1(self):
        print("child1 Method")

class Child2 (Child1):
    def display2(self):
        print("child2 Method")

c=Child2()
c.display()
c.display1()
c.display2()



# hybrid inheritance

class Parent1:
    def display(self):
        print("Parent method")
class Child1 (Parent):
    def display1(self):
        print("child1 Method")

class Child2 (Parent):
    def display2(self):
        print("child2 Method")

c=Child1()
c.display()
c.display1()

c1=Child2()
c1.display()
c1.display2()

# multiple inheritance

class Parents1:
    def display(self):
        print("Parents1 method")
class Parents2:
    def display1(self):
        print("Parents2 Method")

class Child21 (Parents1,Parents2):
    def display2(self):
        print("child2 Method")

ch=Child21()
ch.display2()
ch.display()
ch.display1()

# super keyword

class College:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display1(self):
        print("My name is : ",self.name)
        print("My rollno is : ",self.rollno)


class Dept(College):

    def __init__(self,name,rollno,dept,mark):
        super().__init__(name,rollno)
        self.dept=dept
        self.mark=mark

    def display(self):
        super().display1()
        print("My dept is :",self.dept)
        print("My mark is : ",self.mark)

d=Dept("lokesh",20,"cce",90)
d.display()


# operator overloading
class Book:
     def __init__(self,pages):
         self.pages=pages

     def __add__(self,others):
         return self.pages+others.pages
b=Book(100)
b1=Book(200)

print(b+b1)