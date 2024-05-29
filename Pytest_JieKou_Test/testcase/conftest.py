import pytest
from Config.config_init import read_config
from common.files_util import remove_all_file
from common.random_def import read_yaml

Data_path = read_config("path", "Data_path")
log_path = read_config("path", "log_path")
param_path = read_config("path", "param_path")
host = read_config("env", "test")


# autouse=True意味着fixture会自动使用，
# 不需要在测试函数的参数中显式声明

# 定义好了前后置之后，需要在其他文件调用使用
@pytest.fixture(scope='session')
def session_fixture():
    # 获取token，前置条件/操作，测试开始之前，需要准备的操作
    token = read_yaml("access_token.yaml")
    yield token
    # 后置操作
    # 测试数据清除，测试结束之后，需要做的操作
    # remove_all_file(param_path)
