# coding=utf-8
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt



import anlay_haha


# 两组数据
data_group1 = anlay_haha.home_team_probabilities
data_group2 = anlay_haha.away_team_probabilities
# print(data_group1)
# print(data_group2)


# 计算基本统计量
mean_group1 = np.mean(data_group1)
mean_group2 = np.mean(data_group2)
std_group1 = np.std(data_group1)
std_group2 = np.std(data_group2)
median_group1 = np.median(data_group1)
median_group2 = np.median(data_group2)

# 进行假设检验（t检验）
t_statistic, p_value = stats.ttest_ind(data_group1, data_group2)

# 正态性检验（Shapiro-Wilk测试）
_, normality_pvalue_group1 = stats.shapiro(data_group1)
_, normality_pvalue_group2 = stats.shapiro(data_group2)

# 计算置信区间
confidence_level = 0.95
ci_group1 = stats.norm.interval(confidence_level, loc=mean_group1, scale=std_group1/np.sqrt(len(data_group1)))
ci_group2 = stats.norm.interval(confidence_level, loc=mean_group2, scale=std_group2/np.sqrt(len(data_group2)))

# 绘制直方图
plt.hist(data_group1, alpha=0.5, label='Group 1')
plt.hist(data_group2, alpha=0.5, label='Group 2')
plt.legend()
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Group 1 vs Group 2')
plt.show()

# 打印结果
print("Group 1:")
print(f"Mean: {mean_group1}, Standard Deviation: {std_group1}, Median: {median_group1}")
print(f"Normality p-value: {normality_pvalue_group1}")
print(f"Confidence Interval ({confidence_level*100}%): {ci_group1}")

print("\nGroup 2:")
print(f"Mean: {mean_group2}, Standard Deviation: {std_group2}, Median: {median_group2}")
print(f"Normality p-value: {normality_pvalue_group2}")
print(f"Confidence Interval ({confidence_level*100}%): {ci_group2}")

print("\nT-test results:")
print(f"t-statistic: {t_statistic}, p-value: {p_value}")



# # 计算基本统计量
# mean_group1 = np.mean(data_group1)
# mean_group2 = np.mean(data_group2)
# std_group1 = np.std(data_group1)
# std_group2 = np.std(data_group2)
# median_group1 = np.median(data_group1)
# median_group2 = np.median(data_group2)
#
# # 进行假设检验（t检验）
# t_statistic, p_value = stats.ttest_ind(data_group1, data_group2)
#
# # 绘制直方图
# plt.hist(data_group1, alpha=0.5, label='Group 1')
# plt.hist(data_group2, alpha=0.5, label='Group 2')
# plt.legend()
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram of Group 1 vs Group 2')
# plt.show()
#
# # 打印结果
# print("Group 1:")
# print(f"Mean: {mean_group1}, Standard Deviation: {std_group1}, Median: {median_group1}")
# print("\nGroup 2:")
# print(f"Mean: {mean_group2}, Standard Deviation: {std_group2}, Median: {median_group2}")
# print("\nT-test results:")
# print(f"t-statistic: {t_statistic}, p-value: {p_value}")