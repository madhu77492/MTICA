#Indirect inheritance or multilevel inheritance
class A:
    def first_method(self):
        print("Method of class A ...")

class B:
    def first_method(self):
        print("Method of class B ...")

class C(A,B):
    def third_method(self):
        print("Method of class c ...")

if __name__== '__main__' :
    ob=C()
    ob.first_method()
    ob.third_method()
    #C().third_method()
#Circular inheritance is not possible.
        

