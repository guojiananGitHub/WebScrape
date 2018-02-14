from twitter import *
import urllib.request

# 代理地址和端口
proxy_info = {'host':'localhostXXX','port':xxx}
# 為代理創建一個處理程序
proxy_support = urllib.ProxyHandler({"http": "http://%(host)s:%(port)d" % proxy_info})
#
opener =

t = Twitter(auth=OAuth("", "", "", ""))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)