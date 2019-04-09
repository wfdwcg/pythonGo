import urllib.request
import re
import time
import random
import _thread
import threading
import logging
import ssl


####功能：从列表页进入详情页，然后提取出下载链接

##列表页：http://www.youxiake.com/lines/list?code=cn&month=0&day=0&days=0&price=0&place=0&tag=0&class_id=0&gts=&gte=&p=2
def getHtml(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    page1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(page1)
    html = page.read()
    return html


###详情页：<a href="http://www.youxiake.com/lines.html?id=18010" target="_blank">
def getPageLevel1(html):
    reg1 = r'<a\s+href="(.+?)"\s+target="_blank">'
    xqMatch = re.compile(reg1)
    html = html.decode('utf-8')  # python3
    xqLinklist = xqMatch.findall(html)
    print(xqLinklist)
    return xqLinklist


###获取下载链接
def getImg(xqLinklist,st):
    for xqLink in xqLinklist:
        try:
            #http://www.youxiake.com/lines.html?id=18010
            if xqLink.find("http://www.youxiake.com/lines.html")!=0:
                continue;
            if xqLink in st:
                continue
            st.add(xqLink)
            xqPage = getHtml(xqLink)
            reg = r'<title>(.+?)</title>.*?class="price">\s+<strong>(.+?)</strong>\s+元起 (成人).*?' \
                  r'class="hd_lineDay"(.+?)</span>?.+?'

            #msgsMatch=re.compile(r'◎译\s+名\s+(.*?)\s+<br\s+/>.*?◎片\s+名\s+(.*?)\s+<br\s+/>.*?◎产\s+地\s+(.*?)\s+<br\s+/>.*?◎豆瓣评分\s+(.*?)\s+<br\s+/>.*?◎简\s+介\s+<br\s+/><br\s+/>\s+(.*?)<br\s+/><br\s+/><img.*?<a\s+href="(ftp://.+?)">ftp://.*?',re.S)

            xqs = re.compile(reg)
            xqPage = xqPage.decode('utf-8')  # python3
            linklist = xqs.findall(xqPage)
        except Exception as e:
            logging.exception(e)


def dealWithLine(line,st):
    if(str(line).find("##") == 0):
        return
    html = getHtml(line)
    imgInitlist = getPageLevel1(html)
    getImg(imgInitlist,st)


f = open("./source.txt")
line = f.readline()
y = 1
st = set("0")
while line:
    _thread.start_new_thread(dealWithLine, (line,st))
    print("Thread-"+str(y)+"start")
    y += 1
    line = f.readline()
f.close()

while 1:
   pass
