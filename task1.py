from libs import *

# 1. Згенерувати послідовність з n =1000000 псевдовипадкових чисел, що рівномірно розподілені на інтервалі (0,1)
# (використати вбудований генератор псевдовипадкових чисел). Побудувати графік.
data_range = range(1000)
data = [random.random() for i in data_range]
plt.plot(data_range, data)
plt.show()

# 1.1. Оцінити математичне сподівання та дисперсію отриманої послідовності.
data = [random.random() for i in range(1000000)]
mean = statistics.mean(data)
variance = statistics.variance(data)
print('mean: ', mean)
print('variance: ', variance)

# 1.2. Побудувати таблицю 1 (кількість L підінтервалів не менше 10), частотну таблицю вивести на екран.
intervals = ['0-0.1', '0.1-0.2', '0.2-0.3', '0.3-0.4', '0.4-0.5', '0.5-0.6', '0.6-0.7', '0.7-0.8', '0.8-0.9', '0.9-1']
data_frame_1 = pd.DataFrame()
data_frame_1['Intervals'] = intervals

frequency_in_interval = []
for i in range(10):
    counter = 0
    for j in data:
        if (j > i / 10) & (j < (i + 1) / 10):
            counter += 1
    frequency_in_interval.append(counter)

relative_frequency = [i / 1000000 for i in frequency_in_interval]
data_frame_1['frequency_in_interval'] = frequency_in_interval
data_frame_1['relative_frequency'] = relative_frequency
display(data_frame_1)

# 1.3. Перевірити гіпотезу про закон розподілу, побудувати гістограму
data_frame_2 = pd.DataFrame()
data_frame_2['frequency_in_interval'] = frequency_in_interval
data_frame_2['relative_frequency'] = relative_frequency
chi2, probability, df, expected = sc.stats.chi2_contingency(data_frame_2)
print(probability, 'if value greater than 0.05, then law works')

plt.bar(intervals, relative_frequency)
plt.title("Histogram")
plt.xlabel('Intervals')
plt.ylabel('relative_frequency')
plt.show()


# 1.4 Дослідити розподіл
def max_number_in_range():
    thousand_numbers = np.random.rand(1, 1000)
    return np.max(thousand_numbers)


max_numbers_in_range = []
for i in range(1000000):
    max_numbers_in_range.append(max_number_in_range())

plt.hist(max_numbers_in_range, bins=50)
plt.show()
