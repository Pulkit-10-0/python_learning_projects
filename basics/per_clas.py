class person:
    def __init__(self,name):
        self.name =name

   
    def talk(self):
        print(f"hi, I am {self.name}")



john = person("john smith")

john.talk()

bob = person("bob")
bob.talk()