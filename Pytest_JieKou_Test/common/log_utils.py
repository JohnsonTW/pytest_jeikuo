# 日志生成配置文件
import datetime
import json
import logging

from Config.config_init import read_config

data = datetime.date.today()


def get_logger():
    # 创建日志对象
    logger = logging.getLogger("logging")
    # 设置默认的日志级别DEBUG,代表获取DEBUG及DEBUG级别以上的日志
    logger.setLevel("DEBUG")
    # 设置输出方向
    # 输出到控制台,并且级别INFO,代表INFO及INFO级别以上的内容
    sh1 = logging.StreamHandler()
    # 代表输出INFO及INFO级别以上的内容
    sh1.setLevel("DEBUG")
    # log的路径
    path_log = read_config("path", "log_path")
    # 1、输出到 ./info.log 文件,并且内容追加写入,并且级别INFO,代表INFO及INFO级别以上的内容
    sh2 = logging.FileHandler(path_log + "\\" + str(data) + "_info.log", mode='a+', encoding='utf-8')
    sh2.setLevel("INFO")
    # user_manage、输出到 ./error.log 文件,并且内容追加写入,并且级别ERROR,代表ERROR及ERROR级别以上的内容
    sh3 = logging.FileHandler(path_log + "\\" + str(data) + "_error.log", mode='a+', encoding='utf-8')
    sh3.setLevel("ERROR")
    # 添加输出方向到logger对象
    logger.addHandler(sh1)
    logger.addHandler(sh2)
    logger.addHandler(sh3)
    # 指定日志输出格式
    fmt_str = json.dumps(
        {"CreateTime": "%(asctime)s", "filename": "%(filename)s", "line": "%(lineno)d", "levelname": "%(levelname)s",
         "message": "%(message)s"})
    # 设置样式
    my_fmt = logging.Formatter(fmt_str, datefmt='%Y-%m-%d %H:%M:%S')
    sh1.setFormatter(my_fmt)
    sh2.setFormatter(my_fmt)
    sh3.setFormatter(my_fmt)
    return logger


# 对日志方法，实例化成对象
logger = get_logger()


# 清空原有的日志info
def clear_logger():
    path_log = read_config("path", "log_path")
    info_log = path_log + "\\" + str(data) + "_info.log"
    error_log = path_log + "\\" + str(data) + "_error.log"

    with open(info_log, mode='r+') as f:
        f.truncate(0)
    with open(error_log, mode='r+') as f:
        f.truncate(0)
