import csv
import logging
import re
import ssl
import urllib.request as req

import ax as ax
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from datetime import datetime

from matplotlib import ticker

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://steamcommunity.com/market/listings/730/%E2%98%85%20Karambit"
logging.captureWarnings(True)
request = req.Request(url, headers={
    "User-Agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"
})
with req.urlopen(request) as response:
    HtmlText = response.read().decode("utf-8")
# print(HtmlText)

data = re.search('<script.*?line1=(.*?);.*?</script>', HtmlText, re.S)
print(data.group(1))

path = r'temp2.txt'
with open(path, 'w', encoding='utf-8') as f:
    f.write(data.group(1))

file = open(path)
file_read = file.read()

table = str.maketrans('', '', '":+[]')  # 删除字符串中的“ ： + []
file_translate = file_read.translate(table)

lst = file_translate.split(',')  # 以逗号为分隔符，将字符串转换为列表

list_time = []
list_price = []
list_num = []
# 将时间、价格、数量三个信息分别存入三个list
i = 0
j = 0
while i < len(lst):
    list_time.insert(j, lst[i])
    list_price.insert(j, lst[i + 1])
    list_num.insert(j, lst[i + 2])
    i = i + 3
    j = j + 1
# 创建csv文件，并将数据写入
with open('transaction2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['time', 'price', 'number'])
    for i in range(len(list_time)):
        writer.writerow([list_time[i], list_price[i], list_num[i]])

transaction = pd.read_csv('transaction2.csv')
transaction = transaction.sort_index()
print(transaction)

transaction = pd.read_csv('transaction2.csv')
for i in range(transaction['time'].count()):
    time_original = transaction.iloc[i, 0]
    time_format = datetime.strptime(time_original, '%b %d %Y %H %M')
    time_format = time_format.strftime('%Y/%m/%d %H:%M')
    transaction.iloc[i, 0] = time_format
print(transaction)

tmp = transaction[transaction['time'].str.contains('2022')]
transaction['time'] = pd.to_datetime(transaction['time'])
sns.set_style(style="whitegrid")
plt.title("The price trend of Karambit")
tick_spacing = 5
# plt.figure(figsize=(25, 6))
plt.plot(transaction['time'], transaction['price'], label="Karambit", color='green', linewidth=0.6)
plt.ylabel('Price ($)')
plt.xlabel('Date')
# xtick_location = transaction.index.tolist()[::200]
# xtick_labels = [x[-20:] for x in transaction['time'].tolist()[::200]]
# plt.xticks(ticks=xtick_location, labels=xtick_labels, rotation=-30, fontsize=6, horizontalalignment='center', alpha=1)
plt.xticks(fontsize=6, horizontalalignment='center', alpha=1)
plt.grid(axis='both', alpha=.3)
plt.gca().spines["top"].set_alpha(0.0)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.0)
plt.gca().spines["left"].set_alpha(0.3)
plt.legend()
plt.show()

tmp['time'] = pd.to_datetime(tmp['time'])
print(tmp)
sns.set_style(style="whitegrid")
plt.title("The price trend of Karambit in 2022")
tick_spacing = 5
# plt.figure(figsize=(25, 6))
# HERE we can exchange the index to self-defined strings of time in order to achieve user's customized check
plt.plot(tmp['time'], tmp['price'], label="Karambit", color='green', linewidth=0.6)
plt.ylabel('Price ($)')
plt.xlabel('Date')
# xtick_location = tmp['time'].tolist()[::40]
# xtick_labels = [x for x in tmp['time'].tolist()[::40]]
# plt.xticks(ticks=xtick_location, labels=xtick_labels, fontsize=6, horizontalalignment='center', alpha=1)
plt.xticks(fontsize=6, horizontalalignment='center', alpha=1)
plt.grid(axis='both', alpha=.3)
plt.gca().spines["top"].set_alpha(0.0)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.0)
plt.gca().spines["left"].set_alpha(0.3)
plt.legend()
plt.show()
