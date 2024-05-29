from api_tools.create_ticket import create_ticket
from api_tools.get_token import get_token
from api_tools.tags_api import select_tags, add_tags
from api_tools.user_api import select_user_list
from common.random_def import get_random_digits, generate_random_string, read_yaml, get_kf_account


# 递归地遍历一个数据结构（字典、列表、字符串），并在其中查找特定的占位符，将其替换为动态生成的值。
def replace_dynamic_values(data):
    # isinstance是Python中的一个内置函数，
    # 遍历检查指定的数据类型实际上是否与预期的一致
    if isinstance(data, dict):
        # 遍历字典中的每个键值对（k, v），并对每个值（v）应用 replace_dynamic_values 函数
        # 这个函数会递归地应用于字典中的每个值，直到所有的动态值都被替换
        # 字典推倒式
        return {k: replace_dynamic_values(v) for k, v in data.items()}
    elif isinstance(data, list):
        # replace_dynamic_values()这个函数会递归地应用于数组中的每个值
        # 直到所有的动态值都被替换
        return [replace_dynamic_values(item) for item in data]
    elif isinstance(data, str):
        # 检查字符串是否包含函数调用
        if data.startswith('${') and data.endswith('}'):
            # split('(') 方法被用来查找左括号 ( 并将字符串分割成两部分：函数名和参数列表
            # split('(') 中的 '(' 是分隔符，1表示只分割一次
            # 函数名会是最左边的部分，而参数会是最右边的部分（包括左括号）
            func_name, args = data[2:-1].split('(', 1)
            # 从args的开头到倒数第2个字符的所有内容 :  read_yaml(update_user_remark.yaml)
            args = args[:-1]
            if func_name == 'get_random_digits':
                min_digits, max_digits = map(int, args.split(','))
                return get_random_digits(min_digits, max_digits)
            elif func_name == 'generate_random_string':
                length = int(args)
                return generate_random_string(length)
            elif func_name == 'read_yaml':
                yaml_name = str(args)
                return read_yaml(yaml_name)
            elif func_name == 'get_token':
                return get_token()
            elif func_name == 'select_tags':
                return select_tags()
            elif func_name == 'add_tags':
                return add_tags()
            elif func_name == 'select_user_list':
                return select_user_list()
            elif func_name == 'create_ticket':
                return create_ticket()
            elif func_name == 'get_kf_account':
                return get_kf_account()
        return data
    else:
        return data
