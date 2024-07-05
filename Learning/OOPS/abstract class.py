from abc import *
'''class Test:
    @abstractmethod
    def onlineexamPattern(self):
        pass
class Day1(Test):
    def onlineexamPattern(self):
        return "Pass"

d=Day1()
print(d.onlineexamPattern()) '''

class Test(ABC):  #abstract class
    @abstractmethod
    def onlineexamPattern(self):
        pass
class Day1(Test):

    # once the abstarct class is inherited means we need define the body of the abstarct method
    def onlineexamPattern(self):
        return "Pass"

d=Day1()
print(d.onlineexamPattern())


# the abstract class contains only abstarct class means it is know as inheritance