from libs import *

random_numbers = np.random.normal(0, 1, 1000000)
beta = np.zeros(1000000)
for i in range(999999):
    if random_numbers[i + 1] - random_numbers[i] > 0:
        beta[i] = 1
data_frame = pd.DataFrame()
data_frame['beta'] = beta
data_frame['beta'].value_counts().plot(kind='bar')
