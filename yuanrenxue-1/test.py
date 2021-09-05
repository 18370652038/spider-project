import requests
from bs4 import BeautifulSoup
import execjs

url = 'https://match.yuanrenxue.com/match/1'

session = requests.session()

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
# }

headers = {
    "User-Agent": "yuanrenxue.project"
}


h = session.get(url,headers=headers,verify=False)
print(h)
print(session.cookies.get_dict())
session.cookies.set('sessionid','zt5jid1j4lkip4tz4cotm6fycn628je4')



with open('111.js', 'r+',errors='ignore')as f:
    result = f.read()

ctx = execjs.compile(result, cwd=r'C:\Users\Administrator\AppData\Roaming\npm\node_modules')

nums = 0
a = 0
for i in range(1,6):
    times = str(execjs.eval("Date['\x70\x61\x72\x73\x65'](new Date()) + (16798545 + -72936737 + 156138192)"))
    sion = ctx.call('oo0O0',str(times))
    print(sion)
    print(sion + '丨'+str(times)[:-3])
    url = 'https://match.yuanrenxue.com/api/match/1?page={}&m={}'.format(i,sion + '丨'+str(times)[:-3])
    h = session.get(url,headers=headers,verify=False)
    print(h.json())
    for resu in h.json()['data']:
        nums += list(resu.values())[0]
        a += 1
    print(nums)
print(nums/a)