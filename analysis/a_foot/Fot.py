# coding=utf-8
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt





from bs4 import BeautifulSoup
def clean_data(value):
    # 去除空格和其他非数字字符
    value = value.replace(' ', '').replace(',', '')
    return value


# with open(u'2024-7-7 瑞典超 加爾斯 VS 哈馬比.xls', 'r') as file:  # 平局 p-v  二大   std 小  小小  32  高
# with open(u'2024-7-7 瑞典超 馬模 VS 咸史泰斯.xls', 'r') as file:  # 马默  p-v 小   std 大  大大  502.48  二高
# with open(u'2024-7-7 瑞典超 華納莫 VS 哥登堡.xls', 'r') as file:  # 华纳莫  p-v大   std 二大  二大大  -37.23   低
# with open(u'2024-7-7 瑞典超 AIK蘇納 VS 卡馬亞.xls', 'r') as file:  # 卡玛尔  p-v小  std 小 小小  241.59   高

# with open(u'2024-7-9 瑞典超 諾高平 VS 佐加頓斯.xls', 'r') as file:  # 佐加顿斯  p-v二大 std 大 大大 -155.67 -156.55    二高
# with open(u'2024-7-16 瑞典超 哈馬比 VS 哥登堡.xls', 'r') as file:  # 佐加顿斯  p-v二大 std 大 大大 167.79   二高
# with open(u'2024-7-24 歐冠盃 盧加諾 VS 費倫巴治.xls', 'r') as file:  # 费伦巴治 p-v小 std 大 大大 -54.93  高

# with open(u'2024-7-26 韓K聯 濟州聯 VS 蔚山現代.xls', 'r') as file:  # 佐加顿斯  p-v二大 std 大 大大 -83.86  二高
# with open(u'2024-7-30 瑞典超 AIK蘇納 VS 加爾斯.xls', 'r') as file:  # 加热丝  p-v小 std 二大 二大大 98.36  二高 下降最多
with open(u'2024-7-31 奧運女足 巴西女足 VS 西班牙女足.xls', 'r') as file:  # 加热丝  p-v小 std 二大 二大大 -105.88   二高












# with open(u'2023-9-8 歐洲盃 塞爾維亞 VS 、匈牙利.xls', 'r') as file:  # 匈牙利  p-v  二大   std 二大  小小   229
# with open(u'2023-9-8 歐洲盃 格魯吉亞 VS 西班牙.xls', 'r') as file:  # 西班牙  p-v  小   std 大  大大  -403
# with open(u'2023-9-9 歐洲盃 盧森堡 VS 冰島.xls', 'r') as file:  # 卢森堡  p-v  小   std 大  二大大  -15
# with open(u'2023-9-9 歐洲盃 斯洛伐克 VS 葡萄牙.xls', 'r') as file:  # 葡萄 p-v  小   std 大  大大  -254
# with open(u'2023-9-9 歐洲盃 克羅地亞 VS 拉脫維亞.xls', 'r') as file:  # 克罗地亚  p-v  大   std 大  大大  516
# with open(u'2023-9-9 歐洲盃 塞浦路斯 VS 蘇格蘭.xls', 'r') as file:  # 克罗地亚  p-v 小   std 大  大大  -272
# with open(u'2023-9-8 歐洲盃 荷蘭 VS 希臘.xls', 'r') as file:  # 荷兰  p-v 小   std 大  大大  354
# with open(u'2023-9-8 南美預選 哥倫比亞 VS 委内瑞拉.xls', 'r') as file:  # 哥伦比亚  p-v 小   std 大  大大  242
# with open(u'2023-9-8 南美預選 阿根廷 VS 厄瓜多爾.xls', 'r') as file:  # 哥伦比亚  p-v 小   std 大  大大  242
# with open(u'2023-9-9 歐洲盃 土耳其 VS 阿美尼亞.xls', 'r') as file:  # 平  p-v 小   std 二大  二大大  366

# with open(u'2023-9-9 日職乙 長崎成功丸 VS 草津溫泉.xls', 'r') as file:  # +1平  p-v 小   std 小  二大大  129
# with open(u'2023-9-9 日職乙 岡山綠雉 VS 仙台維加泰.xls', 'r') as file:  # +1平  p-v 二大   std 小  小小  92
# with open(u'2023-9-9 國際友誼 中國 VS 馬來西亞.xls', 'r') as file:  # 马来西亚  p-v 小   std 二大  小小  183
# with open(u'2023-9-9 歐洲盃 阿塞拜疆 VS 比利時.xls', 'r') as file:  # 阿塞拜疆 p-v 小   std 二大 小小  -449
# with open(u'2023-9-9 英甲 史提芬納治 VS 卡素爾.xls', 'r') as file:  #  卡速二 p-v 二大   std 二 大  小小 165
# with open(u'2023-9-9 英甲 埃克塞特 VS 奧連特.xls', 'r') as file:  # 奥联特 p-v 大   std 二大  小小  145
# with open(u'2023-9-9 荷乙 泰斯達 VS 芬洛.xls', 'r') as file:  #  芬洛 p-v 大   std 二大  二大大  33
# with open(u'2023-9-9 歐洲盃 烏克蘭 VS 英格蘭.xls', 'r') as file:  # 乌克兰 p-v 大  std 小  小小  -271
# with open(u'2023-9-9 歐洲盃 愛沙尼亞 VS 瑞典.xls', 'r') as file:  # 瑞典 p-v 大  std 大  大大  -239

# with open(u'2023-9-10 歐洲盃 哈薩克 VS 北愛爾蘭.xls', 'r') as file:  # 哈萨克  p-v 二大   std 二大  二大大  -1.59
# with open(u'2023-9-10 歐洲盃 芬蘭 VS 丹麥.xls', 'r') as file:  # +1平  p-v 二大   std 小  二大大  -194
# with open(u'2023-9-10 歐洲盃 黑山 VS 保加利亞.xls', 'r') as file:  # +1平  p-v 大   std 小  二大大  70
# with open(u'2023-9-11 歐洲盃 阿爾巴尼亞 VS 波蘭.xls', 'r') as file:  # 阿尔巴尼亚 p-v 小  std 二大  小小 -95
# with open(u'2023-9-11 歐洲盃 愛爾蘭 VS 荷蘭.xls', 'r') as file:  # +1平 p-v 小  std 小  二大大  -145
# with open(u'2023-9-11 歐洲盃 阿美尼亞 VS 克羅地亞.xls', 'r') as file:  # +1平 p-v 小  std 二大  二大大  -370
# with open(u'2023-9-12 歐洲盃 葡萄牙 VS 盧森堡.xls', 'r') as file:  # 葡萄牙 p-v 二大  std 二大  大大  694
# with open(u'2023-9-12 歐洲盃 冰島 VS 波斯尼亞.xls', 'r') as file:  # 冰岛 p-v 小  std 二大  二大大  -7
# with open(u'2023-9-13 歐洲盃 意大利 VS 烏克蘭.xls', 'r') as file:  #  p-v 小  std 小  二大大  -7
# with open(u'2023-9-13 歐洲盃 羅馬尼亞 VS 科索沃.xls', 'r') as file:  #  p-v 小  std 小  二大大  -7
# with open(u'2023-9-13 歐洲盃 以色列 VS 白俄羅斯.xls', 'r') as file:  #  p-v 小  std 小  二大大  -7
# with open(u'2023-9-13 歐洲盃 瑞典 VS 奧地利.xls', 'r') as file:  #  p-v 小  std 小  二大大 62


# with open(u'2023-9-23 日職聯 新潟天鵝 VS FC橫濱.xls', 'r') as file:  #  天鹅 p-v 二大  std 大  大大 174
# with open(u'2023-9-23 日職聯 名古屋八鯨 VS 札幌岡薩多.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 174
# with open(u'2023-9-23 日職聯 神戶勝利船 VS 大阪櫻花.xls', 'r') as file:  #  -1 平 # p-v 二大  std 小  小小 98
# with open(u'2023-9-23 德乙 格雷特霍夫 VS 卡斯魯厄.xls', 'r') as file:  #  -1 平  p-v 二大 std 小 小小 80
# with open(u'2023-9-23 瑞典超 迪加科斯 VS 馬模.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 174
# with open(u'2023-9-23 意甲 AC米蘭 VS 維羅納.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 174
# with open(u'2023-9-23 德甲 多蒙特 VS 沃爾夫斯堡.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 174
# with open(u'2023-9-23 英冠 列斯聯 VS 屈福特.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 193
# with open(u'2023-9-24 法乙 阿些斯奧 VS 巴黎FC.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 193
# with open(u'2023-9-24 英超 般尼 VS 曼聯.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 193
# with open(u'2023-9-23 英冠 李斯特城 VS 布里斯托城.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 193
# with open(u'2023-9-23 意甲 莎索羅 VS 祖雲達斯.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 193
# with open(u'2023-9-25 巴西盃 聖保羅 VS 法林明高.xls', 'r') as file:  #  札幌 # p-v 小  std 二大  二大大 193

# with open(u'2023-9-24 亞運男足 泰國U23 VS 科威特U23.xls', 'r') as file:  #  科威特 # p-v 大 std 二大  小小 193
# with open(u'2023-9-24 亞運男足 越南U23 VS 沙特阿拉伯U23.xls', 'r') as file:  #  沙特 # p-v 大 std 大 大大 -126
# with open(u'2023-9-24 亞運男足 南韓U23 VS 巴林U23.xls', 'r') as file:  # +3 平 # p-v 大 std 小 二大大 148
# with open(u'2023-9-24 亞運男足 中國U23 VS 孟加拉U23.xls', 'r') as file:  # 孟加拉 # p-v 二大 std 二大 小小 619
# with open(u'2023-9-25 亞運男足 烏茲別克U23 VS 中國香港U23.xls', 'r') as file:  # 香港 # p-v 二大 std 二大 小小 280
# with open(u'2023-9-25 亞運男足 巴勒斯坦U23 VS 日本U23.xls', 'r') as file:  #巴勒斯坦 # p-v 小 std 大 二大大 258
# with open(u'2023-9-26 瑞典超 咸史泰斯 VS 艾夫斯堡.xls', 'r') as file:  #+1 ping # p-v 二大 std 小 二大大 -178
# with open(u'2023-9-26 葡超 士砵亭 VS 里奧阿維.xls', 'r') as file:  #+2 ping # p-v 小 std 二大 二大大 412
# with open(u'2023-9-27 西甲 西維爾 VS 艾美利亞.xls', 'r') as file:  #+2 ping # p-v 小 std 二大 二大大 412
# with open(u'2023-9-27 意甲 祖雲達斯 VS 萊切.xls', 'r') as file:  #+2 ping # p-v 小 std 二大 二大大 412
# with open(u'2023-9-27 英聯盃 曼聯 VS 水晶宮.xls', 'r') as file:  #+2 ping # p-v 小 std 二大 二大大 412
# with open(u'2023-9-27 法甲 利爾 VS 蘭斯.xls', 'r') as file:  #+2 ping # p-v 小 std 二大 二大大 412
# with open(u'2023-9-27 西甲 馬略卡 VS 巴塞隆拿.xls', 'r') as file:  #+2 ping # p-v 小 std 二大 二大大 -208

# with open(u'2023-10-12 歐洲盃 拉脫維亞 VS 阿美尼亞.xls', 'r') as file:  # 拉脱维亚 # p-v 大 std 二大 小小 -108
# with open(u'2023-10-13 歐洲盃 克羅地亞 VS 土耳其.xls', 'r') as file:  # 土耳其 # p-v 二大 std 二大 小小 223
# with open(u'2023-10-13 歐洲盃 塞浦路斯 VS 挪威.xls', 'r') as file:  # 挪威 # p-v 小 std 大 大大 -238 忽略
# with open(u'2023-10-13 歐洲盃 西班牙 VS 蘇格蘭.xls', 'r') as file:  # +2 平 # p-v 小 std 小 二大大 324 忽略
# with open(u'2023-10-13 國際友誼 南韓 VS 突尼西亞.xls', 'r') as file:  # 南韩  # p-v二大 std 大 大大 155
# with open(u'2023-10-13 歐洲盃 愛沙尼亞 VS 阿塞拜疆.xls', 'r') as file:  # 阿塞拜疆  # p-v二大 std 二大 小小 94
# with open(u'2023-10-13 國際友誼 日本 VS 加拿大.xls', 'r') as file:  # 日本  # p-v小 std 大 大大 94
# with open(u'2023-10-14 歐洲盃 冰島 VS 盧森堡.xls', 'r') as file:  # 卢森堡  # p-v大 std二大 小小 215
# with open(u'2023-10-14 歐洲盃 奧地利 VS 比利時.xls', 'r') as file:  # 比利时  # p-v小 std大 二大大 25
# with open(u'2023-10-14 歐洲盃 愛爾蘭 VS 希臘.xls', 'r') as file:  # 希腊  # p-v大 std大 小小 43
# with open(u'2023-10-14 歐洲盃 荷蘭 VS 法國.xls', 'r') as file:  # +1平  # p-v小 std小 小小 -18
# with open(u'2023-10-16 歐洲盃 波蘭 VS 摩爾多瓦.xls', 'r') as file:  # 摩尔多瓦  # p-v小 std小 二大大 389.52  高
# with open(u'2023-10-16 歐洲盃 威爾斯 VS 克羅地亞.xls', 'r') as file:  # 主  # p-v大 std大 小小 -99.85  高
# with open(u'2023-10-16 歐洲盃 土耳其 VS 拉脫維亞.xls', 'r') as file:  # 主  # p-v小 std大 大大 490.22  高
# with open(u'2023-10-16 歐洲盃 挪威 VS 西班牙.xls', 'r') as file:  # +1平  # p-v大 std小 二大大 -103.29 高
# with open(u'2023-10-17 歐洲盃 波斯尼亞 VS 葡萄牙.xls', 'r') as file:  #   # p-v大 std小 二大大 -206 高
# with open(u'2023-10-17 歐洲盃 比利時 VS 瑞典.xls', 'r') as file:  #  瑞典 # p-v小 std二大 小小 256 高
# with open(u'2023-10-17 歐洲盃 希臘 VS 荷蘭.xls', 'r') as file:  #  希腊 # p-v小 std二大 小小 -72 高
# with open(u'2023-10-15 歐洲盃 匈牙利 VS 塞爾維亞.xls', 'r') as file:  # 主  # p-v大 std大 大大 25 低

# with open(u'2023-10-22 德乙 卡斯魯厄 VS 史浩克零四.xls', 'r') as file:  # 主  # p-v大 std大 大大 53 低
# with open(u'2023-10-22 德乙 紐倫堡 VS 哈化柏林.xls', 'r') as file:  # 主  # p-v小 std小 二大大 -24 低
# with open(u'2023-10-22 挪超 利尼史特朗 VS 華拿倫加.xls', 'r') as file:  # 主  # p-v小 std大 大大 70 低
#
# with open(u'2023-10-22 意甲 博洛尼亞 VS 費辛隆尼.xls', 'r') as file:  # +1平# p-v小 std大 大大 234 高
# with open(u'2023-10-23 意甲 AC米蘭 VS 祖雲達斯.xls', 'r') as file:  # 客 # p-v大 std二大 小小 88.93 高
# with open(u'2023-10-22 英超 阿士東維拉 VS 韋斯咸.xls', 'r') as file:  # 主 # p-v小 std大 大大 105 高
# with open(u'2023-10-22 意甲 羅馬 VS 莫沙.xls', 'r') as file:  # +1平  # p-v二大 std小 二大大 266 低

# with open(u'2023-10-24 意甲 烏甸尼斯 VS 萊切.xls', 'r') as file:  # 客  # p-v二大 std小 二大大 123 低
# with open(u'2023-10-24 英超 熱刺 VS 富咸.xls', 'r') as file:  # 主  # p-v二大 std打 二大大 310 低
# with open(u'2023-10-23 亞冠盃 伊蒂哈德 VS 巴格達空軍.xls', 'r') as file:  # 客  # p-v大 std小 小小 258 高
# with open(u'2023-10-24 亞冠盃 希拉爾 VS 孟買城.xls', 'r') as file:  # 主  # p-v小 std小 大大 640 高
# with open(u'2023-10-24 亞冠盃 浦和紅鑽 VS 浦項制鐵.xls', 'r') as file:  # 主  # p-v小 std小 大大 152 高
# with open(u'2023-10-24 亞冠盃 武漢三鎮 VS TT河內.xls', 'r') as file:  # 主  # p-v小 std小 大大 189 高

# with open(u'2023-10-22 西甲 傑羅納 VS 艾美利亞.xls', 'r') as file:  # 主  # p-v小 std大 大大 169 二高
# with open(u'2023-10-23 西甲 巴塞隆拿 VS 畢爾包.xls', 'r') as file:  # +1平 # p-v小 std小 二大大 199 高
# with open(u'2023-10-24 西甲 華倫西亞 VS 卡迪斯.xls', 'r') as file:  # +1平 # p-v小 std小 二大大 170 高


# with open(u'2024-1-12 亞洲盃 卡塔爾 VS 黎巴嫩.xls', 'r') as file:  # +主 # p-v大 std大 大大 163 二高
# with open(u'2024-1-13 亞洲盃 澳洲 VS 印度.xls', 'r') as file:  # +2平 # p-v大 std大 二大大 593 二高
# with open(u'2024-1-13 亞洲盃 中國 VS 塔吉克斯坦.xls', 'r') as file:  # 平 # p-v大 std小 二大大 79 低
# with open(u'2024-1-14 亞洲盃 日本 VS 越南.xls', 'r') as file:  # 客 # p-v二大 std二大 小小 623  二高
# with open(u'2024-1-14 亞洲盃 阿聯酋 VS 中國香港.xls', 'r') as file:  # 主 # p-v大 std大 大大 290.9  二高

# with open(u'2024-1-15 亞洲盃 南韓 VS 巴林.xls', 'r') as file:  # +2平 # p-v二大 std小 二大大 364 低
# with open(u'2024-1-16 亞洲盃 馬來西亞 VS 約旦.xls', 'r') as file:  # 客 # p-v小 std大 大大 -162 二高
# with open(u'2024-1-15 亞洲盃 印尼 VS 伊拉克.xls', 'r') as file:  # 客 # p-v大 std大 大大 -212 低
# with open(u'2024-1-16 亞洲盃 泰國 VS 吉爾吉斯坦.xls', 'r') as file:  # 主 # p-v二大 std大 大大 52 高
# with open(u'2024-1-17 亞洲盃 沙地阿拉伯 VS 阿曼.xls', 'r') as file:  # +1平 # p-v小 std小 二大大 163 二高
# with open(u'2024-1-17 亞洲盃 黎巴嫩 VS 中國.xls', 'r') as file:  # +1平 # p-v小 std小 二大大 -39.64 二高









# with open(u'2024-6-15 歐洲盃 德國 VS 蘇格蘭.xls', 'r', errors='ignore') as file:  # 德国 # p-v小 std大  大大 435 二高
# with open(u'2024-6-15 歐洲盃 匈牙利 VS 瑞士.xls', 'r', errors='ignore') as file:  # 瑞士 # p-v二大 std二大  大大 -45  -57 高
# with open(u'2024-6-15 歐洲盃 西班牙 VS 克羅地亞.xls', 'r', errors='ignore') as file:  # 西班牙 # p-v二大 std大  大大 168.37   高

# with open(u'2024-6-17 歐洲盃 羅馬尼亞 VS 烏克蘭.xls', 'r', errors='ignore') as file:  # 罗马尼亚 # p-v大 std二大   小小 -70  二高
# with open(u'2024-6-18 歐洲盃 奧地利 VS 法國.xls', 'r', errors='ignore') as file:  # 法国 # p-v二大 std大  大大 -248  高
# with open(u'2024-6-17 歐洲盃 比利時 VS 斯洛伐克.xls', 'r', errors='ignore') as file:  # 斯洛伐克 # p-v小 std小  小小 198  低

# with open(u'2024-6-19 日職聯 橫濱水手 VS 廣島三箭.xls', 'r', errors='ignore') as file:  # 横滨水手 # p-v小 std二大 二大大  -166.55  高
# with open(u'2024-7-3 日職聯 橫濱水手 VS 鳥栖沙岩.xls', 'r', errors='ignore') as file:  # 客队 # p-v二大 std小  小小 260.16   二高
# with open(u'2024-7-5 日職聯 廣島三箭 VS 神戶勝利船.xls', 'r', errors='ignore') as file:  # 平局 # p-v二大 std小  小小 80.98   二高
# with open(u'2024-7-5 韓K聯 仁川聯 VS 金泉尚武.xls', 'r', errors='ignore') as file:  # 仁川  # p-v二大 std小  小小 16.0   二高
# with open(u'2024-7-9 韓K聯 金泉尚武 VS 水原.xls', 'r', errors='ignore') as file:  #水源  # p-v大 std小  二大大 114.98  低
# with open(u'2024-7-10 韓K聯 浦項制鐵 VS FC江原.xls', 'r', errors='ignore') as file:  #主队  # p-v二大 std大  大大 175.02  二高
# with open(u'2024-7-13 韓K聯 蔚山現代 VS FC首爾.xls', 'r', errors='ignore') as file:  #水源  # p-v大 std小  二大大 110.03 低





# with open(u'2024-6-25 歐洲盃 克羅地亞 VS 意大利.xls', 'r', errors='ignore') as file:  # 平局 # p-v大  std小  二大 -166.55  高
# with open(u'2024-6-25 歐洲盃 荷蘭 VS 奧地利.xls', 'r', errors='ignore') as file:  # 奥地利 # p-v大 std小  二大  80.1  低
# with open(u'2024-6-26 日職聯 福岡黃蜂 VS 橫濱水手.xls', 'r', errors='ignore') as file:  # 福冈 # p-v大 std小  二大 -16.95   低
# with open(u'2024-6-26 歐洲盃 烏克蘭 VS 比利時.xls', 'r', errors='ignore') as file:  #平局  # p-v大 std小  二大 -120.78  低
# with open(u'2024-6-28 美洲盃 巴拿馬 VS 美國.xls', 'r', errors='ignore') as file:  # 巴拿马 # p-v大 std小  小小  -292.79  低
# with open(u'2024-6-29 美洲盃 巴拉圭 VS 巴西.xls', 'r', errors='ignore') as file:  # 巴西 # p-v小 std大  大大  -356.55   高
# with open(u'2024-6-29 美洲盃 哥倫比亞 VS 哥斯達黎加.xls', 'r', errors='ignore') as file:  # 哥伦比亚 # p-v小 std大  大大  196.53 高
# with open(u'2024-7-2 美洲盃 美國 VS 烏拉圭.xls', 'r', errors='ignore') as file:  # 乌拉圭  # p-v大 std二大  大大  -5.07 高
# with open(u'2024-7-5 美洲盃 阿根廷 VS 厄瓜多爾.xls', 'r', errors='ignore') as file:  # 哥伦比亚 # p-v小 std大  大大  302 高


# with open(u'2024-6-27 歐洲盃 捷克 VS 土耳其.xls', 'r', errors='ignore') as file:  # 土耳其  # p-v二大 std二大  大大 -19.02  二高
# with open(u'2024-7-1 歐洲盃 法國 VS 比利時.xls', 'r', errors='ignore') as file:  # 法国  # p-v大 std二大  大大 153.87   低
# with open(u'2024-7-2 歐洲盃 葡萄牙 VS 斯洛文尼亞.xls', 'r', errors='ignore') as file:  # 平  # p-v二大 std二大  大大 421   二高
# with open(u'2024-7-2 歐洲盃 羅馬尼亞 VS 荷蘭.xls', 'r', errors='ignore') as file:  # 荷兰 # p-v二大 std大  大大 -274   二高
# with open(u'2024-7-3 歐洲盃 奧地利 VS 土耳其.xls', 'r', errors='ignore') as file:  # 土耳其  # p-v大 std二大  小小 146   二高
# with open(u'2024-7-5 歐洲盃 西班牙 VS 德國.xls', 'r', errors='ignore') as file:  # 平  # p-v二大 std小  小小 20.84    二高
# with open(u'2024-7-6 歐洲盃 葡萄牙 VS 法國.xls', 'r', errors='ignore') as file:  # 平  # p-v二大 std二大  二大大  -84.41    二高
# with open(u'2024-7-10 歐洲盃 西班牙 VS 法國.xls', 'r', errors='ignore') as file:  # 西班牙  # p-v小 std大  大大 30.78    二高
# with open(u'2024-7-11 歐洲盃 荷蘭 VS 英格蘭.xls', 'r', errors='ignore') as file:  # 西班牙  # p-v小 std大  大大 -43.06     二高

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
