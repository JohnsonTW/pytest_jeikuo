import allure
import pytest
from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
from common.files_util import create_file
from common.requests_def import requests_def
from common.yaml_util import read_testCase


# 账号管理 /生成带参数的二维码
# 每次创建二维码，ticket需要提供一个开发者自行设定的参数（scene_id），
# 分别介绍临时二维码和永久二维码的创建二维码ticket过程

@allure.epic("微信项目")
@allure.feature('账号管理')
class Test_qrcode:
    @pytest.mark.parametrize('args', read_testCase('qrcode\\create_ticket.yaml'))
    @allure.story("创建永久二维码ticket接口")
    def test_create_ticket(self, args, session_fixture):
        token = session_fixture
        with allure.step("执行接口"):
            body = requests_def(method=args['method'], url=read_config("env", "test") + args['url'],
                                params={"access_token": token}, json=args['data'])
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("响应体断言"):
            if "errcode" in body.json():
                assret_body(args['caseName'], body, "errcode", args['excepted']['errcode'])
                assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
            else:
                with allure.step("验证实际结果中是否成功返回ticket、二维码url"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['text1'])
                    assret_in_text(args['caseName'], body.json(), args['excepted']['text2'])
                with allure.step("提取ticket"):
                    create_file("ticket.yaml", body.json()['ticket'])
                with allure.step("提取二维码url"):
                    create_file("ticket_url.yaml", body.json()['url'])

    @pytest.mark.parametrize('args', read_testCase('qrcode\\show_qrcode.yaml'))
    @allure.story("通过ticket换取二维码接口")
    def test_by_ticket_get_qrcode(self, args):
        with allure.step("执行接口"):
            body = requests_def(method=args['method'], url=args['url'],
                                params=args['params'])
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

            # 检查响应内容（二进制数据）
            if body.headers['Content-Type'] == args['excepted']['http_response_header']:
                # 对于图片等二进制数据，应该使用content属性
                print("响应内容包含二进制数据：(image/jpeg).")
                # 保存图片：
                with open(read_config("path", "param_path") + "\\" + 'qrcode.jpg', 'wb') as f:
                    f.write(body.content)
            else:
                # 如果响应是文本数据，可以使用text属性
                print(body.text)
