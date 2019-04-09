import urllib.request
import re
import time
import random
import _thread
import threading
import logging
import ssl


####功能：从列表页进入详情页，然后提取出下载链接

##列表页：http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html
def getHtml(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    page1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(page1)
    html = page.read()
    return html


###详情页：http://www.ygdy8.net/html/gndy/dyzz/20181111/57756.html
def getPageLevel1(html):
    reg1 = r'<a\s+href="(.+?\.html)"\s+class="ulink">'
    imgreInit = re.compile(reg1)
    html = html.decode('gbk')  # python3
    imgInitlist = imgreInit.findall(html)
    print(imgInitlist)
    return imgInitlist


###获取下载链接
def getImg(pageList,st):
    for pagel in pageList:
        try:
            #/html/gndy/dyzz/20181113/57762.html
            pageLv1 = "http://www.ygdy8.net" + pagel
            print("pageLv1:" + pageLv1)
            initPage = getHtml(pageLv1)
            reg = r'<a\s+href="(.+?)">ftp://'
            linkMatch = re.compile(reg)
            initPage = initPage.decode('gbk')  # python3
            linklist = linkMatch.findall(initPage)
            x = 0
            for linkUrl in linklist:
                if (linkUrl.find("ftp://")) != 0:
                    continue
                if (linkUrl in st):
                    print ("has_same_link:%s" % linkUrl)
                    continue
                st.add(linkUrl)
                with open('./linkResult.txt', 'a+') as f:
                    f.write(linkUrl + "\n")
                x += 1
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
