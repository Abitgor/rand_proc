from libs import *

random_numbers_1 = np.random.uniform(low=0.0, high=1.0, size=(1000000,))
value1 = 1 / 1000000 * np.sum((np.power(random_numbers_1, 7) + np.power(random_numbers_1, 5) + np.power(random_numbers_1, 3)))
print(value1)

random_numbers_2 = np.random.uniform(low=0.0, high=math.pi, size=(1000000,))
value2 = math.pi / 1000000 * np.sum(2 * np.sin(3 * random_numbers_2))
print(value2)

random_numbers_3 = np.random.uniform(low=0.0, high=9999999999999, size=(1000000,))
value3 = 9999999999999 / 1000000 * np.sum(1 / ((random_numbers_3 + 1) * np.power(random_numbers_3, 0.5)))
print(value3)
