import random
import string
import yaml
from Config.config_init import read_config

base_path = read_config("path", "Data_path")
param_path = read_config("path", "param_path")


def get_random_digits(min_number, max_number):
    return str(random.randint(int(min_number), int(max_number)))


def generate_random_string(length):
    # 参数:length (int): 要生成的随机字符串的长度，默认为6
    # 返回: str: 生成的随机字符串
    # 定义了允许的字符集合 characters: 它包括字母（大小写:string.ascii_letters）和数字:string.digits
    characters = string.ascii_letters + string.digits
    # random.choice(characters)：这部分代码使用random.choice()函数从字符集characters中随机选择一个字符
    # for _ in range(length)：循环，执行 length 次，每次迭代都会随机选择一个字符
    # ''.join(...)：使用join()方法将所有选择的字符连接在一起，形成最终的随机字符串
    random_string = ''.join(random.choice(characters) for _ in range(int(length)))
    return random_string


def read_yaml(yaml_name):
    with open(param_path + "\\" + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value


# 格式为：账号前缀@公众号微信号，账号前缀最多10个字符，必须是英文、数字字符或者下划线，后缀为公众号微信号，长度不超过30个字符
def get_kf_account():
    join_str = "_@"
    star_str = generate_random_string(9)
    end_str = generate_random_string(30)
    kf_account = star_str + join_str + end_str
    return kf_account

