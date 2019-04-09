import csv

out = open('./test22.csv','a+', newline='')
#设定写入模式
csv_write = csv.writer(out,dialect='excel')
#写入具体内容

i = 10000000
while i<10150000:
    i += 1
    sou = ["perf_" + str(i)]
    csv_write.writerow(sou)
