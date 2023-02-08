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
for i in range(transaction['time'].count()):
    time_original = transaction.iloc[i, 0]
    time_format = datetime.strptime(time_original, '%b %d %Y %H %M')
    time_format = time_format.strftime('%Y/%m/%d %H:%M')
    transaction.iloc[i, 0] = time_format
print(transaction)

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

tmp01 = transaction[transaction['time'].str.contains('2021/01')]
tmp02 = transaction[transaction['time'].str.contains('2021/02')]
tmp03 = transaction[transaction['time'].str.contains('2021/03')]
tmp04 = transaction[transaction['time'].str.contains('2021/04')]
tmp05 = transaction[transaction['time'].str.contains('2021/05')]
tmp06 = transaction[transaction['time'].str.contains('2021/06')]
tmp07 = transaction[transaction['time'].str.contains('2021/07')]
tmp08 = transaction[transaction['time'].str.contains('2021/08')]
tmp09 = transaction[transaction['time'].str.contains('2021/09')]
tmp010 = transaction[transaction['time'].str.contains('2021/10')]
tmp011 = transaction[transaction['time'].str.contains('2021/11')]
tmp012 = transaction[transaction['time'].str.contains('2021/12')]

tmp001 = transaction[transaction['time'].str.contains('2020/01')]
tmp002 = transaction[transaction['time'].str.contains('2020/02')]
tmp003 = transaction[transaction['time'].str.contains('2020/03')]
tmp004 = transaction[transaction['time'].str.contains('2020/04')]
tmp005 = transaction[transaction['time'].str.contains('2020/05')]
tmp006 = transaction[transaction['time'].str.contains('2020/06')]
tmp007 = transaction[transaction['time'].str.contains('2020/07')]
tmp008 = transaction[transaction['time'].str.contains('2020/08')]
tmp009 = transaction[transaction['time'].str.contains('2020/09')]
tmp0010 = transaction[transaction['time'].str.contains('2020/10')]
tmp0011 = transaction[transaction['time'].str.contains('2020/11')]
tmp0012 = transaction[transaction['time'].str.contains('2020/12')]

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

number1 = 0
for i in tmp01['number']:
    number1 = number1 + i
print(number1)

number2 = 0
for i in tmp02['number']:
    number2 = number2 + i
print(number2)

number3 = 0
for i in tmp03['number']:
    number3 = number3 + i
print(number3)

number4 = 0
for i in tmp04['number']:
    number4 = number4 + i
print(number4)

number5 = 0
for i in tmp05['number']:
    number5 = number5 + i
print(number5)

number6 = 0
for i in tmp06['number']:
    number6 = number6 + i
print(number6)

number7 = 0
for i in tmp07['number']:
    number7 = number7 + i
print(number7)

number8 = 0
for i in tmp08['number']:
    number8 = number8 + i
print(number8)

number9 = 0
for i in tmp09['number']:
    number9 = number9 + i
print(number9)

number10 = 0
for i in tmp010['number']:
    number10 = number10 + i
print(number10)

number11 = 0
for i in tmp011['number']:
    number11 = number11 + i
print(number11)

number12 = 0
for i in tmp012['number']:
    number12 = number12 + i
print(number12)

timeline = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
buy_number = [number1, number2, number3, number4, number5, number6, number7, number8, number9, number10, number11, number12]
plt.bar(timeline, buy_number)
plt.ylabel('Number')
plt.xlabel('Month')
plt.title('Transaction number in 2021')
plt.show()

number1 = 0
for i in tmp001['number']:
    number1 = number1 + i
print(number1)

number2 = 0
for i in tmp002['number']:
    number2 = number2 + i
print(number2)

number3 = 0
for i in tmp003['number']:
    number3 = number3 + i
print(number3)

number4 = 0
for i in tmp004['number']:
    number4 = number4 + i
print(number4)

number5 = 0
for i in tmp005['number']:
    number5 = number5 + i
print(number5)

number6 = 0
for i in tmp006['number']:
    number6 = number6 + i
print(number6)

number7 = 0
for i in tmp007['number']:
    number7 = number7 + i
print(number7)

number8 = 0
for i in tmp008['number']:
    number8 = number8 + i
print(number8)

number9 = 0
for i in tmp009['number']:
    number9 = number9 + i
print(number9)

number10 = 0
for i in tmp0010['number']:
    number10 = number10 + i
print(number10)

number11 = 0
for i in tmp0011['number']:
    number11 = number11 + i
print(number11)

number12 = 0
for i in tmp0012['number']:
    number12 = number12 + i
print(number12)

timeline = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
buy_number = [number1, number2, number3, number4, number5, number6, number7, number8, number9, number10, number11, number12]
plt.bar(timeline, buy_number)
plt.ylabel('Number')
plt.xlabel('Month')
plt.title('Transaction number in 2020')
plt.show()