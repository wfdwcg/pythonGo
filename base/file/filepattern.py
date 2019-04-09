import re
import pandas as pd

msgsMatch=re.compile(r'<mark>myPrizeAll</mark>\|(.+?)\|</span></dd>.*?',re.S)

f = open('./test.txt', 'r')
for line in f.readlines():
    listMsg = re.findall(msgsMatch, line)
    data = pd.DataFrame(listMsg)
    data.to_csv('./TONGJI.csv', header=False, index=False, mode='a+')
    data = []
    listMsg = []