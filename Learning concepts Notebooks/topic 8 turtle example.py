import turtle

class Fran(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(2)
        #self.penup()
        self.goto(0, 0)

    def square (self):
        for _ in range(4):
            self.forward(100)
            self.left(90)
    
    def triangle (self):
        self.forward(100)
        self.left(120)
        self.forward(100)
        self.left(120)
        self.forward(100)#
    def sq2(self):
        for k in range(100):
            for j in range(4):
                self.forward(100)
                self.left(90)
            self.left(5)


a = Fran()
a.square()
a.triangle()
a.sq2()