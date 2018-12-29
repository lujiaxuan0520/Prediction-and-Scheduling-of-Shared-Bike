#coding=utf-8
import csv
import random

filename = '训练集2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    data = list(reader)

new_data=[]
for i in range(4000):
    rand=random.randint(0,40963)
    new_data.append(data[rand])

with open('测试集.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    count = 0
    for row in new_data:
        writer.writerow(row)
        count += 1
    print(count)