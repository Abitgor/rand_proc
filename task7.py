from libs import *


class Circle:
    def __init__(self, radius, x, y, z):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def exist_in_circle(self, x1, y1, z1):
        if (self.x - x1) * (self.x - x1) + (self.y - y1) * (self.y - y1) + (self.z - z1) * (
                self.z - z1) < self.radius * self.radius:
            return True
        else:
            return False


print('Amount of circles:')
number_circles = int(input())
circles_list = []
xs = []
ys = []
zs = []
rs = []

for i in range(1, number_circles + 1):
    print(i, ' circle')
    print('x: ')
    x_center = float(input())
    xs.append(x_center)
    print('y: ')
    y_center = float(input())
    ys.append(y_center)
    print('z: ')
    z_center = float(input())
    zs.append(z_center)
    print('radius: ')
    r = float(input())
    rs.append(r)
    c = Circle(r, x_center, y_center, z_center)
    circles_list.append(c)

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
z = np.linspace(0, 1, 100)
xx, yy, zz = np.meshgrid(x, y, z)


def in_area(point):
    for circle in circles_list:
        if not circle.exist_in_circle(*point):
            return False
    return True


c = []
for x, y, z in zip(np.ravel(xx), np.ravel(yy), np.ravel(zz)):
    is_in_area = in_area((x, y, z))
    c.append(is_in_area)

area = sum(c) / len(c)
print(area)
