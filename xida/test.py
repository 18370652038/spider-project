import execjs
import requests
import time
from bs4 import BeautifulSoup


def get_cookie():
    username = ''
    password = ''

    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    url1 = 'http://cas.swust.edu.cn/authserver/login'

    h = session.get(url=url1,headers=headers)
    soup = BeautifulSoup(h.text,'html.parser')
    execution = soup.select('input[name="execution"]')[0].attrs.get('value')

    getKey = 'http://cas.swust.edu.cn/authserver/getKey'
    h = session.get(url=getKey,headers=headers)
    # print(h.json())
    Modulus = h.json()['modulus']


    captcha = 'http://cas.swust.edu.cn/authserver/captcha?timestamp={}'.format(int(time.time()*1000))
    h = session.get(url=captcha,headers=headers)
    with open('captcha.jpg','wb+')as f:
        f.write(h.content)

    with open('security.js','r+')as f:
        result = f.read()

    ctx = execjs.compile(result,cwd=r'C:\Users\Administrator\AppData\Roaming\npm\node_modules')
    password = ctx.call('aaaa',Modulus,password)
    print(password)

    yzm = input('验证码：')
    login = 'http://cas.swust.edu.cn/authserver/login?service=http://myo.swust.edu.cn/mht_shall/a/service/serviceFrontManage/cas'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "http://cas.swust.edu.cn/authserver/login?service=http://myo.swust.edu.cn/mht_shall/a/service/serviceFrontManage/cas"
    }
    m = {
        "execution": execution,
        "_eventId": "submit",
        "geolocation": "",
        "username": username,
        "lm": "usernameLogin",
        "password": password,
        "captcha": yzm
    }
    h = session.post(url=login,headers=headers,data=m,verify=False)
    # print(session.cookies.get_dict())
    print(h.text)
    return session.cookies.get_dict()

if __name__ == '__main__':
    print(get_cookie())
