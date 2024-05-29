import allure
import pytest
from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
from common.requests_def import requests_def
from common.yaml_util import read_testCase

kf_account = None

@allure.epic("微信项目")
@allure.feature('客服管理模块')
class Test_kf:
    @allure.story("创建客服账号接口")
    @pytest.mark.parametrize('args', read_testCase('kf_mannage\\create_kf.yaml'))
    def test_create_kf(self, args, session_fixture):
        token = session_fixture
        with allure.step("执行接口"):
            body = requests_def(args['method'], read_config("env", "test") + args['url'],
                                params={'access_token': token},
                                json=args['data'])
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("断言响应体"):
            with allure.step("断言：errcode是否与预期结果一致"):
                assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
            with allure.step("断言：errmsg是否与预期结果一致"):
                assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
            if body.json()['errmsg'] == "ok":
                with allure.step("提取创建成功了的客服账号："):
                    global kf_account
                    kf_account = args['data']['kf_account']

    @allure.story("设置客服信息接口")
    @pytest.mark.parametrize('args', read_testCase('kf_mannage\\update_kf.yaml'))
    def test_uptate_kf(self, args, session_fixture):
        token = session_fixture
        if args['excepted']['errmsg'] == "ok":
            with allure.step("执行接口"):
                body = requests_def(args['method'], read_config("env", "test") + args['url'],
                                    params={'access_token': token},
                                    json={"kf_account":kf_account,"nickname":args['nickname']})
                assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

            with allure.step("断言响应体"):
                with allure.step("断言：errcode是否与预期结果一致"):
                    assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                with allure.step("断言：errmsg是否与预期结果一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
        else:
            with allure.step("执行接口"):
                body = requests_def(args['method'], read_config("env", "test") + args['url'],
                                    params={'access_token': token},
                                    json=args['data'])
                assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

            with allure.step("断言响应体"):
                with allure.step("断言：errcode是否与预期结果一致"):
                    assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                with allure.step("断言：errmsg是否与预期结果一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])

    @allure.story("删除客服账号接口")
    @pytest.mark.parametrize('args', read_testCase('kf_mannage\\del_kf.yaml'))
    def test_del_kf(self, args, session_fixture):
        token = session_fixture
        if args['excepted']['errmsg'] == "ok":
            with allure.step("执行接口"):
                body = requests_def(args['method'], read_config("env", "test") + args['url'],
                                    params={'access_token': token, 'kf_account': kf_account})
                assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

            with allure.step("断言响应体"):
                with allure.step("断言：errcode是否与预期结果一致"):
                    assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                with allure.step("断言：errmsg是否与预期结果一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
        else:
            with allure.step("执行接口"):
                body = requests_def(args['method'], read_config("env", "test") + args['url'],
                                    params={'access_token': token, 'kf_account': args['params']['kf_account']})
                assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

            with allure.step("断言响应体"):
                with allure.step("断言：errcode是否与预期结果一致"):
                    assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                with allure.step("断言：errmsg是否与预期结果一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])

    @allure.story("获取客服基础信息接口")
    @pytest.mark.parametrize('args', read_testCase('kf_mannage\\get_kf_list.yaml'))
    def test_select_kf_list(self, args, session_fixture):
        token = session_fixture
        with allure.step("执行接口"):
            body = requests_def(args['method'], read_config("env", "test") + args['url'],
                                params={'access_token': token})
            assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

        with allure.step("断言响应体"):
            assret_in_text(args['caseName'], body.json(), args['excepted']['text1'])
            assret_in_text(args['caseName'], body.json(), args['excepted']['text2'])
            assret_in_text(args['caseName'], body.json(), args['excepted']['text3'])
            assret_in_text(args['caseName'], body.json(), args['excepted']['text4'])
