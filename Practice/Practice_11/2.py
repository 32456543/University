import math
class Sphere:
    def __init__(self, radius=1, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4/3) * math.pi * self.radius**2

    def get_square(self):
        return 4 * math.pi * self.radius**2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.center[0])**2 + (y - self.center[1])**2 + (z - self.center[2])**2)
        return distance <= self.radius


s0 = Sphere(0.5) # test sphere creation with radius and default center
print(s0.get_center()) # (0.0, 0.0, 0.0)
print(s0.get_volume()) # 0.523598775598
print(s0.is_point_inside(0 , -1.5, 0)) # False
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0)) # True
print(s0.get_radius()) # 1.6
