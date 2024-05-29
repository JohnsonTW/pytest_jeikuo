import allure
import pytest
from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
from common.requests_def import requests_def
from common.yaml_util import read_testCase


@allure.epic("微信项目")
@allure.feature('用户管理模块')
class Test_user_manage:
    @pytest.mark.parametrize('args', read_testCase('user_manage\\get_user_list.yaml'))
    @allure.story("获取用户列表接口")
    def test_getUserList(self, args,session_fixture):
        token = session_fixture
        with allure.step("执行接口"):
            body = requests_def(method=args['method'], url=read_config("env", "test") + args['url'],
                                params={"access_token": token,
                                        "next_openid":args['params']['next_openid']}
                                )
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("响应体断言"):
            if "total" in body.json():
                assret_in_text(args['caseName'], body.json(), args['excepted']['text1'])
                assret_in_text(args['caseName'], body.json(), args['excepted']['text2'])
                assret_in_text(args['caseName'], body.json(), args['excepted']['text3'])
            else:
                with allure.step("errcode实际结果是否与预期一致"):
                    assret_body(args['caseName'], body, "errcode", args['excepted']['errcode'])
                with allure.step("errmsg实际结果是否与预期一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])

