import base64
import hashlib
import requests
import time
import json
import urllib

requests.packages.urllib3.disable_warnings()


print(base64.b64decode('aHR0cHM6Ly9saXN0Lm1vZ3UuY29tL3NlYXJjaC9nb29kcz9xPSVFNSVCNyVBNSVFOCVBMyU4NSVFOCVBMyVBNA=='.encode('utf-8')))
#https://list.mogu.com/search/goods?q=%E5%B7%A5%E8%A3%85%E8%A3%A4


def z(gjc:str):
    m = hashlib.md5()
    m.update(gjc.encode('utf-8'))
    a = m.hexdigest()
    print(a)
    return a

session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

goods = 'https://list.mogu.com/search/goods?q=%E5%B7%A5%E8%A3%85%E8%A3%A4'
h = session.get(url=goods,headers=headers,verify=False)

getUuid = 'https://portal.mogu.com/api/util/getUuid?callback=callback_1001'
h = session.get(url=getUuid,headers=headers,verify=False)

back = int(time.time()*1000)
mget = 'https://list.mogu.com/module/mget?code=sketch&callback=httpCb{}18&_={}'.format(back,back)
h = session.get(url=mget,headers=headers,verify=False)
print(session.cookies.get_dict())

back = int(time.time()*1000)
baseinfo = 'https://portal.mogu.com/api/profile/baseinfo?needHttps=true&callback=httpCb{}28&_={}'.format(back,back)
h = session.get(url=mget,headers=headers,verify=False)
print(session.cookies.get_dict())

mw_t = str(int(time.time()*1000))
data1 = {"pids":"132244,138852,138851"}

result = ['100028','unknown',mw_t,'NMMain@mgj_pc_1.0','','mwp.darwin.multiget','3',z(json.dumps(data1)),'']
m = {
    'data': json.dumps(data1),
    'mw-appkey': 100028,
    'mw-ttid': 'NMMain@mgj_pc_1.0',
    'mw-t': mw_t,
    'mw-uuid': '',
    'mw-h5-os': 'unknown',
    'mw-sign': z('&'.join(result)),
    'callback': 'mwpCb1',
    '_': int(time.time()*1000)
}
multiget = 'https://api.mogu.com/h5/mwp.darwin.multiget/3/'
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Referer": "https://list.mogu.com/",
    "Host": "api.mogu.com"
}
h = session.get(url=multiget,headers=headers1,verify=False,params=m)
print(h.text)
print(session.cookies.get_dict())

search = 'https://api.mogu.com/h5/mwp.pagani.search/19/'
mw_t = str(int(time.time()*1000))
data2 = {"page":2,"pageSize":24,"sort":"pop","ratio":"3:4","cKey":"pc-search-wall","q":"%E5%B7%A5%E8%A3%85%E8%A3%A4","ptp":"31.nXjSr.0.0.PAtJ4WR8"}
result = ['100028','pc-search-wall','unknown',mw_t,'NMMain@mgj_pc_1.0',session.cookies.get_dict()['__mgjuuid'],'mwp.pagani.search','19',z(json.dumps(data2)),session.cookies.get_dict()['_mwp_h5_token']]
print('&'.join(result))

m = {
    'data': json.dumps(data2),
    'mw-ckey': 'pc-search-wall',
    'mw-appkey': 100028,
    'mw-ttid': 'NMMain@mgj_pc_1.0',
    'mw-t': mw_t,
    'mw-uuid': session.cookies.get_dict()['__mgjuuid'],
    'mw-h5-os': 'unknown',
    'mw-sign': z('&'.join(result)),
    'callback': 'mwpCb3',
    '_': int(time.time()*1000)
}
print(m)
headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Referer": "https://list.mogu.com/",
    "Host": "api.mogu.com",
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site'
}
h = session.get(url=search,headers=headers2,verify=False,params=m)
print(h.text)
print(h)
print(h.url)