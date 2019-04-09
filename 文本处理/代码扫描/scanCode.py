import os.path
import re


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    count = 0
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        if os.path.isfile(child):
            count += readFile(child)
            continue
        else:
            eachFile(child)

# 遍历出结果 返回文件的名字
def readFile(filenames):
    fopen = open(filenames, 'r')  # r 代表read
    fileread = fopen.read()
    t = re.search(r'buy\.repayfundpackage\.rabbitmq\.queue', fileread)
    fopen.close()
    if t:
        arr.append(filenames)
        return 1
    return 0

'''
buy\.insurance\.rabbitmq\.queue 2
buy\.repayfundpackage\.rabbitmq\.queue 2
fcVerify\.rabbitmq\.queueName
deposit\.frozen\.rabbitmq\.queueName
gjb\.fund\.consumer\.rabbitmq\.queueName
billimport\.rabbitmq\.consumer\.queue
invite\.crowd\.login\.rabbitmq\.queue
invite\.friends\.rabbitmq\.queue
invite\.register\.rabbitmq\.queue
invitation\.wxshare\.rabbitmq\.queue
lyq\.loan\.rabbitmq\.queueName
ocelot\.import\.bill\.rabbitmq\.queueName
opsevent\.consumer\.rabbitmq\.queueName
rabbit\.order\.queue\.name
periodbill\.rabbitmq\.consumer\.queue
repay\.rabbitmq\.queueName
returnloan\.rpd\.lyq\.rabbitmq\.queueName
decentral\.deposit\.rabbitmq\.queueName
rpplan\.deposit\.rabbitmq\.queueName
rpb\.openaccount\.rabbitmq\.consumer\.queue
rpb\.userrecharge\.rabbitmq\.queueName
rpd\.certification\.rabbitmq\.queueName
user\.login\.event\.queue
usercenter\.rabbitmq\.queueName\.userCreated
user\.daily\.sign\.rabbitmq\.consumer\.queue
utilities\.repay\.rabbitmq\.queueName
welfare\.redpacket\.rabbitmq\.queueName
welfare\.coupon\.rabbitmq\.queueName
welfare\.loanCoupon\.rabbitmq\.queueName
welfare\.repay\.rabbitmq\.queueName
LMK_applySubmitSuccess
gold_coin_pay_success
Vcard_SuccBuyOrQuitFinancial
LMK_CardStatusChanged
LMK_TransferAccountSuccess
p2pmarket_purchase_notify
bonus_pay_success_notify
'''


    #reg = r'.*?(welfare\.redpacket\.rabbitmq\.queueName).*?'
    #key = re.compile(reg,re.S)
    #keylist = key.findall(fileread)
    #if keylist is not None:
        #return len(keylist)

if __name__ == "__main__":
    count = 0
    filenames = '/Users/lichuang.lc/Documents/git/ops-activity/mainVenue/server/src/main/java'  # refer root dir
    arr = []
    count = eachFile(filenames)
    print(count)
    print(len(arr))