import yaml
from Config.config_init import read_config
from common.replace_load import replace_dynamic_values

Data_path = read_config("path", "Data_path")
param_path = read_config("path", "param_path")


def read_yamlFile(yaml_name):
    with open(Data_path + "\\" + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value


def read_testCase(yamlName):
    with open(Data_path + "\\" + yamlName, mode="r", encoding="utf-8") as file:
        args = yaml.safe_load(file)
    # 替换动态值
    args = replace_dynamic_values(args)
    return args


def write_yaml(filename, value):
    with open(param_path + "\\" + filename, mode='w', encoding='utf-8') as f:
        f.write(str(value))


def clear_yaml(filename):
    with open(Data_path + "\\" + filename, mode='w', encoding='utf-8') as f:
        f.truncate()
