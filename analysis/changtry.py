# coding=utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定义目标网址
# url = 'https://nba.titan007.com/1x2/oddslist/522687.htm'

# 发起GET请求获取网页内容
# response = requests.get(url)
# html = response.text
#
# # 使用BeautifulSoup解析HTML内容
# soup = BeautifulSoup(html, 'html.parser').encode("gbk")

# 找到包含数据的表格
# table = soup.find('table', class_='oddslist')
# print(soup)
# 创建存储数据的列表
# data = []
#
# # 遍历表格中的每一行
# for row in table.find_all('tr'):
#     columns = row.find_all('td')
#     if len(columns) >= 5:  # 确保每行至少有5个单元格
#         team = columns[0].text.strip()
#         home_odds = columns[2].text.strip()
#         draw_odds = columns[3].text.strip()
#         away_odds = columns[4].text.strip()
#         data.append([team, home_odds, draw_odds, away_odds])
#
# # 将数据转换为DataFrame
# df = pd.DataFrame(data, columns=['Team', 'Home Odds', 'Draw Odds', 'Away Odds'])
#
# # 将DataFrame保存为Excel文件
# excel_filename = 'nba_odds.xlsx'
# df.to_excel(excel_filename, index=False, engine='openpyxl')
#
# print(f'Data saved to {excel_filename}')
import torch
from torchvision.transforms import v2

H, W = 32, 32
img = torch.randint(0, 256, size=(3, H, W), dtype=torch.uint8)

transforms = v2.Compose([
    v2.RandomResizedCrop(size=(224, 224), antialias=True),
    v2.RandomHorizontalFlip(p=0.5),
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
img = transforms(img)
