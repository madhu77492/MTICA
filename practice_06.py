class Wolf:
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print("Crr...")
class Dog(Wolf):
    def bark(self):
        print("Woof")
        

pet1=Dog("Tommy","brown")
pet1.bark()
pet2=Wolf("Loose","White")
pet2.bark()
Dog("abc","xyz").bark()
#Redefining a method of base class in derived class is overriding.
