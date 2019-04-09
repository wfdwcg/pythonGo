import datetime;

i = datetime.datetime.now()
#yyyy-MM-dd HH:mm:ss
print(i.strftime('%Y-%m-%d %H:%M:%S'))
print("取字段：day="+str(i.day)+";hour="+str(i.hour))
print(("UNIX时间戳=")+str(int(i.timestamp()*1000)))