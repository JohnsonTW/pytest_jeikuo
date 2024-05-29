import pytest
from common.requests_def import requests_def
from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
from common.yaml_util import read_testCase
import allure


@allure.epic("微信项目")
@allure.feature('黑名单管理模块')
class Test_userBlack:
    @pytest.mark.parametrize('args', read_testCase('black_manage\\black_List.yaml'))
    @allure.story("获取微信黑名单")
    def test_getUserList(self, args,session_fixture):
        token = session_fixture
        with allure.step(args['caseName']):
            body = requests_def(method=args['method'], url=read_config("env", "test") + args['url'],
                                params={"access_token": token}, json=args['data'])

            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("响应体断言"):
            if "errcode" in body.json():
                with allure.step("验证errcode是否与预期结果一致"):
                    assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                with allure.step("验证errcode是否与预期结果一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])

            else:
                assret_in_text(args['caseName'], body.json(), args['excepted']['text1'])
                assret_in_text(args['caseName'], body.json(), args['excepted']['text2'])
