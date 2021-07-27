
class MyClass:

    # right click --> rename symbol  equals to Replace all
    def myPassFunc(self):
        pass
        
    # extract variable
    def myfunc2(self,age):
        newvariable757 = age+10
        return (newvariable757)

    # select code --> right click --> Extract method
    def myfunc3(self):
        self.newmethod725()
        print("messag6")
        print("message7")
        print("message8")
        print("message9")

    def newmethod725(self):
        print("message1")
        print("message2")
        print("message3")
        print("message4")
        print("message5")


class1 = MyClass()
class1.myPassFunc()
result = class1.myfunc2(10)
