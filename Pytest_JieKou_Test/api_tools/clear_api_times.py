from Config.config_init import read_config
from common.random_def import read_yaml
from common.requests_def import requests_def

host = read_config("env", "test")
appid = read_config("env", "appid")


# 清空api的调用quota
# 本接口用于清空微信公众号平台接口的每日调用接口次数
# 每个账号每月共10次清零操作机会，清零生效一次即用掉一次机会
# 由于指标计算方法或统计时间差异，实时调用量数据可能会出现误差，一般在1%以内


def clear_api_times():
    body = requests_def(method="post", url=host + "/cgi-bin/clear_quota",
                        params={'access_token': read_yaml("access_token.yaml")},
                        json={"appid": appid})
    return body.json()

# print(clear_api_times())
