#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json


def parking(address):
    ak = 'RFHjuImLlwq9xg9hi5DlozbEuGGRE7f4'
    url = "http://api.map.baidu.com/geocoder/v2/?address={%s}&output=json&ak=%s" % (address, ak)
    resp = requests.get(url)
    originate_location = resp.json()['result']['location']
    originate_location_lng = resp.json()['result']['location']['lng']
    originate_location_lat = resp.json()['result']['location']['lat']

    print(originate_location)
    print(' %s %s' % (originate_location_lng, originate_location_lat))

    #     114.164071,22.580606 116.307054,40.057478
    # 地址逆解析
    location = '22.58066,114.165782'
    url = "http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=%s&output=json&pois=1&ak=%s" % (
        location, ak)
    resp = requests.get(url)
    rep_str = resp.content.decode(encoding='utf-8')
    rep_json = json.loads(rep_str[29:-1])
    print(rep_json)
    print(rep_json['result']['location'])

    # 推荐上车点服务
    location = '120.349352,30.333446'
    url = 'http://api.map.baidu.com/parking/search?location=%s&coordtype=bd09ll&ak=%s' % (location, ak)
    resp = requests.get(url)
    print(resp.json())


if __name__ == '__main__':
    parking('东湖绿道揽胜亭观景台')
