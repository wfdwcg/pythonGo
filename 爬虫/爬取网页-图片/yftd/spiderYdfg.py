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
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    page1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(page1)
    #page = urllib.request.urlopen(url)
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
            #http://bbs.voc.com.cn/viewthread.php?tid=6459367
            if (imgInit.find("read-htm-tid")) != 0:
                continue
            imgInit = "http://XXX/pw/" + imgInit
            print("imgInit:" + imgInit)
            initHtml = getHtml(imgInit)
            reg = r'src="(.+?\.jpg)"'
            imgre = re.compile(reg)
            initHtml = initHtml.decode('utf-8')  # python3
            imglist = imgre.findall(initHtml)
            x = 0
            for imgurl in imglist:
                if (imgurl.find("XXX")) != 0:
                    continue
                if (imgurl in st):
                    print ("has_same_image:%s" % imgurl)
                    continue
                st.add(imgurl)
                t = time.time()
                imagename = str(int(round(t * 1000))) + str(random.randint(0,100))
                print(threading.currentThread().name + "::write_success:name=" + imgurl)
                ssl._create_default_https_context = ssl._create_unverified_context

                opener = urllib.request.build_opener()
                opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')]
                urllib.request.install_opener(opener)
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
