from turtle import Turtle

coord = []
for x in range(-300, 300, 50):
    for y in range(0, 300, 30):
        coord.append((x, y))
print(coord)

class Blocks(Turtle):
    def __init__(self, pos, color):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 1)
        self.color(color)
        self.penup()
        self.goto(pos)

    # def delete(self):
    #     self.hideturtle()


