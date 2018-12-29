import csv
left_1 = (40.011039, 116.221884)#左上角
left_2 = (39.779632, 116.530812)#右下角
width = round(((left_1[0] - left_2[0])/200), 9)
length = round(((left_2[1] - left_1[1])/200), 9)
print(length, width)


def mark(lat, lot):
    if lat > left_1[0] or lat < left_2[0] or lot < left_1[1] or lot > left_2[1]:
        return -1
    else:
        row = (lat - left_2[0])//width
        col = (lot - left_1[1])//length
        tag = row * 200 + col
        return int(tag)

filename = 'example1.csv'


with open(filename) as f:
    reader = csv.reader(f)
    data = list(reader)


#已经得到data

new_data = []
for word in data:
    new_line = word
    new_line.append(mark(float(word[2]), float(word[3])))
    new_line.append(mark(float(word[4]), float(word[5])))
    new_data.append(new_line)


with open('example2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    count = 0
    for row in new_data:
        if row[-1] != -1 and row[-2] != -1:
            writer.writerow(row)
            count += 1
    print(count)

