import logging
import os
from Config.config_init import read_config

param_path = read_config("path", "param_path")


def create_file(file_name, info):
    with open(param_path + "\\" + file_name, 'w') as f:
        f.write(info)
    # 检查文件是否创建成功
    if os.path.exists(param_path + "\\" + file_name):
        logging.info(f"文件 {file_name} 创建成功。")
    else:
        logging.info(f"文件 {file_name} 创建失败。")


def remove_file(fileName):
    # 检查文件是否存在，然后删除它
    if os.path.exists(param_path + "\\" + fileName):
        os.remove(param_path + "\\" + fileName)
        logging.info("文件【" + fileName + "】已成功删除")
    else:
        logging.info("文件【" + fileName + "】不存在")


def remove_all_file(path):
    # 遍历目录中的所有文件和文件夹
    for filename in os.listdir(path):
        # 构建完整的文件路径
        file_path = os.path.join(path, filename)
        # 检查是否为文件
        if os.path.isfile(file_path):
            # 删除文件
            os.remove(file_path)
            logging.info(f'文件 {file_path} 已成功删除.')



