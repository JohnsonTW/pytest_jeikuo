from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
from common.requests_def import requests_def
from common.yaml_util import read_testCase
import allure
import pytest


@allure.epic("微信项目")
@allure.feature('用户标签管理模块')
class Test_userTag:
    @pytest.mark.parametrize('args', read_testCase("user_tags\\update_tag.yaml"))
    @allure.story("修改用户标签接口")
    def test_UpdateTag(self, args, session_fixture):
        token = session_fixture
        with allure.step("执行接口："):
            body = requests_def(args['method'], url=read_config("env", "test") + args['url'],
                                params={'access_token': token}, json=args['data'])
            assret_statusCode(args['caseName'], body.status_code, args['statusCode'])

        with allure.step("断言响应体"):
            assret_body(args['caseName'], body, 'errcode', args['errcode'])
            assret_in_text(args['caseName'], body.json(), args['errmsg'])
