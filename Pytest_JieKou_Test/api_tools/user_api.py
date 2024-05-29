import logging
from common.random_def import get_random_digits, read_yaml
from Config.config_init import read_config
from common.requests_def import requests_def

host = read_config("env", "test")
select_user_list_url = read_config("api", "select_user_list_url")


# OPENID不填默认从头开始拉取
def select_user_list():
    body = requests_def(method="get", url=host + select_user_list_url,
                        params={'access_token': read_yaml("access_token.yaml"),
                                "next_openid": ""})
    logging.info("调用【查询用户列表】接口，创建测试数据-接口响应结果：" + str(body.json()))
    # openid_list：全部的 openid
    openid_list = body.json()['data']['openid']
    # 随机取一个openid
    i = get_random_digits(0, len(openid_list) - 1)
    openid = openid_list[int(i)]
    return openid

# print(select_user_list())
