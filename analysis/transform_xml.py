# coding=utf-8

from bs4 import BeautifulSoup
import control_all
def clean_data(value):
    # 去除空格和其他非数字字符
    value = value.replace(' ', '').replace(',', '')
    return value

# 读取HTML文件
# with open('2023-7-12 WNBA 芝加哥天空 VS 康涅狄克太阳.xls', 'r') as file:  # taiyang
# with open(u'2023-7-13 WNBA 洛杉矶火花 VS 拉斯维加斯王牌.xls', 'r') as file:  # wang
# with open(u'2023-7-13 WNBA 明尼苏达天猫 VS 达拉斯飞翼.xls', 'r') as file:         # fei
# with open(u'2023-7-13 WNBA 亚特兰大梦想 VS 西雅图风暴.xls', 'r') as file:     #  meng




# name = control_all.analy_name
def clear_num(name):
    with open(name, 'r') as file:
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
    return data
# 打印数据
# for row in data:
#     print(row)
# print(data)

# if __name__ == '__main__':
#     clear_num()

# import os
# os.rename(u"2023-7-12 WNBA 芝加哥天空 VS 康涅狄克太阳.xml",
#  u"2023-7-12 WNBA 芝加哥天空 VS 康涅狄克太阳.xls")