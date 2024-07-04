from abc import *
class Test:
    @abstractmethod
    def onlineexamPattern(self):
        pass
class Day1(Test):
    def onlineexamPattern(self):
        return "Pass"

d=Day1()
print(d.onlineexamPattern())
