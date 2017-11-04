import sys
import requests
import urllib.request
import urllib.parse
print(sys.getdefaultencoding())
request_str = 'http://api.map.baidu.com/geocoder/v2/?address={中国广东省深圳市南山区学府路81号附近软产业基地1栋C座}&output=json&ak=jwIc3hYW05E87k5GwLv0CIeUMSFRYoy2'
# params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# url = "http://www.baidu.com?%s" % params
# with urllib.request.urlopen(request_str) as f:
#     print(f.read().decode('utf-8'))


request_str.encode('utf-8')

r = requests.get('http://api.map.baidu.com/geocoder/v2/?address={中国广东省深圳市南山区学府路81号附近软产业基地1栋C座}&output=json&ak=jwIc3hYW05E87k5GwLv0CIeUMSFRYoy2')
print(r.content)
r.headers['content-type']
# 'application/json; charset=utf8'
r.encoding
# 'utf-8'
r.text
# u'{"type":"User"...'
r.json()
# {u'private_gists': 419, u'total_private_repos': 77, ...}
