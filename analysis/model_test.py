# coding=utf-8
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import anlay_haha
# 读取数据
# data = pd.read_csv('betting_data.csv')
# xls = pd.ExcelFile('2024-7-10 WNBA 洛杉矶火花 VS 明尼苏达天猫.xls')

data = anlay_haha.data
print(data)
# 提取特征和目标变量
X = data.drop(['序号', '赛果'], axis=1)
y = data['赛果']
# # 划分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # 创建逻辑回归模型
# model = LogisticRegression()
# # 训练模型
# model.fit(X_train, y_train)
# # 预测
# y_pred = model.predict(X_test)
# # 评估模型
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)
# print(classification_report(y_test, y_pred))