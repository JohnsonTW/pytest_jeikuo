import allure
import pytest
from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
from common.requests_def import requests_def
from common.yaml_util import read_testCase


@allure.epic("微信项目")
@allure.feature('黑名单管理模块')
class Test_userBlack:
    @pytest.mark.parametrize('args', read_testCase('black_manage\\batch_user_to_black.yaml'))
    @allure.story("拉黑用户至黑名单接口")
    def test_batch_blackList(self, args, session_fixture):
        token = session_fixture
        with allure.step("执行接口"):
            body = requests_def(method=args['method'], url=read_config("env", "test") + args['url'],
                                params={"access_token": token}, json=args['data'])
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("响应体断言"):
            assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
            assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
