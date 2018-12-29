#coding=utf-8
import xlrd
import csv
data = xlrd.open_workbook('北京poi数据订单1.xlsx')
table = data.sheets()[0]
nrows = table.nrows
new_data=[]
for i in range(1,nrows):
    new_data.append(table.row_values(i))
data = xlrd.open_workbook('北京poi数据订单2.xlsx')
table = data.sheets()[0]
nrows = table.nrows
for i in range(1,nrows):
    new_data.append(table.row_values(i))
with open('北京poi数据汇总表.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    count = 0
    for row in new_data:
        writer.writerow(row)
        count += 1
    print(count)