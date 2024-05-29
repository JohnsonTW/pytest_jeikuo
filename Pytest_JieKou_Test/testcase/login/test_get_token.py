import pytest
from common.Assert import assret_body, assret_statusCode
from common.requests_def import requests_def
from common.yaml_util import read_testCase
from Config.config_init import read_config
import allure


@allure.epic("微信项目")
@allure.feature("登录模块")
class Test_geToken:
    @allure.story("获取token鉴权接口")
    # 数据驱动测试流程，pytest参数化（测试数据、测试用例）
    @pytest.mark.parametrize('args', read_testCase('get_token\\get_token_api.yaml'))
    def test_geToken(self, args):
        with allure.step("执行接口"):
            body = requests_def(method=args['method'], url=read_config("env", "test") + args['url'],
                                params=args['params'])
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("响应体断言"):
            if "errcode" in body.json():
                assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
            else:
                assret_body(args['caseName'], body, 'expires_in', args['excepted']['expires_in'])
