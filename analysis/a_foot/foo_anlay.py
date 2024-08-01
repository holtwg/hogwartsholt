# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 数据
# data = {
#     '序号': range(1, 91),
#     '博彩公司': ['Betfair(英国)', 'Nordicbet(马恩岛)', '10B(英国)', ...],  # 填写完整数据
#     '初盘主': [2.42, 2.45, 2.10, ...],  # 填写完整数据
#     '初盘平': [3.20, 3.00, 3.25, ...],  # 填写完整数据
#     '初盘客': [2.98, 2.80, 2.90, ...],  # 填写完整数据
#     '即时盘主': [3.10, 3.00, 3.00, ...],  # 填写完整数据
#     '即时盘平': [3.10, 2.92, 2.85, ...],  # 填写完整数据
#     '即时盘客': [2.74, 2.52, 2.60, ...],  # 填写完整数据
#     '最新概率(%)主': [31.93, 31.08, 31.19, ...],  # 填写完整数据
#     '最新概率(%)平': [31.93, 31.93, 32.83, ...],  # 填写完整数据
#     '最新概率(%)客': [36.13, 37.00, 35.98, ...],  # 填写完整数据
#     '最新凯利指数主': [1.00, 0.97, 0.97, ...],  # 填写完整数据
#     '最新凯利指数平': [0.98, 0.92, 0.90, ...],  # 填写完整数据
#     '最新凯利指数客': [0.99, 0.91, 0.94, ...],  # 填写完整数据
#     '返还率值': [98.98, 93.24, 93.56, ...],  # 填写完整数据
# }
#
# # 创建DataFrame
# df = pd.DataFrame(data)
#
# # 打印前几行数据
# print(df.head())
#
# # 绘制初盘和即时盘的平均值对比图
# plt.figure(figsize=(10, 6))
# plt.plot(df['序号'], df['初盘主'], label='初盘主')
# plt.plot(df['序号'], df['初盘平'], label='初盘平')
# plt.plot(df['序号'], df['初盘客'], label='初盘客')
# plt.plot(df['序号'], df['即时盘主'], label='即时盘主')
# plt.plot(df['序号'], df['即时盘平'], label='即时盘平')
# plt.plot(df['序号'], df['即时盘客'], label='即时盘客')
# plt.legend()
# plt.xlabel('序号')
# plt.ylabel('赔率')
# plt.title('初盘和即时盘的平均值对比')
# plt.show()
#
# # 绘制最新凯利指数的分布图
# plt.figure(figsize=(8, 6))
# plt.hist(df['最新凯利指数主'], bins=20, alpha=0.5, label='主')
# plt.hist(df['最新凯利指数平'], bins=20, alpha=0.5, label='平')
# plt.hist(df['最新凯利指数客'], bins=20, alpha=0.5, label='客')
# plt.legend()
# plt.xlabel('凯利指数')
# plt.ylabel('频数')
# plt.title('最新凯利指数的分布')
# coding=utf-8

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
def clean_data(value):
    # 去除空格和其他非数字字符
    value = value.replace(' ', '').replace(',', '')
    return value






# with open(u'2023-8-11 女世界盃 西班牙女足 VS 荷蘭女足.xls', 'r') as file:  #  荷兰
# with open(u'2023-8-11 女世界盃 日本女足 VS 瑞典女足.xls', 'r') as file:  #  瑞典
# with open(u'2023-8-12 法甲 奈斯 VS 利爾.xls', 'r') as file:  #  奈斯
# with open(u'2023-8-12 西甲 西維爾 VS 華倫西亞.xls', 'r') as file:  #  华伦西亚

# with open(u'2023-8-12 女世界盃 澳洲女足 VS 法國女足.xls', 'r') as file:  #  维恩
# with open(u'2023-8-12 女世界盃 英格蘭女足 VS 哥倫比亞女足.xls', 'r') as file:  #  英格兰胜
# with open(u'2023-8-12 日職聯 川崎前鋒 VS 神戶勝利船.xls', 'r') as file:  #  神户
# with open(u'2023-8-12 日職聯 FC東京 VS 京都不死鳥.xls', 'r') as file:  #  FC
# with open(u'2023-8-12 英超 阿仙奴 VS 諾定咸森林.xls', 'r') as file:  #  威森林
# with open(u'2023-8-12 英超 白禮頓 VS 盧頓.xls', 'r') as file:  #  维恩
# with open(u'2023-8-12 英冠 伯明翰 VS 列斯聯.xls', 'r') as file:  #  维恩
# with open(u'2023-8-12 英冠 修咸頓 VS 諾域治.xls', 'r') as file:  #  维恩
# with open(u'2023-8-12 英冠 屈福特 VS 普利茅夫.xls', 'r') as file:  #  维恩
# with open(u'2023-8-12 英冠 哈德斯菲爾德 VS 李斯特城.xls', 'r') as file:  #  维恩
# with open(u'2023-8-12 荷甲 PSV燕豪芬 VS 烏德勒支.xls', 'r') as file:  #  维恩
#
# with open(u'2023-8-12 法甲 馬賽 VS 蘭斯.xls', 'r') as file:  #  维恩
# with open(u'2023-8-12 挪超 薩普斯堡 VS 史卓加斯特.xls', 'r') as file:  #  维恩
# with open(u'2023-8-13 法乙 巴斯蒂亞 VS 華倫西恩斯.xls', 'r') as file:  #  维恩
# with open(u'2023-8-13 法乙 昂熱 VS 安納西.xls', 'r') as file:  #  维恩
# with open(u'2023-8-13 英超 紐卡素 VS 阿士東維拉.xls', 'r') as file:  #  维恩
# with open(u'2023-8-13 荷甲 阿積士 VS 荷華高斯.xls', 'r') as file:  #  维恩
# with open(u'2023-8-12 西甲 皇家蘇斯達 VS 傑羅納.xls', 'r') as file:  # 维恩
# with open(u'2023-8-13 法乙 歐塞爾 VS 阿美恩斯.xls', 'r') as file:  #  维恩
# with open(u'2023-8-13 德超盃 拜仁慕尼黑 VS RB萊比錫.xls', 'r') as file:  #  维恩
# with open(u'2023-8-13 西甲 畢爾包 VS 皇家馬德里.xls', 'r') as file:  #  维恩
# with open(u'2023-8-14 葡超 阿洛卡 VS 伊斯托里爾.xls', 'r') as file:  #  维恩
# with open(u'2023-8-13 瑞典超 天狼星 VS 卡馬亞.xls', 'r') as file:  #  天狼星
# with open(u'2023-8-13 瑞典超 哥登堡 VS 佐加頓斯.xls', 'r') as file:  #  哥
# with open(u'2023-8-13 英超 賓福特 VS 熱刺.xls', 'r') as file:  #  滨福特
# with open(u'2023-8-13 英超 車路士 VS 利物浦.xls', 'r') as file:  #  车路士
# with open(u'2023-8-13 西甲 切爾達 VS 奧沙辛拿.xls', 'r') as file:  #  奥沙
# with open(u'2023-8-14 西甲 加泰 VS 巴塞隆拿.xls', 'r') as file:  #  嘉泰
# with open(u'2023-8-15 瑞典超 米贊比 VS 馬模.xls', 'r') as file:  #  嘉泰
# with open(u'2023-8-15 英超 曼聯 VS 狼隊.xls', 'r') as file:  #  嘉泰
# with open(u'2023-8-15 西甲 馬德里體育會 VS 格蘭納達.xls', 'r') as file:  #  马德里
# with open(u'2023-8-15 葡超 博維斯塔 VS 賓菲加.xls', 'r') as file:  #  博
# with open(u'2023-8-15 女世界盃 西班牙女足 VS 瑞典女足.xls', 'r') as file:  #  嘉泰
# with open(u'2023-8-16 歐冠盃 莫迪 VS 基卡拉斯域卡.xls', 'r') as file:  #  嘉+1
# with open(u'2023-8-16 歐冠盃 海法馬卡比 VS 巴迪斯拉華.xls', 'r') as file:  #  吗卡比
# with open(u'2023-8-16 歐冠盃 布拉格斯巴達 VS 哥本哈根.xls', 'r') as file:  #  歌本
# with open(u'2023-8-16 歐冠盃 馬賽 VS 彭拿典奈高斯.xls', 'r') as file:  #  +1平
# with open(u'2023-8-17 超霸盃 曼城 VS 西維爾.xls', 'r') as file:  #  嘉泰
# with open(u'2023-8-17 巴西盃 聖保羅 VS 哥連泰斯.xls', 'r') as file:  #  嘉泰
# with open(u'2023-8-17 巴西盃 法林明高 VS 甘美奧.xls', 'r') as file:  #  嘉泰
# with open(u'2023-8-18 日職聯 浦和紅鑽 VS 名古屋八鯨.xls', 'r') as file:  #  嘉泰



# with open(u'2023-8-20 日職聯 FC橫濱 VS 大阪櫻花.xls', 'r') as file:  #  樱花 大 大 小 100%
# with open(u'2023-8-20 女世界盃 西班牙女足 VS 英格蘭女足.xls', 'r') as file: #西班牙 大  大 100%
# with open(u'2023-8-20 英冠 諾域治 VS 米禾爾.xls', 'r') as file: #若域治 大 大 小 100%
# with open(u'2023-8-21 西甲 巴塞隆拿 VS 卡迪斯.xls', 'r') as file: #+2平 二 大 二 0%
# with open(u'2023-8-21 俄超 莫斯科斯巴達 VS 聖彼德斯堡.xls', 'r') as file: #圣彼得堡 二 大 小 100%
# with open(u'2023-8-21 美職業 紐約城 VS 明尼蘇達聯.xls', 'r') as file: #明尼苏达联 小 二 大 1.18%
# with open(u'2023-8-20 英超 阿士東維拉 VS 愛華頓.xls', 'r') as file: #阿士 小 二 小 100%
# with open(u'2023-8-20 英超 韋斯咸 VS 車路士.xls', 'r') as file: #伟斯咸 大 二 大 66.67%
# with open(u'2023-8-21 意甲 羅馬 VS 沙蘭力坦拿.xls', 'r') as file: #伟斯咸 二 小 大  0%

# with open(u'2023-8-22 西甲 艾拉維斯 VS 西維爾.xls', 'r') as file: #艾拉维斯 小 小 大  51.760%
# with open(u'2023-8-22 西甲 艾拉維斯 VS 西維爾1.xls', 'r') as file: #艾拉维斯 小 小 大  51.760%
# with open(u'2023-8-22 瑞典超 諾高平 VS AIK蘇納.xls', 'r') as file: #若高平 小 小 小  0%
# with open(u'2023-8-22 瑞典超 諾高平 VS AIK蘇納1.xls', 'r') as file: #若高平 小 二 小  100%
# with open(u'2023-8-22 荷乙 阿積士青年隊 VS 迪加史卓普.xls', 'r') as file: #迪迦 大 小 小  100%
# with open(u'2023-8-22 意甲 博洛尼亞 VS AC米蘭.xls', 'r') as file: #米兰 大 二 小  100%
# with open(u'2023-8-22 英超 水晶宮 VS 阿仙奴.xls', 'r') as file: #阿仙奴 小 二 小  100%
#
# with open(u'2023-8-22 亞冠盃 上海海港 VS 巴吞聯.xls', 'r') as file: #阿仙奴 小 二 小  100%
# with open(u'2023-8-23 亞冠盃 艾納斯 VS 沙巴柏阿爾艾利杜拜.xls', 'r') as file: #阿仙奴 小 二 小  100%
# with open(u'2023-8-23 歐冠盃 琴斯托霍瓦 VS 哥本哈根.xls', 'r') as file: # 歌本 小 二 小  100%
# with open(u'2023-8-23 歐冠盃 格拉斯哥流浪 VS PSV燕豪芬.xls', 'r') as file: # 歌本 小 二 小  100%
# with open(u'2023-8-23 歐冠盃 安特衛普 VS AEK雅典.xls', 'r') as file: # 歌本 小 二 小  100%
# with open(u'2023-8-24 歐冠盃 莫迪 VS 加拉塔沙雷.xls', 'r') as file: # 歌本 小 二 小  100%
# with open(u'2023-8-24 歐冠盃 海法馬卡比 VS 年青人.xls', 'r') as file: # 歌本 小 二 小  100%
# with open(u'2023-8-24 歐冠盃 布拉加 VS 彭拿典奈高斯.xls', 'r') as file: # 歌本 小 二 小  100%


# with open(u'2023-8-30 英聯盃 富咸 VS 熱刺.xls', 'r') as file: # fuxian 小 小 二  16.36%  二高
# with open(u'2023-8-30 歐冠盃 年青人 VS 海法馬卡比.xls', 'r') as file: # 年轻人 大 小 小  100%
# with open(u'2023-8-30 歐冠盃 加拉塔沙雷 VS 莫迪.xls', 'r') as file: # +1 平  小 小 二  0%
# with open(u'2023-8-30 歐冠盃 彭拿典奈高斯 VS 布拉加.xls', 'r') as file: # 布拉加  大 小 二 二高  100%
# with open(u'2023-8-31 英聯盃 諾定咸森林 VS 般尼.xls', 'r') as file: # 布拉加  大 小 二 二高  100%

# with open(u'2023-8-31 歐冠盃 哥本哈根 VS 琴斯托霍瓦.xls', 'r') as file: # 琴 大 大 二 二高  100%
# with open(u'2023-8-31 歐冠盃 PSV燕豪芬 VS 格拉斯哥流浪.xls', 'r') as file: # 燕好 大 小 小 二高  100%
# with open(u'2023-8-31 歐冠盃 AEK雅典 VS 安特衛普.xls', 'r') as file: # 安特卫普 小 小 大 二高  0%
# with open(u'2023-8-31 歐霸盃 卡拉巴克 VS 奧林比查.xls', 'r') as file: # 布拉加  大 小 二 二高  100%
# with open(u'2023-9-1 歐霸盃 布拉格斯巴達 VS 薩格勒布戴拿模.xls', 'r') as file: # 布拉加  大 小 二 二高  100%
# with open(u'2023-9-1 歐霸盃 阿積士 VS 盧多格德斯.xls', 'r') as file: # 布拉加  大 小 二 二高  100%
# with open(u'2023-9-1 歐霸盃 鴨巴甸 VS 赫根.xls', 'r') as file: # 布拉加  大 小 二 二高  100%
# with open(u'2023-9-1 歐會盃 費倫天拿 VS 維也納迅速.xls', 'r') as file: # 布拉加  大 小 二 二高  100%
# with open(u'2023-9-6 日聯盃 大阪飛腳 VS 浦和紅鑽.xls', 'r') as file: # 蒲河 小 二大 二大 二高  100%
# with open(u'2023-9-6 日聯盃 名古屋八鯨 VS 鹿島鹿角.xls', 'r') as file: # 鹿岛 小 小 大 低  95%
# with open(u'2023-9-6 日聯盃 札幌岡薩多 VS 橫濱水手.xls', 'r') as file: # 扎 大 小 二大 高  100%
# with open(u'2023-9-8 歐洲盃 塞爾維亞 VS 匈牙利.xls', 'r') as file: # 扎 大 小 二大 高  100%
# with open(u'2023-9-8 歐洲盃 荷蘭 VS 希臘 (1).xls', 'r') as file: # 扎 大 小 二大 高  100%
# with open(u'2023-9-8 南美預選 巴拉圭 VS 秘魯.xls', 'r') as file: # 扎 大 小 二大 高  100%
# with open(u'2023-9-8 歐洲盃 法國 VS 愛爾蘭.xls', 'r') as file: # 扎 大 小 二大 高  100%

with open(u'2024-6-15 歐洲盃 德國 VS 蘇格蘭.xls', 'r',errors='ignore') as file: # 扎 大 小 二大 高  100%
# with open(u'2024-6-15 歐洲盃 匈牙利 VS 瑞士.xls', 'r') as file: # 扎 大 小 二大 高  100%

# with open(u'2023-9-7 哥斯盃 阿拉倫斯 VS 慕尼斯帕爾利比亞.xls', 'r') as file: # 慕妮丝 二大 小 大 高  0%
# with open(u'2023-9-7 阿根廷盃 里奧瓜托學生隊 VS 防衛者.xls', 'r') as file: # 学生队 大 二大 大 高  0%
# with open(u'2023-9-7 巴西乙 施亞拉 VS 隆德里納.xls', 'r') as file: # 塞亚拉 大 大 小   100%
# with open(u'2023-9-7 薩爾超 阿利安薩聖薩爾瓦多 VS 薩卡特科盧卡.xls', 'r') as file: # 萨尔卡 小 大 大   0%
# with open(u'2023-9-7 哥倫甲 卡利 VS 聖達菲.xls', 'r') as file: # 圣达非 小 大 大   0%
# with open(u'2023-9-7 哥斯盃 薩普里沙 VS 森卡洛斯.xls', 'r') as file: # 森卡 大 小 大   0%



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
# print(data)



# 打印数据
# for row in data:
#     print(row)
# print(data)






# Extracting win, draw, and lose results
wins = [float(row[2]) for row in data]
draws = [float(row[3]) for row in data]
loses = [float(row[4]) for row in data]

# print(wins)

wins1 = [float(row[5]) for row in data]
draws1 = [float(row[6]) for row in data]
loses1 = [float(row[7]) for row in data]

a_probability = [float(row[8]) for row in data]
# a_probability = [row[8] for row in data]
# print(a_probability)
b_probability = [float(row[9]) for row in data]
# b_probability = [row[9] for row in data]
c_probability = [float(row[10]) for row in data]
# c_probability = [row[10] for row in data]
a_kai = [row[11] for row in data]
b_kai = [row[12]for row in data]
c_kai = [row[13] for row in data]

zhu = np.inner([wins, wins1], [a_probability, a_kai])
ping = np.inner([draws, draws1], [b_probability, b_kai])
ke = np.inner([loses, loses1], [c_probability,c_kai])
# print(wins1)
print(np.inner([wins, wins1], a_probability))
print(np.inner([draws, draws1], b_probability))
print(np.inner([loses, loses1], c_probability))

a = np.vdot(wins, wins1)
b = np.vdot(draws, draws1)
c = np.vdot(loses, loses1)
a_p = np.dot(a_probability, a_kai)
b_p = np.dot(b_probability, b_kai)
c_p = np.dot(c_probability, c_kai)
# print(a_p)
# print(b_p)
# print(c_p)
total_matches = len(data)
print((a * a_p)/total_matches/1000)
print((b * b_p)/total_matches/1000)
print((c * c_p)/total_matches/1000)
# Calculate probabilities
# total_matches = len(data)
# win_probability = len([result for result in wins if result < 3.0]) / total_matches
# draw_probability = len([result for result in draws if result < 3.0]) / total_matches
# lose_probability = len([result for result in loses if result < 3.0]) / total_matches
win_probability = len([result for result in wins1 if result < 3.5]) / total_matches
draw_probability = len([result for result in draws1 if result < 3.5]) / total_matches
lose_probability = len([result for result in loses1 if result < 3.5]) / total_matches



zhu_data = np.multiply(wins, wins1)
ping_data = np.multiply(draws, draws1)
ke_data = np.multiply(loses, loses1)
# print((wins1, a_kai))
# print(np.dot(draws1, b_kai))
# print(np.dot(loses1, c_kai))

# print(a/total_matches)
# print(b/total_matches)
# print(c/total_matches)

print(f"Win Probability: {win_probability:.2%}")
print(f"Draw Probability: {draw_probability:.2%}")
print(f"Lose Probability: {lose_probability:.2%}")

# Plot histograms
plt.figure(figsize=(10, 6))
# plt.hist(wins, bins=20, alpha=0.7, label='Win')
# plt.hist(draws, bins=20, alpha=0.7, label='Draw')
# plt.hist(loses, bins=20, alpha=0.7, label='Lose')
plt.hist(zhu_data, bins=20, alpha=0.7, label='Win')
plt.hist(ping_data, bins=20, alpha=0.7, label='Draw')
plt.hist(ke_data, bins=20, alpha=0.7, label='Lose')
# plt.hist(wins1, bins=20, alpha=0.7, label='Win')
# plt.hist(draws1, bins=20, alpha=0.7, label='Draw')
# plt.hist(loses1, bins=20, alpha=0.7, label='Lose')
plt.xlabel('Odds')
plt.ylabel('Frequency')
plt.title('Odds Distribution')
plt.legend()
plt.show()

# Plot boxplots
plt.figure(figsize=(10, 6))
# plt.boxplot([wins, draws, loses], labels=['Win', 'Draw', 'Lose'])
# plt.boxplot([wins1, draws1, loses1], labels=['Win', 'Draw', 'Lose'])
plt.boxplot([zhu_data, ping_data, ke_data], labels=['Win', 'Draw', 'Lose'])
plt.ylabel('Odds')
plt.title('Boxplot of Odds')
plt.show()
