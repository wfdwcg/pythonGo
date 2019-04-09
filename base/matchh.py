import re


#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符,加?就可以采用非贪婪匹配
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010--12345'))

print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))