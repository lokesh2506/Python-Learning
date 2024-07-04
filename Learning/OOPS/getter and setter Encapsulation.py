class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

s=Student()
s.setName("lokesh")

print("My name is :", s.getName())
