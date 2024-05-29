import allure
import pytest
from Config.config_init import read_config
from common.Assert import assret_body, assret_statusCode, assret_in_text
from common.files_util import create_file
from common.yaml_util import read_testCase
import requests
from tools.image_type import is_imgs


@allure.epic("微信项目")
@allure.feature('上传卡券')
class Test_upload_img:
    @pytest.mark.parametrize('args', read_testCase('kaquan\\kaquan.yaml'))
    @allure.story("上传卡券图片接口")
    def test_upload_img(self, args, session_fixture):
        token = session_fixture
        files_path = read_config("path", "files_path")
        file_name = args['files']['buffer']
        if is_imgs(files_path + "\\" + file_name) is True:
            # 只有是有效的图片格式才需要去打开图片进行传参,调用接口
            files = {
                "file": (
                    file_name, open(files_path + "\\" + file_name, "rb")
                )
            }
            with allure.step("执行接口"):
                body = requests.request(method=args["method"], url=read_config("env", "test") + args['url'],
                                        params={"access_token": token}, files=files)
                assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

            with allure.step("响应体断言"):
                if "errcode" in body.text:
                    with allure.step("验证errcode是否与预期结果一致"):
                        assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                    with allure.step("验证errmsg是否与预期结果一致"):
                        assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
                else:
                    with allure.step("验证响应body是否存在url"):
                        assret_in_text(args['caseName'], body.json(), args['excepted']['text1'])
                    with allure.step("提取url"):
                        create_file("url.yaml", body.json()['url'])

        else:
            # 不是图片格式直接判断，走异常流程，无需打开图片
            with allure.step("执行接口"):
                body = requests.request(method=args["method"], url=read_config("env", "test") + args['url'],
                                        params={"access_token": token},
                                        files=args["files"])
                assret_statusCode(args['caseName'], body.status_code, args['excepted']['statusCode'])

            with allure.step("响应体断言"):
                with allure.step("验证errcode是否与预期结果一致"):
                    assret_body(args['caseName'], body, 'errcode', args['excepted']['errcode'])
                with allure.step("验证errmsg是否与预期结果一致"):
                    assret_in_text(args['caseName'], body.json(), args['excepted']['errmsg'])
