class Mammal:
    def walk (self):
        print("walk")


class Dog (Mammal):  
    pass


class cat(Mammal):
    pass


dog1 = Dog()
dog1.walk() 