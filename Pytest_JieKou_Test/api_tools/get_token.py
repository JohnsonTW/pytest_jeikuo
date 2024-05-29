# 在模块顶部定义全局变量
from common.files_util import create_file
from Config.config_init import read_config
from common.requests_def import requests_def
import logging

host = read_config("env", "test")


def get_token():
    body = requests_def(method="get", url=host + "/cgi-bin/token",
                        params={'grant_type': read_config("env", "grant_type"),
                                "appid": read_config("env", "appid"),
                                "secret": read_config("env", "secret")})
    access_token = body.json()['access_token']
    logging.info("获取到了最新的 access_token：" + str(access_token))
    create_file("access_token.yaml", access_token)
    return access_token

# print(get_token())
