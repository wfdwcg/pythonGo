import requests
import json
from datetime import datetime,timedelta
import time


##获取数据保存到本地
def save():
    start_time = datetime.now()
    end_time = datetime.strptime('2018-12-15 00:00:00','%Y-%m-%d %H:%M:%S')
    while start_time > end_time:
        # http://m.maoyan.com/mmdb/comments/movie/249342.json?_v_=yes&offset=15&startTime=2018-12-17%2015:49:00
        url = 'http://m.maoyan.com/mmdb/comments/movie/249342.json?_v_=yes&offset=15&startTime='+start_time.strftime('%Y-%m-%d %H:%M:%S')
        print(url)
        html = None
        try:
            html = get_data(url)
        except Exception as e:
            time.sleep(0.5)
            html = get_data(url)
        else:
            time.sleep(0.1)
        comments = parse_data_by_json(html)
        start_time = datetime.strptime(comments[14]['startTime'],'%Y-%m-%d %H:%M:%S')
        # print('评论最后一条评论时间：'+start_time)
        start_time = start_time - timedelta(seconds=1)
        for item in comments:
            # print(item)
            with open('./dataSource.txt','a',encoding='UTF-8') as f:
                f.write(item['nickname']+':'+item['cityName']+':'+item['content']+':'+str(item['score'])+':'+item['startTime']+'\n')
    print("finished")


##解析json数据
def parse_data_by_json(html):
    content = json.loads(html)
    json_data = content['cmts']
    total = content['total']
    # print(total)
    comments = []
    try:
        for item in json_data :
            comment = {
                'nickname':item['nickName'],
                'cityName':item['cityName'] if 'cityName' in item else'',
                'content':item['content'].strip().replace('\n',''),
                'score':item['score'],
                'startTime':item['startTime']
            }
            comments.append(comment)
        return comments
    except Exception as e:
        print(e)


#获取原始用户评论数据
def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        return html.content


save()