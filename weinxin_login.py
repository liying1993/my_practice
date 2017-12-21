import requests
import urllib.parse

data = {"appid": "wx0dd17375b6f636af","redirect_uri": "https://www.lansheng8.com/","response_type":"code", "scope":"snsapi_login"}
parse_uri = urllib.parse.urlencode(data)
print(parse_uri)
r = requests.get(f"https://open.weixin.qq.com/connect/qrconnect?{parse_uri}")
print(bytes(r.text, "utf-8"))
# return bytes(r.text, "utf-8")
# code = request.args.get("code")
data1 = {"appid":"wx0dd17375b6f636af","code": "001jScge2pKfRE07cVge2dxWfe2jScg2", "secret":"f5353a9e3b143f7dd119882f5c3aacc3", "grant_type":"authorization_code"}
r1 = requests.get("https://api.weixin.qq.com/sns/oauth2/access_token", data=data1)
data2 = {"access_toekn":r1.text.access_token, "openid":r1.text.access_token}
r2 = requests.get("https://api.weixin.qq.com/sns/userinfo", data=data2)


# https://open.weixin.qq.com/connect/qrconnect?appid=wx0dd17375b6f636af&redirect_uri=https%3A%2F%2Fwww.lansheng8.com%2F&response_type=code&scope=snsapi_login
# https://www.lansheng8.com/?code=001jScge2pKfRE07cVge2dxWfe2jScg2&state=
#https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx0dd17375b6f636af&secret=f5353a9e3b143f7dd119882f5c3aacc3&code=001jScge2pKfRE07cVge2dxWfe2jScg2&grant_type=authorization_code
# {"access_token":"5_F_15ha56g2mch92gQwIV1ZL17ZMSWQL1z2sRPu_ObS4thDyiq1a6pLlk8lOILR2RzwqrbAzpAJBLU0Y-Csv0NQ","expires_in":7200,"refresh_token":"5_liBilp9WLGKzR5iuqO1SAmR5E_t79dw-FBHp9lU9Q58lG9lfmz8X5TLK9m5KDAnM4qI4IDeq0GrtdUuvfeiT5g","openid":"os86_05v1KxaY3-WMggFHRPNdp6g","scope":"snsapi_login","unionid":"okxoY1EGP7LR9I4D1PxaKW14oMJM"}
# https://api.weixin.qq.com/sns/userinfo?access_token=5_F_15ha56g2mch92gQwIV1ZL17ZMSWQL1z2sRPu_ObS4thDyiq1a6pLlk8lOILR2RzwqrbAzpAJBLU0Y-Csv0NQ&openid=os86_05v1KxaY3-WMggFHRPNdp6g
# {"openid":"os86_05v1KxaY3-WMggFHRPNdp6g","nickname":"榛戝姞浠�","sex":1,"language":"zh_CN","city":"Bristol","province":"Hubei","country":"CN","headimgurl":"http:\/\/wx.qlogo.cn\/mmopen\/vi_32\/lpR8ysAEwLV9PQvk0K6H93UUd7GOrFw8EKLicpWaubjia9qPu5M7R8CbuM3mUReEsgxj5cEoGaYica1L3XUpE2dEQ\/0","privilege":[],"unionid":"okxoY1EGP7LR9I4D1PxaKW14oMJM"}
#
# 微信登录的整个过程：
# 1、后端请求链接https://open.weixin.qq.com/connect/qrconnect?appid=wx0dd17375b6f636af&redirect_uri=https%3A%2F%2Fwww.lansheng8.com%2F&response_type=code&scope=snsapi_login返回带二维码的HTML文件
# 2、用户扫描二维码，并确认登录之后，返回code
# 3、后端根据code请求access_token
# 4、后端获取access_token之后，请求https://api.weixin.qq.com/sns/userinfo，获取用户个人信息
# 5、获取用户信息如下