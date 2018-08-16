from cmath import pi


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return pi * (self.radius **2) * self.height

    def surface_area(self):
        return 2 * pi * self.radius * (self.radius + self.height)


cylinder = Cylinder(2, 3)
print(cylinder.volume())
print(cylinder.surface_area())
