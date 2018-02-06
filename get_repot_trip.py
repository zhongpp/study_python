#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json


def calculate():
    ak = 'jwIc3hYW05E87k5GwLv0CIeUMSFRYoy2'
    with open("dst.json", encoding='utf-8') as fr:
        content = fr.read()
        datas = json.loads(content)
        print(datas)
        print(len(datas["RECORDS"]))
        for data in datas["RECORDS"]:
            data
            try:
                originate_location_lat = data['plat']
                originate_location_lng = data['plon']
                destination_location_lat = data['dlat']
                destination_location_lng = data['dlon']
                url = "http://api.map.baidu.com/direction/v2/driving?origin=%s,%s&destination=%s,%s&ak=%s" % (originate_location_lat, originate_location_lng, destination_location_lat, destination_location_lng, ak)
                resp = requests.get(url)
                rep_str = resp.json()
                print(rep_str['result']['routes'][0]['distance']/1000)
            except Exception as exception:
                print(0)
                pass

if __name__ == '__main__':
    calculate()