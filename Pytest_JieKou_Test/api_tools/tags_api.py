import logging
from Config.config_init import read_config
from common.random_def import get_random_digits, generate_random_string, read_yaml
from common.requests_def import requests_def

host = read_config("env", "test")
select_tags_url = read_config("api", "select_tags_url")
delete_tags_url = read_config("api", "delete_tags_url")
add_tags_url = read_config("api", "add_tags_url")


def select_tags():
    body = requests_def(method="get", url=host+select_tags_url,
                        params={'access_token': read_yaml("access_token.yaml")})
    tags = body.json()['tags']
    # 所有的用户标签id都在列表 all_tag_id
    all_tag_id = []
    for i in range(len(tags)):
        # 追加
        all_tag_id.append(tags[i]["id"])
    # 根据tags的总数长度，随机生成这个长度范围内的一个id，对标签下粉丝列表进行查询
    i = get_random_digits(0, len(all_tag_id)-1)
    ID = str(all_tag_id[int(i)])
    logging.info("调用查询用户标签接口，获取测试参数-接口响应结果：" + str(body.json()))
    return ID


def del_tags(del_id):
    body = requests_def(method="post", url=host + delete_tags_url,
                        params={'access_token': read_yaml("access_token.yaml")},
                        json={"tag": {"id": del_id}})
    logging.info("调用删除接口，清除测试数据-接口响应结果：" + str(body.json()))


def add_tags():
    body = requests_def(method="post", url=host + add_tags_url,
                        params={'access_token': read_yaml("access_token.yaml")},
                        json={"tag": {"name": generate_random_string(30)}})
    logging.info("调用新增用户标签接口，创建测试数据-接口响应结果：" + str(body.json()))
    ID = body.json()["tag"]['id']
    return ID
