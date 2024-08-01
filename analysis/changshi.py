# data = [
#     [1.0, 'Interwetten(马耳他)', '1.4', '2.75', '1.12', '5.5', '83.08', '16.92', '0.9408', '0.88', '93.05'],
#     # ... (其他数据)
#     [97.0, 'Vbet.UKR', '1.87', '1.87', '1.1', 6.0, '84.51', '15.49', '0.924', '0.96', '92.96']
# ]

# import transform_xml
# def calculate_win_probability(data):
#     home_win_prob_sum = 0
#     away_win_prob_sum = 0
#     num_games = len(data) - 1  # 减去表头
#
#     for i in range(1, len(data)):
#         home_prob = float(data[i][5])
#         away_prob = float(data[i][6])
#         home_win_prob_sum += home_prob
#         away_win_prob_sum += away_prob
#
#     home_win_prob_avg = home_win_prob_sum / num_games
#     away_win_prob_avg = away_win_prob_sum / num_games
#
#     return home_win_prob_avg, away_win_prob_avg
#
#
# def calculate_kelly_index(data):
#     home_kelly_sum = 0
#     away_kelly_sum = 0
#     num_games = len(data) - 1  # 减去表头
#
#     for i in range(1, len(data)):
#         home_prob = float(data[i][5])
#         away_prob = float(data[i][6])
#         home_kelly = float(data[i][7])
#         away_kelly = float(data[i][8])
#         home_kelly_sum += home_prob * home_kelly
#         away_kelly_sum += away_prob * away_kelly
#
#     home_kelly_index = home_kelly_sum / num_games
#     away_kelly_index = away_kelly_sum / num_games
#
#     return home_kelly_index, away_kelly_index
#
#
# def calculate_return_rate(data):
#     return_rate_sum = 0
#     num_games = len(data) - 1  # 减去表头
#
#     for i in range(1, len(data)):
#         return_rate = float(data[i][9])
#         return_rate_sum += return_rate
#
#     return_rate_avg = return_rate_sum / num_games
#
#     return return_rate_avg
#
# # data = transform_xml.clear_num(control_all.analy_name)
#
# data = transform_xml.clear_num()
#
# def convert_odds_to_probability(odds):
#     return 1 / float(odds)
#
# home_team_probabilities = []
# away_team_probabilities = []
#
# for row in data:
#     home_team_prob = convert_odds_to_probability(row[2])
#     away_team_prob = convert_odds_to_probability(row[4])
#     home_team_probabilities.append(home_team_prob)
#     away_team_probabilities.append(away_team_prob)
#
# print("主队获胜概率：", home_team_probabilities)
# print("客队获胜概率：", away_team_probabilities)
# coding=utf-8
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt





from bs4 import BeautifulSoup
def clean_data(value):
    # 去除空格和其他非数字字符
    value = value.replace(' ', '').replace(',', '')
    return value


# with open(u'2023-10-20 NBL(A) 伊拉瓦拉老鹰 VS 墨尔本联.xls', 'r') as file:  # 主  # p-v大 std大 大大 25 低
# with open(u'2023-10-20 Euro 皇家马德里 VS 米兰阿玛尼.xls', 'r') as file:  # 主  # p-v大 std大 大大 25 低
# with open(u'2023-10-20 Euro 奥林匹亚科斯 VS 游击队.xls', 'r') as file:  # 主  # p-v大 std大 大大 25 低
with open(u'2023-10-20 Euro 费内巴切 VS 里昂.xls', 'r') as file:  # 主  # p-v大 std大 大大 25 低


    html_content = file.read()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 查找表格元素
table = soup.find('table')

# 提取表格数据
data = []
rows = table.find_all('tr')[1:]  # 跳过表头行
for row in rows:
    cells = [cell.text.strip() for cell in row.find_all('td')]
    cleaned_cells = [clean_data(cell) for cell in cells]  # 清洗数据

    # 检查第一个元素是否为数字，以排除非数据行
    if cleaned_cells[0].isdigit():
        data.append(cleaned_cells)

# 将数据转换为浮点数
for i in range(len(data)):
    for j in range(len(data[i])):
        # 检查是否为数字，如果不是则将其保持为字符串
        if data[i][j].isdigit():
            data[i][j] = float(data[i][j])


def convert_odds_to_probability(odds):
    return 1 / float(odds)

home_team_probabilities = []
ping_team_probabilities = []
away_team_probabilities = []

for row in data:
    home_team_prob = convert_odds_to_probability(row[2])
    ping_team_prob = convert_odds_to_probability(row[3])
    away_team_prob = convert_odds_to_probability(row[4])
    home_team_probabilities.append(home_team_prob)
    ping_team_probabilities.append(ping_team_prob)
    away_team_probabilities.append(away_team_prob)

home_team_probabilities = np.array(home_team_probabilities)
ping_team_probabilities = np.array(ping_team_probabilities)
away_team_probabilities = np.array(away_team_probabilities)

# 两组数据
data_group1 = home_team_probabilities
data_group2 = ping_team_probabilities
data_group3 = away_team_probabilities

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


# 计算基本统计量
mean_group1 = np.mean(data_group1)
mean_group2 = np.mean(data_group2)
mean_group3 = np.mean(data_group3)
std_group1 = np.std(data_group1)
std_group2 = np.std(data_group2)
std_group3 = np.std(data_group3)
median_group1 = np.median(data_group1)
median_group2 = np.median(data_group2)
median_group3 = np.median(data_group3)

# 进行假设检验（t检验）
# t_statistic, p_value = stats.ttest_ind(data_group1, data_group2, data_group3)
t_statistic, p_value = stats.ttest_ind(data_group1, data_group3)

# 正态性检验（Shapiro-Wilk测试）
_, normality_pvalue_group1 = stats.shapiro(data_group1)
_, normality_pvalue_group2 = stats.shapiro(data_group2)
_, normality_pvalue_group3 = stats.shapiro(data_group3)

# 计算置信区间
confidence_level = 0.95
ci_group1 = stats.norm.interval(confidence_level, loc=mean_group1, scale=std_group1/np.sqrt(len(data_group1)))
ci_group2 = stats.norm.interval(confidence_level, loc=mean_group2, scale=std_group2/np.sqrt(len(data_group2)))
ci_group3 = stats.norm.interval(confidence_level, loc=mean_group3, scale=std_group3/np.sqrt(len(data_group3)))

# 绘制直方图
plt.hist(data_group1, alpha=0.5, label='Group 1')
plt.hist(data_group2, alpha=0.5, label='Group 2')
plt.hist(data_group3, alpha=0.5, label='Group 3')
plt.legend()
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Group 1 vs Group 2 vs Group 3')
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

print("\nGroup 3:")
print(f"Mean: {mean_group3}, Standard Deviation: {std_group3}, Median: {median_group3}")
print(f"Normality p-value: {normality_pvalue_group3}")
print(f"Confidence Interval ({confidence_level*100}%): {ci_group3}")

print("\nT-test results:")
print(f"t-statistic: {t_statistic}, p-value: {p_value}")
