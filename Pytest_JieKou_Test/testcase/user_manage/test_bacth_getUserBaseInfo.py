from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
import allure
import pytest
from common.requests_def import requests_def
from common.yaml_util import read_testCase


@allure.epic("微信项目")
@allure.feature('用户管理模块')
class Test_user_manage:
    @pytest.mark.parametrize('args', read_testCase('user_manage\\batch_get_user_info.yaml'))
    @allure.story("批量获取用户基础信息接口")
    def test_bacth_getUserBaseInfo(self, args,session_fixture):
        token = session_fixture
        with allure.step("执行接口"):
            body = requests_def(args['method'], url=read_config("env", "test") + args['url'],
                                params={"access_token": token}, json=args['data'])
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("响应体断言"):
            if "errcode" in body.json():
                with allure.step("errcode的实际结果是否与预期一致"):
                    assret_body(args['caseName'], body, "errcode", args['excepted']['errcode'])
                with allure.step("errmsg的实际结果是否与预期一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
            else:
                assret_in_text(args['caseName'], body.json(), args['excepted']['text1'])
                assret_in_text(args['caseName'], body.json(), args['excepted']['text2'])

