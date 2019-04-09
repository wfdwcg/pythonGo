import redis

###https://www.jianshu.com/p/2639549bedc8
##基本链接
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('keyOnly', 'value1')  # key是"foo" value是"bar" 将键值对存入redis缓存
r.expire('keyOnly',100)
print(r['keyOnly'])


##连接池
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)
r.set('keyPool', 'value2')     # key是"gender" value是"male" 将键值对存入redis缓存
print(r.get('keyPool'))      # gender 取出键male对应的值