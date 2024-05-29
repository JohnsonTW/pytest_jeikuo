import logging
import allure
import pytest
from Config.config_init import read_config
from api_tools.tags_api import del_tags
from common.Assert import assret_in_text, assret_body, assret_statusCode
from common.requests_def import requests_def
from common.yaml_util import read_testCase


@allure.epic("微信项目")
@allure.feature('用户标签管理模块')
class Test_userTag:
    @allure.story("创建用户标签接口")
    @pytest.mark.parametrize('args', read_testCase('user_tags\\create_tags.yaml'))
    def test_CreateTag(self, args, session_fixture):
        token = session_fixture
        with allure.step("执行接口"):
            body = requests_def(args['method'], read_config("env", "test") + args['url'],
                                params={'access_token': token},
                                json=args['data'])
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("断言响应体"):
            if "tag" in body.json():
                with allure.step("断言:验证新增name是否与预期一致"):
                    assert body.json()['tag']['name'] == args['data']['tag']['name']
                    logging.info('实际name与预期一致，【实际name】：' + str(body.json()['tag']['name']) +
                                 "，【预期name】" + str(args['data']['tag']['name']))
                with allure.step("清除测试数据"):
                    del_tags(str(body.json()['tag']['id']))
            else:
                with allure.step("断言：errcode是否与预期结果一致"):
                    assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                with allure.step("断言：errmsg是否与预期结果一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
