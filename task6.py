from libs import *


class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def exist_in_circle(self, x1, y1):
        if (self.x - x1) * (self.x - x1) + (self.y - y1) * (self.y - y1) < self.radius * self.radius:
            return True
        else:
            return False


print('Amount of circles:')
number_circles = int(input())
circles_list = []
xs = []
ys = []
rs = []

for i in range(1, number_circles + 1):
    print(i, ' Circle')
    print('x: ')
    x_center = float(input())
    xs.append(x_center)
    print('y: ')
    y_center = float(input())
    ys.append(y_center)
    print('radius: ')
    r = float(input())
    rs.append(r)
    c = Circle(r, x_center, y_center)
    circles_list.append(c)

fig, ax = plt.subplots()
for circle in circles_list:
    a_circle = plt.Circle((circle.x, circle.y), circle.radius, color='b', linewidth=1, fill=False)
    ax.add_artist(a_circle)
plt.show()

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
xx, yy = np.meshgrid(x, y)


def in_area(point):
    for circle in circles_list:
        if not circle.exist_in_circle(*point):
            return False
    return True


c = []
for x, y in zip(np.ravel(xx), np.ravel(yy)):
    is_in_area = in_area((x, y))
    c.append(is_in_area)

area = sum(c) / len(c)
print(area)

colors = list(map(lambda x: {True: 'b', False: 'w'}[x], c))
plt.scatter(np.ravel(xx), np.ravel(yy), c=colors)
plt.title(f'Area: {area}')
plt.show()
