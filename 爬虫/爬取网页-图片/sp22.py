import urllib.request
import re
import time
import logging


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImgInit(html):
    reg1 = r'zoomfile="(.+?\.jpg)"'
    imgreInit = re.compile(reg1)
    imgInitlist = imgreInit.findall(html)
    return imgInitlist


def getImg(imgInitlist):
    for imgInit in imgInitlist:
        try:
            print(imgInit)
            print(imgInit.find("https://www.mymypic.net"))
            if (imgInit.find("https://www.mymypic.net")) != 0:
                continue
            if not(imgInit.endswith(".jpg")):
                continue
            x = 0
            t = time.time()
            urllib.request.urlretrieve(imgInit,'/Users/lichuang.lc/Desktop/testt/cece/%s.jpg' % str(int(round(t * 1000))))
            x+=1
        except Exception as e:
            logging.exception(e)

html = getHtml("https://www.jkforum.net/thread-9738267-1-1.html")
imgInitlist =  getImgInit(html)
print(getImg(imgInitlist))

