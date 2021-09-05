import requests
from bs4 import BeautifulSoup
import base64

url = 'https://match.yuanrenxue.com/match/1'

session = requests.session()

headers = {
    "User-Agent": "yuanrenxue.project"
}


h = session.get(url,headers=headers,verify=False)
print(h)
print(session.cookies.get_dict())
session.cookies.set('sessionid','zt5jid1j4lkip4tz4cotm6fycn628je4')


nums = 0
a = 0
for i in range(1,6):
    url = 'https://match.yuanrenxue.com/api/match/12?page={}&m='.format(i)+str(base64.b64encode('yuanrenxue{}'.format(i).encode('utf-8')),'utf-8')
    print(url)
    h = session.get(url,headers=headers,verify=False)
    print(h.json())
    for resu in h.json()['data']:
        nums += list(resu.values())[0]
        a += 1
    print(nums)
print(nums/a)