import urllib.request
import re
import time
import random
import _thread
import threading
import logging
import ssl


def getHtml(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImgInit(html):
    reg1 = r'href="(.+?\.html)"'
    imgreInit = re.compile(reg1)
    html = html.decode('utf-8')  # python3
    imgInitlist = imgreInit.findall(html)
    print(imgInitlist)
    return imgInitlist


def getImg(imgInitlist,st):
    for imgInit in imgInitlist:
        try:
            if (imgInit.find("https://www.zcool.com.cn/work/")) != 0:
                continue
            if not(imgInit.endswith(".html")):
                continue
            print("imgInit:" + imgInit)
            initHtml = getHtml(imgInit)
            reg = r'src="(.+?\.jpg)"'
            imgre = re.compile(reg)
            initHtml = initHtml.decode('utf-8')  # python3
            imglist = imgre.findall(initHtml)
            x = 0
            for imgurl in imglist:
                if (imgurl.find("https://img.zcool.cn/community")) != 0:
                    continue
                if (imgurl in st):
                    print ("has_same_image:%s" % imgurl)
                    continue
                st.add(imgurl)
                t = time.time()
                imagename = str(int(round(t * 1000))) + str(random.randint(0,100))
                print(threading.currentThread().name + "::write_success:name=" + imgurl)
                ssl._create_default_https_context = ssl._create_unverified_context
                urllib.request.urlretrieve(imgurl, '/Users/lichuang.lc/Desktop/testt/cece/%s.jpg' % imagename)
                x += 1
        except Exception as e:
            logging.exception(e)


def dealWithLine(line,st):
    if(str(line).find("##") == 0):
        return
    html = getHtml(line)
    imgInitlist = getImgInit(html)
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
