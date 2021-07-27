



class MyClass:

    # right click --> rename symbol  equals to Replace all
    def myfunc1(self):
        pass

    # extract variable
    def myfunc2(self, age):
        return (age+10)

    # select code --> right click --> Extract method
    def myfunc3(self):
        print("message1")
        print("message2")
        print("message3")
        print("message4")
        print("message5")
        print("messag6")
        print("message7")
        print("message8")
        print("message9")


class1 = MyClass()
class1.myfunc1()
result = class1.myfunc2(10)
