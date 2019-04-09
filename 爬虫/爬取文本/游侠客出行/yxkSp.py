import requests
import re
import pandas as pd
import plotly


url_first='http://www.youxiake.com/lines/list?code=cn'
head={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
cookies={'cookie':'sideMuenShop=1; _ga=GA1.2.1359402878.1544164788; _gid=GA1.2.840314668.1544164788; sitecode=1; yxk_saltkey=N06rN6zc; muzhi_register=eyJpdiI6Ikc4ZXBibEpOMklFczdic1FqMHcrdUE9PSIsInZhbHVlIjoiZmRsemQ3RXA0ZmpWQnMzamo0UXZZVVdSWXdHek1iWTVjelltM1g2UGloWT0iLCJtYWMiOiJlNTlkNTAxYWUwNzc1MTNhOGVkNDNlNjMzNzgzZGZhNjgyM2FlMDg2YmFkYjRmYmM1NzE2NTRlZWRiZDRkNzhjIn0%3D; XSRF-TOKEN=eyJpdiI6IlBTTW5QMlVTZCtvb0I5ODV6Z1k1TlE9PSIsInZhbHVlIjoiSHNnV2t0N3RJQ3RZM3dDZ0ZZZGtxWnAyUUhqbUFrSmlReWNISlZjZ1FHeFBjelNNbDdWbGtvOGsrUHJXTyt0ZlZcL1NLR2lHc0dSTzlEYlJDMDZvOWdnPT0iLCJtYWMiOiIwNDk1ZjlkZGYzNWMxMjQ0YTY5ZWY3OGIwZWFhN2E3OWRkMjIxMTNlMjAxZTkzNjRlMzg0NDRmY2ZkZTJjOGQ5In0%3D; laravel_session=eyJpdiI6InM3TkNaVEtpZ292RGg0cmo5aEhKbHc9PSIsInZhbHVlIjoiU2U3NXpqNTlBKzdWbW94aDZwV1VuRHExQTB1Tk9GNVwvS2xMXC9NVkxPXC9sNGpReXE3OWFpYXU2OEg1NlJRczl0NW5HXC9CRnJhK2R0cmpxc09qSVpGTEV3PT0iLCJtYWMiOiJlNzNjNTQ4Y2EyZmMzODcyMjhiNTMwZmFmZDM0YjgwZDYwMWNiMTFkMDY5NzA3YjRlZGI1OGJhYWRkY2YwNGE4In0%3D; Hm_lvt_4668967a6a0541a2a7cb9bf90df08bdd=1544165099; sideMuenShop=1; _gat=1; yxk_session=eyJpdiI6IlJhekJ5eHBRcFlZT2d6amFiYXdZMFE9PSIsInZhbHVlIjoiODhzNExvN210ZmZiT3hYVnY5NXN5WXYrVzh0MzVFeTlQdjFucWpPZUxjOTlYK29EOHk4M3V4Z2JiZ0dmd0hNdSIsIm1hYyI6IjExNzY0MmFjZjVmMWQyZDBmYmE4MGRkZmUzODBhOTZmOTlmZGRmY2I3OGZiYmMyODRjNGRiYjliNTZkMjhjY2EifQ%3D%3D; yxk_last_visit=eyJpdiI6IlJTQXJZV2RrK3lrVWRRVzVMeU1adkE9PSIsInZhbHVlIjoicjUyZTdqamJSYUNOYzd2eDEwME5QQT09IiwibWFjIjoiMmNkNmNlMDFkOWE5ZTgwZTJkNTM4MDFkM2EyMGViY2UyNWVkNWYyMTgyYjY5ZTU5YmViZGY2MDZmZDM2YjUyZCJ9; Hm_lpvt_4668967a6a0541a2a7cb9bf90df08bdd=1544168488'}
topHtml=requests.get(url_first, headers=head, cookies=cookies)
#topHtml.encoding = 'gbk'

##<a href="http://www.youxiake.com/lines/list?code=cn&month=0&day=0&days=0&price=0&place=0&tag=0&class_id=0&gts=&gte=&p=2"  title="下一页">>
nextMatch=re.compile(r'<a\s+href="(.*?)"\s+title="下一页">>') #列表页下一页
##<a href="http://www.youxiake.com/lines.html?id=14904" target="_blank">
xqPageMatch = re.compile(r'<a\s+href="(.+?)"\s+target="_blank">') #详情页

##详情页需要抓取的数据项
####view-source:http://www.youxiake.com/lines.html?id=18010
msgsMatch=re.compile(r'<title>(.+?)</title>.*?class="c_666">(.+?)\s</span>.*?'
                     r'class="hd_otherSpan">\s+<strong>(.+?)</strong><i>人浏览</i>\s+<strong>(.+?)</strong><i>人参加过.*?'
                     r'class="hd_lineDay">(.+?)</span>.*?class="price">\s+<strong.*?>(.+?)</strong>\s+元起.+?'
                     r'class="hd_priceInfoContent\s+hd_priceInfoPlace">\s+(.+?)\s+<!--\s+<div\sclass="phone_buy_mugua">.+?',re.S)
i = 0
st = set("0")
while topHtml.status_code == 200:
    print('inLoop')
    i += 1
    if i > 20:
        break
    xqPageList = re.findall(xqPageMatch,topHtml.text)
    for xqPage in xqPageList:
        if xqPage.find("http://www.youxiake.com/lines.html") != 0:
            continue;
        if xqPage.find("nofollow") > 0:
            continue;
        if xqPage in st:
            continue
        st.add(xqPage)
        print("xqPage:")
        print(xqPage)
        pageHtml = requests.get(xqPage, headers=head, cookies=cookies)
        ###设置输出的编码格式，否则为中文乱码
        #pageHtml.encoding = 'gbk'
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
        data.to_csv('./yxkMsgs.csv', header=False,index=False,mode='a+')
        data=[]
        msgsThisPage=[]
    nextPageUrl = re.findall(nextMatch, topHtml.text)[0]
    topHtml = requests.get(nextPageUrl, cookies=cookies, headers=head)
    #topHtml.encoding = 'gbk'