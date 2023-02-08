import csv
import logging
import re
import ssl
import urllib.request as req
import ax
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from matplotlib import ticker
import pylab
import scipy.stats as stats

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://steamcommunity.com/market/listings/730/%E2%98%85%20Bayonet"
logging.captureWarnings(True)
request = req.Request(url, headers={
    "User-Agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"
})
with req.urlopen(request) as response:
    HtmlText = response.read().decode("utf-8")
# print(HtmlText)

data = re.search('<script.*?line1=(.*?);.*?</script>', HtmlText, re.S)
print(data.group(1))

path = r'temp.txt'
with open(path, 'w', encoding='utf-8') as f:
    f.write(data.group(1))

file = open(path)
file_read = file.read()

table = str.maketrans('', '', '":+[]')
file_translate = file_read.translate(table)
lst = file_translate.split(',')
list_time = []
list_price = []
list_num = []
i = 0
j = 0
while i < len(lst):
    list_time.insert(j, lst[i])
    list_price.insert(j, lst[i + 1])
    list_num.insert(j, lst[i + 2])
    i = i + 3
    j = j + 1
with open('transaction.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['time', 'price', 'number'])
    for i in range(len(list_time)):
        writer.writerow([list_time[i], list_price[i], list_num[i]])

transaction = pd.read_csv('transaction.csv')
transaction = transaction.sort_index()
print(transaction)

transaction = pd.read_csv('transaction.csv')
for i in range(transaction['time'].count()):
    time_original = transaction.iloc[i, 0]
    time_format = datetime.strptime(time_original, '%b %d %Y %H %M')
    time_format = time_format.strftime('%Y/%m/%d %H:%M')
    transaction.iloc[i, 0] = time_format
print(transaction)

tmp = transaction[transaction['time'].str.contains('2022')]
tmp13 = transaction[transaction['time'].str.contains('2013')]
tmp14 = transaction[transaction['time'].str.contains('2014')]
tmp15 = transaction[transaction['time'].str.contains('2015')]
tmp16 = transaction[transaction['time'].str.contains('2016')]
tmp17 = transaction[transaction['time'].str.contains('2017')]
tmp18 = transaction[transaction['time'].str.contains('2018')]
tmp19 = transaction[transaction['time'].str.contains('2019')]
tmp20 = transaction[transaction['time'].str.contains('2020')]
tmp21 = transaction[transaction['time'].str.contains('2021')]

tmp1 = transaction[transaction['time'].str.contains('2022/01')]
tmp2 = transaction[transaction['time'].str.contains('2022/02')]
tmp3 = transaction[transaction['time'].str.contains('2022/03')]
tmp4 = transaction[transaction['time'].str.contains('2022/04')]
tmp5 = transaction[transaction['time'].str.contains('2022/05')]
tmp6 = transaction[transaction['time'].str.contains('2022/06')]
tmp7 = transaction[transaction['time'].str.contains('2022/07')]
tmp8 = transaction[transaction['time'].str.contains('2022/08')]
tmp9 = transaction[transaction['time'].str.contains('2022/09')]
tmp10 = transaction[transaction['time'].str.contains('2022/10')]
tmp11 = transaction[transaction['time'].str.contains('2022/11')]

transaction['time'] = pd.to_datetime(transaction['time'])  # HERE convert to datetime type
sns.set_style(style="whitegrid")
plt.title("The price trend of Bayonet")
tick_spacing = 5
# plt.figure(figsize=(25, 6))
plt.plot(transaction['time'], transaction['price'], label="Bayonet", color='r', linewidth=0.6)
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

plt.scatter(transaction['price'], transaction['number'], s=1)
plt.xlabel("Price")
plt.ylabel("Number")
plt.title(stats.pearsonr(transaction['number'], transaction['price']))
pylab.show()

# 0.05
print(stats.pearsonr(transaction['number'], transaction['price']))

number2013 = 0
for i in tmp13['number']:
    number2013 = number2013 + i
print(number2013)

number2014 = 0
for i in tmp14['number']:
    number2014 = number2014 + i
print(number2014)

number2015 = 0
for i in tmp15['number']:
    number2015 = number2015 + i
print(number2015)

number2016 = 0
for i in tmp16['number']:
    number2016 = number2016 + i
print(number2016)

number2017 = 0
for i in tmp17['number']:
    number2017 = number2017 + i
print(number2017)

number2018 = 0
for i in tmp18['number']:
    number2018 = number2018 + i
print(number2018)

number2019 = 0
for i in tmp19['number']:
    number2019 = number2019 + i
print(number2019)

number2020 = 0
for i in tmp20['number']:
    number2020 = number2020 + i
print(number2020)

number2021 = 0
for i in tmp21['number']:
    number2021 = number2021 + i
print(number2021)

number2022 = 0
for i in tmp['number']:
    number2022 = number2022 + i
print(number2022)

timeline = ('2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022')
buy_number = [number2013, number2014, number2015, number2016, number2017, number2018, number2019, number2020, number2021, number2022]
plt.bar(timeline, buy_number)
plt.ylabel('Number')
plt.xlabel('Year')
plt.title('Transaction number')
plt.show()

tmp['time'] = pd.to_datetime(tmp['time'])
print(tmp)
sns.set_style(style="whitegrid")
plt.title("The price trend of Bayonet in 2022")
tick_spacing = 5
# plt.figure(figsize=(25, 6))
plt.plot(tmp['time'], tmp['price'], label="Bayonet", color='r', linewidth=0.6)
# HERE we can exchange the index to self-defined strings of time in order to achieve user's customized check
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

number1 = 0
for i in tmp1['number']:
    number1 = number1 + i
print(number1)

number2 = 0
for i in tmp2['number']:
    number2 = number2 + i
print(number2)

number3 = 0
for i in tmp3['number']:
    number3 = number3 + i
print(number3)

number4 = 0
for i in tmp4['number']:
    number4 = number4 + i
print(number4)

number5 = 0
for i in tmp5['number']:
    number5 = number5 + i
print(number5)

number6 = 0
for i in tmp6['number']:
    number6 = number6 + i
print(number6)

number7 = 0
for i in tmp7['number']:
    number7 = number7 + i
print(number7)

number8 = 0
for i in tmp8['number']:
    number8 = number8 + i
print(number8)

number9 = 0
for i in tmp9['number']:
    number9 = number9 + i
print(number9)

number10 = 0
for i in tmp10['number']:
    number10 = number10 + i
print(number10)

number11 = 0
for i in tmp11['number']:
    number11 = number11 + i
print(number11)

timeline = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11')
buy_number = [number1, number2, number3, number4, number5, number6, number7, number8, number9, number10, number11]
plt.bar(timeline, buy_number)
plt.ylabel('Number')
plt.xlabel('Month')
plt.title('Transaction number in 2022')
plt.show()
