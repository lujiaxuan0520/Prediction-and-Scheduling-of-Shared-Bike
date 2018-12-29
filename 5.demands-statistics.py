#coding=utf-8
import csv
import re
import math

filename = '单车数据区域划分结果.csv'
with open(filename) as f:
    reader = csv.reader(f)
    data = list(reader)

dic=dict()
for line in data:
    time=line[1]
    time=int(re.split(r':',time)[0])
    time=str(math.floor(time/2))
    key=str(line[6])+'-'+time
    if key in dic.keys():
        dic[key]+=1
    else:
        dic[key]=1

with open('单车各区域与时间段需求量统计.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    count = 0
    for items in dic.items():
        new_line=[]
        key=items[0]
        value=items[1]
        split=re.split(r'-',key)
        district=int(split[0])
        time=int(split[1])
        new_line.append(district)
        new_line.append(time)
        new_line.append(value)
        writer.writerow(new_line)
        count += 1
    for i in range(40000):
        for j in range(12):
            s=str(i)+'-'+str(j)
            if s not in dic.keys():
                count+=1
                new_line=[]
                new_line.append(i)
                new_line.append(j)
                new_line.append(0)
                writer.writerow(new_line)

    print(count)