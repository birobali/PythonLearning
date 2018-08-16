class Line:
    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) ** (1.0 / 2)

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)


x = (3, 2)
y = (8, 10)
line = Line(x, y)
print(line.distance())
print(line.slope())
