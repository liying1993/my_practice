import os, sys, platform
import requests, time, re, subprocess
import json, xml.dom.minidom

uuid = None
BASE_URL = "https://login.weixin.qq.com"
session = requests.Session()
OS = platform.system()
path = "/Users/liying/Downloads/QR.jpg"


def get_QRuuid():
    url = 'https://login.weixin.qq.com/jslogin'
    params = {
        "appid": "wx782c26e4c19acffb",
        "redirect_uri": "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage",
        "fun": "new",
        "lang": "zh_CN",
        "_": int(time.time())
    }
    r = session.get(url, params=params)
    regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)";'
    data = re.search(regx, r.text)
    if data and data.group(1) == '200': return data.group(2)


def get_QR():
    url = "%s/qrcode/%s" % (BASE_URL, uuid)
    r = session.get(url, stream=True)
    with open(path, "wb") as f:
        f.write(r.content)
    if OS == "Darwin":
        subprocess.call(['open', path])
    elif OS == "Linux":
        subprocess.call(['xdg-open', path])
    else:
        OS.startfile(path)


def check_login(uuid):
    url = '%s/cgi-bin/mmwebwx-bin/login' % BASE_URL
    payloads = "loginicon=true&uuid=%s&tip=0&r=1699846821&_=%s" % (uuid, int(time.time()))
    r = session.get(url, params=payloads)
    regx = r"window.code=(\d+)"
    data = re.search(regx, r.text)
    if not data: return False
    def one_line_print(msg):
        sys.stdout.write('%s\r'%msg)
        sys.stdout.flush()
    if data.group(1) == '200':
        regx = r'window.redirect_uri="(\S+)"'
        global INTERACT_URL
        INTERACT_URL = re.search(regx, r.text).group(1)
        r = session.get(INTERACT_URL, allow_redirexts=False)
        INTERACT_URL = INTERACT_URL[:INTERACT_URL.rfind('/')]
        get_login_info(r.text)
        return True
    elif data.group(1) == '201':
        one_line_print('please press confirm')
    elif data.group(1) == '408':
        one_line_print('Please reload QR Code')
    return False

def get_login_info(s):
    global baseRequest
    for node in xml.dom.minidom.parseString(s).documentElement.childsNodes:
        if node.nodeName == 'skey':
            baseRequest['SKey'] = node.childNodes[0].data.encode('utf8')
        elif node.nodeName == 'wxsid':
            baseRequest['Sid'] = node.childNodes[0].data.encode('utf8')
        elif node.nodeName == 'wxuin':
            baseRequest['Uin'] = node.childNodes[0].data.encode('utf8')
        elif node.nodeName == 'pass_ticket':
            baseRequest['DeviceID'] = node.childNodes[0].data.encode('utf8')

def web_init():
    url = '%s/webwxinit?r=%s'%(INTERACT_URL, int(time.time()))
    payloads = {
        'BaseRequest': baseRequest,
    }
    headers = {'ContentType': 'application/json; charset=UTF-8'}
    r = session.post(url, data=json.dumps(payloads), headers=headers)
    dic = json.loads(r.content.decode('utf-8', 'replace'))
    return dic['User']['UserName']

def send_msg(toUserName=None, msg='Test Message'):
    url = '%s.webwxsendmsg'%INTERACT_URL
    payloads = {
        'BaseRequest': baseRequest,
        'Msg': {
            'Type': 1,
            'Content': msg.encode('utf8'),
            'FromUserName': myUserName.encode('utf8'),
            'ToUserName': (toUserName if toUserName else myUserName).encode('utf-8'),
            'LocalID':int(time.time()),
            'ClientMsgId': int(time.time())
        },
    }
    headers = {'ContentType': 'text/plain; charset=UTF-8'}
    session.post(url, data=json.dumps(payloads,ensure_ascii=False), headers=headers)
if __name__ == '__main__':
    while not uuid: uuid = get_QRuuid()
    get_QR()
    while not check_login(uuid): pass
    myUserName = web_init()
    print('Login successfully you can send message now, input q to exit')
    msg = ''
    while msg != 'q':
        if msg:send_msg(myUserName, msg)
        msg = input('>').encode(sys.stdin.encoding)
    print('Have fun')
    # myUserName = web_init()
    # msg = None
    # while msg != "q":
    #     if msg:send_msg(myUserName, msg)
    #     msg = input(">").decode(sys.stdin.encoding)
    # print("have fun")











# session = requests.Session()
# url = 'https://login.weixin.qq.com/jslogin'
# params = {
#     "appid": "wx782c26e4c19acffb",
#     "redirect_uri": "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage",
#     "fun": "new",
#     "lang": "zh_CN",
#     "_": int(time.time())
# }
# r = session.get(url, params=params)
# # print(r.text)
# #上面的代码就是像微信提交参数，申请登录的二维码
# #==============================================================
#
#
# regx = r"window.QRLogin.code = (\d+); window.QRLogin.uuid = '(\S+?)';"
# data = re.search(regx, r.text)
# if data and data.group(1) == '200':uuid = data.group(2)
# print(uuid)
# #上面的代码获得uuid
#
# url = 'http://login.weixin.qq.com/qrcode/'+uuid
# r = session.get(url, stream=True)
# with open("QRCode.jpg", "wb") as f:f.write(r.content)
# import platform, os, subprocess
# if platform.system() == "Darwin":
#     subprocess.call(['open', "QRCode.jpg"])
# elif platform.system() == "Linux":
#     subprocess.call(["xdg-open", "QRCode.jpg"])
# else:
#     os.startfile("QR.jpg")
