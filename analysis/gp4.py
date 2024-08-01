# coding=utf-8
import numpy as np
from scipy.stats import ttest_ind
import anlay_haha
# 两组数据
data1 = anlay_haha.home_team_probabilities
data2 = anlay_haha.away_team_probabilities
# data1 = np.array([0.6993007, 0.72463768, 0.70422535, 0.71428571, 0.69444444, 0.73529412,
#  0.72463768, 0.70422535, 0.69444444, 0.73529412, 0.73529412, 0.69444444,
#  0.72992701, 0.69444444, 0.6993007, 0.70422535, 0.68965517, 0.69444444,
#  0.72463768, 0.69444444, 0.72992701, 0.6993007, 0.71942446, 0.66666667,
#  0.68493151, 0.69444444, 0.91743119, 0.7518797, 0.74626866, 0.71428571,
#  0.69444444, 0.69444444, 0.72463768, 0.7518797, 0.72463768, 0.71942446,
#  0.71942446, 0.67114094, 0.68965517, 0.8, 0.69444444, 0.75757576,
#  0.72992701, 0.68965517, 0.72992701, 0.70422535, 0.72992701, 0.68965517,
#  0.70422535, 0.67567568, 0.69444444, 0.72992701, 0.6993007, 0.69444444,
#  0.71428571, 0.69444444, 0.72992701, 0.68965517, 0.65789474, 0.79365079,
#  0.79365079, 0.71428571, 0.6993007, 0.74626866, 0.74626866, 0.70422535,
#  0.72992701, 0.68965517, 0.68965517, 0.69444444, 0.71942446, 0.69444444,
#  0.7518797, 0.73529412, 0.72992701, 0.72992701, 0.74074074])
#
# data2 = np.array([0.6993007, 0.72463768, 0.70921986, 0.69444444, 0.71428571, 0.71428571,
#  0.70422535, 0.71428571, 0.71428571, 0.70422535, 0.70422535, 0.71428571,
#  0.69444444, 0.69444444, 0.70422535, 0.6993007, 0.6993007, 0.70422535,
#  0.72463768, 0.70422535, 0.70921986, 0.6993007, 0.69444444, 0.68493151,
#  0.70422535, 0.70422535, 0.68493151, 0.7518797, 0.71428571, 0.71942446,
#  0.70422535, 0.70422535, 0.70422535, 0.70422535, 0.70422535, 0.69444444,
#  0.6993007, 0.69444444, 0.71942446, 0.8, 0.71428571, 0.72463768,
#  0.68493151, 0.6993007, 0.72992701, 0.71428571, 0.70921986, 0.71428571,
#  0.70921986, 0.72463768, 0.70422535, 0.72992701, 0.6993007, 0.69444444,
#  0.71428571, 0.70422535, 0.72992701, 0.6993007, 0.68027211, 0.66666667,
#  0.66666667, 0.71428571, 0.6993007, 0.6993007, 0.6993007, 0.70921986,
#  0.71428571, 0.6993007, 0.6993007, 0.69444444, 0.72463768, 0.69444444,
#  0.70422535, 0.68965517, 0.68493151, 0.68493151, 0.72992701])

# 计算平均值
mean1 = np.mean(data1)
mean2 = np.mean(data2)

# 进行t检验
t, p = ttest_ind(data1, data2)
#
# print("Data 1 Mean:", mean1)
# print("Data 2 Mean:", mean2)
# print("T-test Result: T-value =", t, ", P-value =", p)
#
# if p < 0.05:
#     print('Data sets are significantly different存在很大不同')
# else:
#     print('Data sets are not significantly different')


from scipy.stats import mode, skew, kurtosis

# 计算数据集的中位数，模数，标准差，偏度和峰度
stats_data1 = {
    'mean': np.mean(data1),
    'median': np.median(data1),
    'mode': mode(data1)[0][0],
    'std_dev': np.std(data1),
    'variance': np.var(data1),
    'skewness偏态': skew(data1),
    'kurtosis峰度': kurtosis(data1)
}

stats_data2 = {
    'mean': np.mean(data2),
    'median': np.median(data2),
    'mode': mode(data2)[0][0],
    'std_dev': np.std(data2),
    'variance': np.var(data2),
    'skewness偏态': skew(data2),
    'kurtosis峰度': kurtosis(data2)
}

print("Stats for data set 1:\n", stats_data1)
print("Stats for data set 2:\n", stats_data2)

import matplotlib.pyplot as plt
plt.hist(data1, bins=20, alpha=0.5, label='Data 1')
plt.hist(data2, bins=20, alpha=0.5, label='Data 2')
plt.legend(loc='upper right')
plt.show()

from collections import Counter
counter_data1 = Counter(data1)
counter_data2 = Counter(data2)
print("Top 3 frequent values in data 1:", counter_data1.most_common(3))
print("Top 3 frequent values in data 2:", counter_data2.most_common(3))

