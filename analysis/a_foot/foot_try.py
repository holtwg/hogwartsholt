# coding=utf-8

from bs4 import BeautifulSoup
def clean_data(value):
    # 去除空格和其他非数字字符
    value = value.replace(' ', '').replace(',', '')
    return value




# name = control_all.analy_name
# def clear_num(name):
def clear_num():
    # with open(u'2023-8-23 亞冠盃 艾納斯 VS 沙巴柏阿爾艾利杜拜.xls', 'r') as file:
    # with open(u'2023-8-22 亞冠盃 上海海港 VS 巴吞聯.xls', 'r') as file: #阿仙奴 小 二 小  100%:
    # with open(u'2023-8-22 英超 水晶宮 VS 阿仙奴.xls', 'r') as file: #阿仙奴 小 二 小  100%:
    # with open(u'2023-8-22 意甲 博洛尼亞 VS AC米蘭.xls', 'r') as file:
    # with open(u'2023-8-23 歐冠盃 琴斯托霍瓦 VS 哥本哈根.xls', 'r') as file:  # 歌本

    with open(u'2023-9-8 歐洲盃 塞爾維亞 VS 匈牙利.xls', 'r') as file:  # 匈牙利

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
    print(data)
    return data


# import control_all
def calculate_win_probability(data):
    home_win_prob_sum = 0
    away_win_prob_sum = 0
    num_games = len(data) - 1  # 减去表头

    for i in range(1, len(data)):
        home_prob = float(data[i][5])
        away_prob = float(data[i][6])
        home_win_prob_sum += home_prob
        away_win_prob_sum += away_prob

    home_win_prob_avg = home_win_prob_sum / num_games
    away_win_prob_avg = away_win_prob_sum / num_games

    return home_win_prob_avg, away_win_prob_avg


def calculate_kelly_index(data):
    home_kelly_sum = 0
    away_kelly_sum = 0
    num_games = len(data) - 1  # 减去表头

    for i in range(1, len(data)):
        home_prob = float(data[i][5])
        away_prob = float(data[i][6])
        home_kelly = float(data[i][7])
        away_kelly = float(data[i][8])
        home_kelly_sum += home_prob * home_kelly
        away_kelly_sum += away_prob * away_kelly

    home_kelly_index = home_kelly_sum / num_games
    away_kelly_index = away_kelly_sum / num_games

    return home_kelly_index, away_kelly_index


def calculate_return_rate(data):
    return_rate_sum = 0
    num_games = len(data) - 1  # 减去表头

    for i in range(1, len(data)):
        return_rate = float(data[i][9])
        return_rate_sum += return_rate

    return_rate_avg = return_rate_sum / num_games

    return return_rate_avg

data = clear_num()


import numpy as np
import matplotlib.pyplot as plt


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

# print(home_team_probabilities)
# print(ping_team_probabilities)
# print(away_team_probabilities)


# from scipy.stats import f_oneway


# # 进行单因素方差分析 (ANOVA)
# f_statistic, p_value = f_oneway(home_team_probabilities, ping_team_probabilities , away_team_probabilities )
#
# # 打印分析结果
# print("单因素方差分析结果:")
# print("F 统计量:", f_statistic)
# print("p 值:", p_value)
#
# # 根据 p 值判断是否存在显著差异
# alpha = 0.05
# if p_value < alpha:
#     print("数据之间存在显著差异")
# else:
#     print("数据之间不存在显著差异")
import numpy as np


# # 计算 Cohen's d 效应大小
# def cohen_d(group1, group2):
#     mean_diff = np.mean(group1) - np.mean(group2)
#     pooled_std = np.sqrt((np.std(group1, ddof=1)**2 + np.std(group2, ddof=1)**2) / 2)
#     return mean_diff / pooled_std
#
# # 计算效应大小
# effect_size1 = cohen_d(home_team_probabilities, ping_team_probabilities)
# effect_size2 = cohen_d(home_team_probabilities, away_team_probabilities)
# effect_size3 = cohen_d(ping_team_probabilities, away_team_probabilities)
#
# # 打印效应大小
# print("效应大小 (data1 vs. data2):", effect_size1)
# print("效应大小 (data1 vs. data3):", effect_size2)
# print("效应大小 (data2 vs. data3):", effect_size3)
#
# # 比较效应大小来判断优势
# if effect_size1 > 0 and effect_size1 > effect_size2 and effect_size1 > effect_size3:
#     print("数据组 1 更具优势")
# elif effect_size2 > 0 and effect_size2 > effect_size1 and effect_size2 > effect_size3:
#     print("数据组 3 更具优势")
# else:
#     print("数据组 2 更具优势")

"""
import numpy as np
import matplotlib.pyplot as plt

# data1 = [0.83333333, 0.89285714, 0.86206897, ...]  # 第一组数据
# data2 = [0.15384615, 0.125, 0.15873016, ...]        # 第二组数据
# data3 = [0.07692308, 0.05882353, 0.1, ...]          # 第三组数据

# 计算平均值、标准差和中位数
avg_data1 = np.mean(home_team_probabilities)
avg_data2 = np.mean(ping_team_probabilities)
avg_data3 = np.mean(away_team_probabilities)

std_data1 = np.std(home_team_probabilities)
std_data2 = np.std(ping_team_probabilities)
std_data3 = np.std(away_team_probabilities)

median_data1 = np.median(home_team_probabilities)
median_data2 = np.median(ping_team_probabilities)
median_data3 = np.median(away_team_probabilities)

# 打印统计信息
print("数据组 1 - 平均值:", avg_data1)
print("数据组 2 - 平均值:", avg_data2)
print("数据组 3 - 平均值:", avg_data3)
print("\n数据组 1 - 标准差:", std_data1)
print("数据组 2 - 标准差:", std_data2)
print("数据组 3 - 标准差:", std_data3)
print("\n数据组 1 - 中位数:", median_data1)
print("数据组 2 - 中位数:", median_data2)
print("数据组 3 - 中位数:", median_data3)

# 绘制直方图
plt.hist(home_team_probabilities, alpha=0.5, label='数据组 1', bins=15)
plt.hist(ping_team_probabilities, alpha=0.5, label='数据组 2', bins=15)
plt.hist(away_team_probabilities, alpha=0.5, label='数据组 3', bins=15)
plt.xlabel('值')
plt.ylabel('频数')
plt.title('数据分布直方图')
plt.legend()
plt.show()

# 比较平均值来判断优势
if avg_data1 > avg_data2 and avg_data1 > avg_data3:
    print("数据组 1 更具优势")
elif avg_data2 > avg_data1 and avg_data2 > avg_data3:
    print("数据组 2 更具优势")
else:
    print("数据组 3 更具优势")
"""


import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd


# 进行单因素方差分析 (ANOVA)
f_statistic, p_value = f_oneway(home_team_probabilities, ping_team_probabilities, away_team_probabilities)

# 打印分析结果
print("单因素方差分析结果:")
print("F 统计量:", f_statistic)
print("p 值:", p_value)

# 使用 Tukey's HSD 测验进行多重比较校正
data_all = np.concatenate((home_team_probabilities, ping_team_probabilities, away_team_probabilities))
group_labels = ['data1'] * len(home_team_probabilities) + ['data2'] * len(ping_team_probabilities) + ['data3'] * len(away_team_probabilities)

tukey_results = pairwise_tukeyhsd(data_all, group_labels, alpha=0.05)

# 打印多重比较结果
print("\nTukey's HSD 多重比较结果:")
print(tukey_results)

# 判断哪组更好
best_group = np.argmax(np.array([np.mean(home_team_probabilities), np.mean(ping_team_probabilities), np.mean(away_team_probabilities)]))
print("\n数据组", best_group + 1, "更好")
