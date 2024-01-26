import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return volume

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return surface_area

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2)
        if distance <= self.radius:
            return True
        else:
            return False


sphere1 = Sphere()
print(sphere1.get_radius())
print(sphere1.get_center())
print(sphere1.get_volume())
print(sphere1.get_surface_area())

sphere1.set_radius(2)
sphere1.set_center(1, 2, 3)

print(sphere1.get_radius())
print(sphere1.get_center())

print(sphere1.is_point_inside(1, 2, 5))
print(sphere1.is_point_inside(5, 5, 5))