from libs import *
# 2
data_frame_3 = pd.DataFrame()
xi = np.array([13, 16, 28, 33, 39, 47, 52])
pi = np.array([0.08, 0.14, 0.25, 0.16, 0.25, 0.09, 0.03])
data_frame_3['xi'] = xi
data_frame_3['pi'] = pi
display(data_frame_3)

plt.bar(xi, pi)
plt.title("Histogram")
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

mean = np.sum(xi * pi)
mean_square = np.sum((xi ^ 2) * pi)
variance = mean_square - (mean * mean)
print('mean: ', mean)
print('variance: ', variance)
