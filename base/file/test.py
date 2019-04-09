import urllib.request

urll = "http://t-www.meipian.cn/promo/checkin_duiba/api/autoLogin?dbredirect=https%3A%2F%2Factivity.m.duiba.com.cn%2Fhdtool%2Findex%3Fid%3D3275442"
print(urll)

urll = urllib.request.unquote(urll)
print(urll)