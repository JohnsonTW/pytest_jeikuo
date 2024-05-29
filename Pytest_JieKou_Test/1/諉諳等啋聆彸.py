import requests
from common.Assert import assret_in_text

url = "https://api.weixin.qq.com/cgi-bin/token"

param = {
    "appid": "wx8419d850fbd9f70e",
    "secret": "3a6dcf6ba33cd5b954574036111f1373",
    "grant_type": "client_credential"
}

body = requests.request(method="get", url=url, params=param)
# 内置函数，控制台打印
print(body.json())
print(body.status_code)

# assret_in_text("测试用例1", body.json(), "expires_in222")
