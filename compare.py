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

transaction = pd.read_csv('transaction.csv')
transaction = transaction.sort_index()
print(transaction)

transaction2 = pd.read_csv('transaction2.csv')
transaction2 = transaction2.sort_index()
print(transaction2)

transaction = pd.read_csv('transaction.csv')
for i in range(transaction['time'].count()):
    time_original = transaction.iloc[i, 0]
    time_format = datetime.strptime(time_original, '%b %d %Y %H %M')
    time_format = time_format.strftime('%Y/%m/%d %H:%M')
    transaction.iloc[i, 0] = time_format
print(transaction)

transaction2 = pd.read_csv('transaction2.csv')
for i in range(transaction2['time'].count()):
    time_original2 = transaction2.iloc[i, 0]
    time_format2 = datetime.strptime(time_original2, '%b %d %Y %H %M')
    time_format2 = time_format2.strftime('%Y/%m/%d %H:%M')
    transaction2.iloc[i, 0] = time_format2
print(transaction2)

atmp1 = transaction[transaction['time'].str.contains('2022/01')]
atmp2 = transaction[transaction['time'].str.contains('2022/02')]
atmp3 = transaction[transaction['time'].str.contains('2022/03')]
atmp4 = transaction[transaction['time'].str.contains('2022/04')]
atmp5 = transaction[transaction['time'].str.contains('2022/05')]
atmp6 = transaction[transaction['time'].str.contains('2022/06')]
atmp7 = transaction[transaction['time'].str.contains('2022/07')]
atmp8 = transaction[transaction['time'].str.contains('2022/08')]
atmp9 = transaction[transaction['time'].str.contains('2022/09')]
atmp10 = transaction[transaction['time'].str.contains('2022/10')]
atmp11 = transaction[transaction['time'].str.contains('2022/11')]

btmp1 = transaction2[transaction2['time'].str.contains('2022/01')]
btmp2 = transaction2[transaction2['time'].str.contains('2022/02')]
btmp3 = transaction2[transaction2['time'].str.contains('2022/03')]
btmp4 = transaction2[transaction2['time'].str.contains('2022/04')]
btmp5 = transaction2[transaction2['time'].str.contains('2022/05')]
btmp6 = transaction2[transaction2['time'].str.contains('2022/06')]
btmp7 = transaction2[transaction2['time'].str.contains('2022/07')]
btmp8 = transaction2[transaction2['time'].str.contains('2022/08')]
btmp9 = transaction2[transaction2['time'].str.contains('2022/09')]
btmp10 = transaction2[transaction2['time'].str.contains('2022/10')]
btmp11 = transaction2[transaction2['time'].str.contains('2022/11')]

tmp = transaction[transaction['time'].str.contains('2022')]
tmp2 = transaction2[transaction2['time'].str.contains('2022')]
# transaction3 = pd.concat([transaction, transaction2], axis=0, ignore_index=True)
# print(transaction3)
transaction['time'] = pd.to_datetime(transaction['time'])
transaction2['time'] = pd.to_datetime(transaction2['time'])
sns.set_style(style="whitegrid")
plt.title("The price trend of Bayonet and Karambit")
tick_spacing = 5
# plt.figure(figsize=(25, 6))
plt.plot(transaction['time'], transaction['price'], label="Bayonet", color='r', linewidth=0.6)
plt.plot(transaction2['time'], transaction2['price'], label="Karambit", color='green', linewidth=0.6)
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
tmp2['time'] = pd.to_datetime(tmp2['time'])
print(tmp)
print(tmp2)
sns.set_style(style="whitegrid")
plt.title("The price trend of Bayonet and Karambit in 2022")
tick_spacing = 5
# plt.figure(figsize=(25, 6))
# HERE we can exchange the index to self-defined strings of time in order to achieve user's customized check
plt.plot(tmp['time'], tmp['price'], label="Bayonet", color='r', linewidth=0.6)
plt.plot(tmp2['time'], tmp2['price'], label="Karambit", color='green', linewidth=0.6)
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
for i in atmp1['number']:
    number1 = number1 + i
print(number1)

number2 = 0
for i in atmp2['number']:
    number2 = number2 + i
print(number2)

number3 = 0
for i in atmp3['number']:
    number3 = number3 + i
print(number3)

number4 = 0
for i in atmp4['number']:
    number4 = number4 + i
print(number4)

number5 = 0
for i in atmp5['number']:
    number5 = number5 + i
print(number5)

number6 = 0
for i in atmp6['number']:
    number6 = number6 + i
print(number6)

number7 = 0
for i in atmp7['number']:
    number7 = number7 + i
print(number7)

number8 = 0
for i in atmp8['number']:
    number8 = number8 + i
print(number8)

number9 = 0
for i in atmp9['number']:
    number9 = number9 + i
print(number9)

number10 = 0
for i in atmp10['number']:
    number10 = number10 + i
print(number10)

number11 = 0
for i in atmp11['number']:
    number11 = number11 + i
print(number11)

bnumber1 = 0
for i in btmp1['number']:
    bnumber1 = bnumber1 + i
print(bnumber1)

bnumber2 = 0
for i in btmp2['number']:
    bnumber2 = bnumber2 + i
print(bnumber2)

bnumber3 = 0
for i in btmp3['number']:
    bnumber3 = bnumber3 + i
print(bnumber3)

bnumber4 = 0
for i in btmp4['number']:
    bnumber4 = bnumber4 + i
print(bnumber4)

bnumber5 = 0
for i in btmp5['number']:
    bnumber5 = bnumber5 + i
print(bnumber5)

bnumber6 = 0
for i in btmp6['number']:
    bnumber6 = bnumber6 + i
print(bnumber6)

bnumber7 = 0
for i in btmp7['number']:
    bumber7 = number7 + i
print(number7)

bnumber8 = 0
for i in btmp8['number']:
    bnumber8 = bnumber8 + i
print(bnumber8)

bnumber9 = 0
for i in btmp9['number']:
    bnumber9 = bnumber9 + i
print(bnumber9)

bnumber10 = 0
for i in btmp10['number']:
    bnumber10 = bnumber10 + i
print(bnumber10)

bnumber11 = 0
for i in btmp11['number']:
    bnumber11 = bnumber11 + i
print(bnumber11)

timeline = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
timeline2 = (1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2, 11.2)
buy_number = [number1, number2, number3, number4, number5, number6, number7, number8, number9, number10, number11]
buy_number2 = [bnumber1, bnumber2, bnumber3, bnumber4, bnumber5, bnumber6, bnumber7, bnumber8, bnumber9, bnumber10, bnumber11]
index = np.arange(len(timeline))
plt.bar(timeline, buy_number, label='Bayonet', fc='y', width=0.2)
plt.bar(timeline2, buy_number2, label='Karambit', fc='r', width=0.2)
plt.ylabel('Number')
plt.xlabel('Month')
plt.title('Transaction number(Bayonet & Karambit) in 2022')
plt.legend()
plt.show()

