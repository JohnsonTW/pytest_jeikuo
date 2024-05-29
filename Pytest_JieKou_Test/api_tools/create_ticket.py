import logging
from Config.config_init import read_config
from common.files_util import create_file
from common.random_def import read_yaml, get_random_digits
from common.requests_def import requests_def

host = read_config("env", "test")


def create_ticket():
    body = requests_def(method="post", url=host + "/cgi-bin/qrcode/create",
                        params={'access_token': read_yaml("access_token.yaml")},
                        json={"action_name": "QR_LIMIT_SCENE",
                              "action_info": {"scene": {"scene_id": get_random_digits(1, 100000)}}
                              })
    logging.info("调用[创建永久二维码ticket]接口，提取ticket参数-接口响应结果：" + str(body.json()))
    ticket = body.json()["ticket"]
    create_file("ticket.yaml",ticket)
    return ticket
