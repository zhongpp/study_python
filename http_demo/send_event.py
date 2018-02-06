import requests
import time
import json

url = "http://xxx/trips/%s/events"
access_token = ""


# 发送到达派件地点事件
def send_arrive_drop_off_event(uuid):
    url2 = url % uuid
    headers = {'PushEnvelope-Device-Token': access_token, 'Content-Type': 'application/json'}
    now = time.strftime("%Y-%m-%dT%H:%M:%S.%u+0800", time.localtime())
    body = {
        'event': {
            'createdAt': now,
            'detail': {
                'coordinate': {
                    'latitude': 31.245038,
                    'longitude': 121.634426,
                    'standard': 'BD09LL',
                    'timestamp': now
                }
            },
            'source': 'DRIVER',
            'type': 'ARRIVE_DROP_OFF'
        }
    }
    resp = requests.post(url2, json=body, headers=headers)
    print(resp.json())


# 发送派件事件
def send_drop_off_event(uuid, delivered_verify_code):
    url2 = url % uuid
    headers = {'PushEnvelope-Device-Token': access_token, 'Content-Type': 'application/json'}
    now = time.strftime("%Y-%m-%dT%H:%M:%S.%u+0800", time.localtime())
    body = {
        'event': {
            'createdAt': now,
            'detail': {
                'coordinate': {
                    'latitude': 31.245038,
                    'longitude': 121.634426,
                    'standard': 'BD09LL',
                    'timestamp': now
                },
                'verification': delivered_verify_code,
                'option': 'RECEIVER'
            },
            'source': 'DRIVER',
            'type': 'DROP_OFF'
        }
    }

    resp = requests.post(url2, json=body, headers=headers)
    print(resp.json())


if __name__ == '__main__':
    with open("aa.json", encoding='utf-8') as fr:
        content = fr.read()
        datas = json.loads(content)
        for data in datas["RECORDS"]:
            print(data["uuid"])
            print(data["code"])
            try:
                send_arrive_drop_off_event(data["uuid"])
                send_drop_off_event(data["uuid"], data["code"])
            except Exception as e:
                print(e)
