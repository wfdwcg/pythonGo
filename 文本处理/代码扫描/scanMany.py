import os.path
import re
import _thread
import threading
import logging



# 遍历指定目录，显示目录下的所有文件名
def eachFile(line,filepath):
    count = 0
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        if os.path.isfile(child):
            if count > 0:
                print("before:")
                print(count)
            count += readFile(child,line)
            if count > 0:
                print(count)
            #             print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
            continue
        else:
            eachFile(line,filepath)

# 遍历出结果 返回文件的名字
def readFile(filenames,line):
    fopen = open(filenames, 'r')  # r 代表read
    fileread = fopen.read()
    t = re.search(r'%s' %line, fileread)
    fopen.close()
    if t:
        #arr.append(filenames)
        return 1
    return 0


    #reg = r'.*?(welfare\.redpacket\.rabbitmq\.queueName).*?'
    #key = re.compile(reg,re.S)
    #keylist = key.findall(fileread)
    #if keylist is not None:
        #return len(keylist)

def countNum(line,filepath):
    try:
        count = eachFile(line,filepath)
        print(line)
        print(count)
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    filepath = '/Users/lichuang.lc/Documents/git/ops-activity/mainVenue/server/src/main/java'
    f = open("./source.txt")
    line = f.readline()

    while line:
        _thread.start_new_thread(countNum, (line,filepath))
        print("Thread-" + str(line) + "start")
        line = f.readline()
    f.close()

    while 1:
        pass