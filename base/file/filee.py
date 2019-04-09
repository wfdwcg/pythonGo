# print(f.read())
# f.close()

with open('./test.txt', 'r') as f:
    print(f.read())

f = open('./test.txt', 'r')
for line in f.readlines():
    print(line)
f.close()


###写入，覆盖原来文件
with open('./test.txt', 'a+') as f:
    f.write("www.qq2.com")
