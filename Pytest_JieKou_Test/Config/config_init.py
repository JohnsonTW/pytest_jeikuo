import configparser


def read_config(section, key):
    # 先处理配置文件的路径
    cfg_path = r"D:\Python_Code\Pytest_JieKou_Test\Config\config.ini"
    # 1.创建配置文件对象
    conf = configparser.ConfigParser()
    # 读取配置文件
    conf.read(cfg_path, encoding='utf-8')
    value = conf.get(section, key)
    return value


# print(read_config("email", "user"))
