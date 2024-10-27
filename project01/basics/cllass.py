class point :
    def __init__(self,x,y):
        self.x =x
        self.y =y
    def move (self):
        print("move")

    def draw(self):
        print("Draw")



point3 =point(12,23)
print(point3.x)