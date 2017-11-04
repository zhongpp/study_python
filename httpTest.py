import http.client
import urllib, parser

# # 初始化一个 https 链接
conn = http.client.HTTPSConnection("www.python.org")
# 指定 request 请求的方法和请求的链接地址
conn.request("GET", "/doc/")
# 得到返回的 http response
r1 = conn.getresponse()
# HTTP 状态码
print(r1.status, r1.reason)
# HTTP 头部
print(r1.getheaders())
# body 部分
print(r1.read())
# 如果连接没有关闭,打印输出前 200 个字节
if not r1.closed:
    print(r1.read(200))
# 关闭连接后才能重新请求
conn.close()
# 请求一个不存在的文件或地址
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status, r2.reason)
conn.close()
# 使用 HEAD 请求,但是不会返回任何数据
conn = http.client.HTTPSConnection("www.python.org")
conn.request("HEAD", "/")
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()
print(len(data))
conn.close()
# 使用 POST 请求,提交的数据放在 body 部分
params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
# post 请求数据,要带上 Content-type 字段,以告知消息主体以何种方式编码
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = http.client.HTTPConnection("bugs.python.org")
conn.request("POST", "/", params, headers)
response = conn.getresponse()
# 访问被重定向
print(response.status, response.reason)
print(response.read().decode("utf-8"))
conn.close()




