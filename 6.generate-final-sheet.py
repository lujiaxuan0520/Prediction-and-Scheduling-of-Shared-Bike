#coding=utf-8
import csv
import re
import math

def Index(category):
    s=category[:2]
    if s=="餐饮":
        return 0
    elif s=="道路" or s=="地名" or s=="通行":
        return 1
    elif s=="公共" or s=="生活" or s=="事件" or s=="体育" or s=="科教" or s=="医疗":
        return 2
    elif s=="公司" or s=="金融" or s=="政府":
        return 3
    elif s=="购物":
        return 4
    elif s=="交通":
        return 5
    elif s=="商务" or s=="住宿":
        return 6
    else:
        return -1

filename = '北京poi数据区域划分结果.csv'
with open(filename) as f:
    reader = csv.reader(f)
    data = list(reader)

dic=dict()
count=0
for line in data:
    category=line[1]
    index=Index(category)
    district=int(line[20])
    if index!=-1:
        if district not in dic.keys():
            dic[district]=[0,0,0,0,0,0,0]
            count+=1
        else:
            dic[district][index]+=1
for i in range(40000):
    if i not in dic.keys():
        dic[i]=[0,0,0,0,0,0,0]
        count+=1


with open("单车各区域与时间段需求量统计.csv") as f:
    reader1 = csv.reader(f)
    data1 = list(reader1)
    
new_data = []
for word in data1:
    district=int(word[0])
    new_line = word
    new_line.append(dic[district][0])
    new_line.append(dic[district][1])
    new_line.append(dic[district][2])
    new_line.append(dic[district][3])
    new_line.append(dic[district][4])
    new_line.append(dic[district][5])
    new_line.append(dic[district][6])
    new_data.append(new_line)

with open('各时间段各区域地理画像与需求量对照表.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    count = 0
    for row in new_data:
        writer.writerow(row)
        count += 1
    print(count)