import requests
import re
import pandas as pd
import plotly


url_first='http://www.ygdy8.net/html/gndy/dyzz/index.html'
head={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
cookies={'cookie':'XLA_CI=b65d62d83ce74a25a2a33c92c2a510e0'}
topHtml=requests.get(url_first, headers=head, cookies=cookies)
topHtml.encoding = 'gbk'

nextMatch=re.compile(r'<a\s+href=\'(.*?)\'>下一页</a>') #列表页下一页
msgMatch = re.compile(r'<a\s+href="(.+?\.html)"\s+class="ulink">') #详情页

##详情页需要抓取的数据项
##view-source:http://www.ygdy8.net/html/gndy/dyzz/20181113/57761.html
msgsMatch=re.compile(r'◎译\s+名\s+(.*?)\s+<br\s+/>.*?◎片\s+名\s+(.*?)\s+<br\s+/>.*?◎产\s+地\s+(.*?)\s+<br\s+/>.*?◎豆瓣评分\s+(.*?)\s+<br\s+/>.*?◎简\s+介\s+<br\s+/><br\s+/>\s+(.*?)<br\s+/><br\s+/><img.*?<a\s+href="(ftp://.+?)">ftp://.*?',re.S)
#msgsMatch=re.compile(r'译\s+名\s+(.*?)\s+<br\s+/>.*?',re.S)
i = 0
st = set("0")
while topHtml.status_code == 200:
    print('inLoop')
    i += 1
    if i > 20:
        break
    listMsg = re.findall(msgMatch,topHtml.text)
    for msgPagePre in listMsg:
        msgPageUrl = 'http://www.ygdy8.net' + msgPagePre
        print("msgPageUrl:" + msgPageUrl)
        pageHtml = requests.get(msgPageUrl, headers=head, cookies=cookies)
        ###设置输出的编码格式，否则为中文乱码
        pageHtml.encoding = 'gbk'
        msgsThisPage = re.findall(msgsMatch,pageHtml.text)
        ##去重
        if len(msgsThisPage)>0:
            if msgsThisPage[0] in st:
                print("has the same item:")
                print(msgsThisPage[0])
                continue
            st.add(msgsThisPage[0])
        print(msgsThisPage)
        data=pd.DataFrame(msgsThisPage)
        data.to_csv('./movieMsgs.csv', header=False,index=False,mode='a+')
        data=[]
        msgsThisPage=[]
    nextPagePre = re.findall(nextMatch, topHtml.text)[0]
    nextPageUrl = 'http://www.ygdy8.net/html/gndy/dyzz/' + nextPagePre
    topHtml = requests.get(nextPageUrl, cookies=cookies, headers=head)
    topHtml.encoding = 'gbk'