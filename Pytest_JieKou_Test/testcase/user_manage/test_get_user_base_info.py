import pytest
from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
import allure
from common.requests_def import requests_def
from common.yaml_util import read_testCase


@allure.epic("微信项目")
@allure.feature('用户管理模块')
class Test_user_manage:
    @pytest.mark.parametrize('args', read_testCase('user_manage\\get_user_base_info.yaml'))
    @allure.story("获取用户基本信息接口")
    def test_getUserBaseInfo(self, args,session_fixture):
        token = session_fixture
        with allure.step("执行接口"):
            body = requests_def(args['method'], url=read_config("env", "test") + args['url'],
                                params={"access_token": token,
                                        "openid":args['params']['openid']}
                                )
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("响应体验证"):
            if "errcode" in body.json():
                with allure.step("errcode的实际结果是否与预期一致"):
                    assret_body(args['caseName'], body, "errcode", args['excepted']['errcode'])
                with allure.step("errmsg的实际结果是否与预期一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
            else:
                with allure.step("openid的实际结果是否与预期一致"):
                    assret_body(args['caseName'], body, "openid", args['params']['openid'])
                with allure.step("language的实际结果是否与预期一致"):
                    assret_body(args['caseName'], body, "language", args['excepted']['language'])
