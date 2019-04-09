import requests
import re
import pandas as pd
import plotly
import json
import urllib.request
import http.cookiejar

url_first='https://movie.douban.com/subject/26363254/comments?start=0'
head={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
cookies={'cookie':'ll="118172"; bid=31vaI6_q3CM; __utmc=30149280; __utmc=223695111; _vwo_uuid_v2=D4CA2882D475B492A2E91DCF31D3867C3|72d0320998283579971ed558ae0fdad9; douban-fav-remind=1; __utmz=30149280.1543762097.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1543762097.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1543915571%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DZOEqacLatSWPUHDDhi6vYsJSCbjkpZQGyL8i0xefh021XhyBMqPAmU1HZsFDd56HIyi4Cfd2Mb9S43OKKzAli_%26wd%3D%26eqid%3Da575e96a00020196000000035c03f0ad%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.264379618.1543636660.1543762097.1543915571.6; __utmb=30149280.0.10.1543915571; __utma=223695111.1484075202.1543636660.1543762097.1543915571.6; __utmb=223695111.0.10.1543915571; _pk_id.100001.4cf6=feb6197d541afef6.1543636660.6.1543915924.1543762097.'}
html=requests.get(url_first, headers=head, cookies=cookies)
#选取从"<a href=""到"&amp;"之间的部分
reg=re.compile(r'<a href="(.*?)&amp;.*?class="next">') #下一页
#view-source:https://movie.douban.com/subject/26363254/comments?start=0
#每个括号括起来的为一列
ren=re.compile(r'<a\s+title="(.*?)"\s+href=".*?\s+onclick="">(.*?)</a>.*?rating"\s+title="(.*?)"></span>.*?"\s+title="(.*?)">.*?<span class="short">(.*?)</span>\n?',re.S)
i = 0
while html.status_code == 200:
    print('inLoop')
    i += 1
    if i > 30000:
        break
    url_next='https://movie.douban.com/subject/26363254/comments'+re.findall(reg,html.text)[0]
    print("url_next:" + url_next)
    zhanlang=re.findall(ren,html.text)
    print(zhanlang)
    data=pd.DataFrame(zhanlang)
    data.to_csv('./movieMsgs.csv', header=False,index=False,mode='a+')
    print("writeOk")
    data=[]
    zhanlang=[]
    html=requests.get(url_next,cookies=cookies,headers=head)


plotly()