# coding=utf-8
import pandas as pd
import transform_xml
import control_all
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

data = transform_xml.clear_num(control_all.analy_name)

# print(data)

# # 将数据存储为二维列表
# data = [
#     ['序号', '博彩公司', '主', '客', '主', '客', '主', '客', '主', '客', '值'],
#     ['最大值', '2.82', '1.94', '3.05', '1.55', '37.80', '68.39', '1.07', '1.01', '99.10'],
#     ['最小值', '1.82', '1.38', '2.30', '1.25', '31.61', '62.20', '0.80', '0.81', '84.82'],
#     ['平均值', '2.26', '1.62', '2.71', '1.45', '34.86', '65.14', '0.95', '0.94', '94.14'],
#     ['1', 'Interwetten(马耳他)', '2.10', '1.65', '2.55', '1.45', '36.25', '63.75', '0.89', '0.94', '92.44'],
#     ['2', '易胜(安提瓜和巴布达)', '2.23', '1.63', '2.50', '1.48', '37.19', '62.81', '0.88', '0.96', '92.97'],
#     # 剩下的数据行...
# ]
# 读取Excel文件
# dataframe = pd.read_html('2023-7-12 WNBA 芝加哥天空 VS 康涅狄克太阳.xml')


# 将数据转换为二维列表
# data = dataframe.values.tolist()


# home_prob, away_prob = calculate_win_probability(data)
# home_kelly_index, away_kelly_index = calculate_kelly_index(data)
# return_rate = calculate_return_rate(data)
#
# print("平均主队获胜概率：{:.2f}%".format(home_prob))
# print("平均客队获胜概率：{:.2f}%".format(away_prob))
# print("平均主队凯利指数：{:.2f}".format(home_kelly_index))
# print("平均客队凯利指数：{:.2f}".format(away_kelly_index))
# print("平均返还率：{:.2f}%".format(return_rate))



# Function to separate data for home team and away team
# def separate_teams_data(all_data):
#     home_team_data = []
#     away_team_data = []
#     for row in all_data:
#         if '(马耳他)' in row[1]:
#             home_team_data.append(row)
#         else:
#             away_team_data.append(row)
#     return home_team_data, away_team_data
#
# home_team_data, away_team_data = separate_teams_data(data)
#
# # Function to calculate the average of a specific column for a given team
# def calculate_average(column_index, team_data):
#     total = sum(float(row[column_index]) for row in team_data)
#     return total / len(team_data)
#
# # Function to find the maximum value of a specific column for a given team
# def find_maximum(column_index, team_data):
#     return max(float(row[column_index]) for row in team_data)
#
# # Function to find the minimum value of a specific column for a given team
# def find_minimum(column_index, team_data):
#     return min(float(row[column_index]) for row in team_data)
#
# # Example usage of the functions for home team and away team
# column_index = 6  # You can change this index to analyze different columns
#
# home_team_average = calculate_average(column_index, home_team_data)
# home_team_max = find_maximum(column_index, home_team_data)
# home_team_min = find_minimum(column_index, home_team_data)
#
# away_team_average = calculate_average(column_index, away_team_data)
# away_team_max = find_maximum(column_index, away_team_data)
# away_team_min = find_minimum(column_index, away_team_data)
#
# print("Home Team Analysis:")
# print(f"Average: {home_team_average}")
# print(f"Max Value: {home_team_max}")
# print(f"Min Value: {home_team_min}")
#
# print("\nAway Team Analysis:")
# print(f"Average: {away_team_average}")
# print(f"Max Value: {away_team_max}")
# print(f"Min Value: {away_team_min}")

# Function to separate data for home team and away team
# 节点
"""
def separate_teams_data(all_data):
    home_team_data = []
    away_team_data = []
    for row in all_data:
        if '(马耳他)' in row[1]:
            home_team_data.append(row)
        else:
            away_team_data.append(row)
    return home_team_data, away_team_data

home_team_data, away_team_data = separate_teams_data(data)

# Function to calculate the average of a specific column for a given team
def calculate_average(column_index, team_data):
    total = sum(float(row[column_index]) for row in team_data)
    return total / len(team_data)

# Function to find the maximum value of a specific column for a given team
def find_maximum(column_index, team_data):
    return max(float(row[column_index]) for row in team_data)

# Function to find the minimum value of a specific column for a given team
def find_minimum(column_index, team_data):
    return min(float(row[column_index]) for row in team_data)

# Example usage of the functions for home team and away team
# You can change the column_index to analyze different columns
# column_indices = [8, 9, 10]
column_indices = [5]

for index in column_indices:
    home_team_average = calculate_average(index, home_team_data)
    home_team_max = find_maximum(index, home_team_data)
    home_team_min = find_minimum(index, home_team_data)

    away_team_average = calculate_average(index, away_team_data)
    away_team_max = find_maximum(index, away_team_data)
    away_team_min = find_minimum(index, away_team_data)

    print(f"Column Index: {index}")
    print("Home Team Analysis:")
    print(f"Average: {home_team_average}")
    print(f"Max Value: {home_team_max}")
    print(f"Min Value: {home_team_min}")

    print("Away Team Analysis:")
    print(f"Average: {away_team_average}")
    print(f"Max Value: {away_team_max}")
    print(f"Min Value: {away_team_min}")
    print("\n")
# 节点
"""

import numpy as np
import matplotlib.pyplot as plt


def convert_odds_to_probability(odds):
    return 1 / float(odds)

home_team_probabilities = []
away_team_probabilities = []

for row in data:
    home_team_prob = convert_odds_to_probability(row[2])
    away_team_prob = convert_odds_to_probability(row[4])
    home_team_probabilities.append(home_team_prob)
    away_team_probabilities.append(away_team_prob)



home_team_probabilities = np.array(home_team_probabilities)
away_team_probabilities = np.array(away_team_probabilities)
# print(home_team_probabilities)
# print(away_team_probabilities)
# 进行数据分析
average_home_team_prob = np.mean(home_team_probabilities)
average_away_team_prob = np.mean(away_team_probabilities)
max_home_team_prob = np.max(home_team_probabilities)
max_away_team_prob = np.max(away_team_probabilities)
min_home_team_prob = np.min(home_team_probabilities)
min_away_team_prob = np.min(away_team_probabilities)

# 绘制直方图
plt.hist(home_team_probabilities, bins=20, alpha=0.5, label='Home Team')
plt.hist(away_team_probabilities, bins=20, alpha=0.5, label='Away Team')
plt.xlabel('Winning Probability')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.title('Distribution of Winning Probability')
plt.show()

# 绘制箱线图
plt.boxplot([home_team_probabilities, away_team_probabilities], labels=['Home Team', 'Away Team'])
plt.ylabel('Winning Probability')
plt.title('Boxplot of Winning Probability')
plt.show()

# 打印统计结果
print("平均主队获胜概率：", average_home_team_prob)
print("平均客队获胜概率：", average_away_team_prob)
print("最大主队获胜概率：", max_home_team_prob)
print("最大客队获胜概率：", max_away_team_prob)
print("最小主队获胜概率：", min_home_team_prob)
print("最小客队获胜概率：", min_away_team_prob)

