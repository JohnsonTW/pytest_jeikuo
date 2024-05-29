import allure
import pytest
import requests
from Config.config_init import read_config
from common.Assert import assret_in_text, assret_body, assret_statusCode
from common.requests_def import requests_def
from common.yaml_util import read_testCase
from tools.image_type import is_imgs


@allure.epic("微信项目")
@allure.feature('客服管理模块')
class Test_kf:
    @allure.story("上传客服头像接口")
    @pytest.mark.parametrize('args', read_testCase('kf_mannage\\upload_head_img.yaml'))
    def test_upload_kf_headImg(self, args, session_fixture):
        token = session_fixture
        headImg_path = read_config("path", "imgs_path")
        file_name = args['files']['media']
        if is_imgs(headImg_path + "\\" + file_name):
            # 只有是有效的图片格式才需要去打开图片进行传参
            files = {
                "file": (
                    file_name, open(headImg_path + "\\" + file_name, "rb")
                )
            }
            with allure.step("执行接口"):
                body = requests_def(method=args["method"], url=read_config("env", "test") + args['url'],
                                    params={"access_token": token, "kf_account": args['params']['kf_account']},
                                    files=files)
                assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

                with allure.step("响应体断言"):
                    with allure.step("验证errcode是否与预期结果一致"):
                        assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                    with allure.step("验证errmsg是否与预期结果一致"):
                        assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])

        else:
            with allure.step("执行接口"):
                body = requests.request(method=args["method"], url=read_config("env", "test") + args['url'],
                                        params={"access_token": token, "kf_account": args['params']['kf_account']},
                                        files=args['files'])
                assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

            with allure.step("响应体断言"):
                with allure.step("验证errcode是否与预期结果一致"):
                    assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                with allure.step("验证errmsg是否与预期结果一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
