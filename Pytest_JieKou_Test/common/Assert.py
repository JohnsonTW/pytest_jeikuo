from common.log_utils import logger
import json


# 验证接口响应body中任意属性的值是否与我的预期结果一致
def assret_body(caseName, body, msg, assret_txt):
    # caseName：测试用例名称
    # boby：响应body
    # msg：  需要判断的响应body里的任意字段/属性（实际结果）,,,,,,通过jsonpath获取、或通过正则去获取
    # assret_msg： 预期结果
    try:
        assert body.json()[msg] == assret_txt
        logger.info(caseName + "- 测试用例,执行成功！实际响应结果为：" + str(body.json()))
        return True

    except Exception as e:
        logger.error(caseName + ",执行失败！实际响应结果为：{}".format(body.json()[msg]) + ",预期结果为：{}".format(assret_txt))
        raise e


# 验证接口响应body中是否包含预期字符串文本
def assret_in_text(caseName, body_json, assret_info):
    # caseName：测试用例名称
    # boby：响应body
    # assret_msg： 预期结果
    try:
        # text： 响应body转换为字符串类型的（实际结果）
        text = json.dumps(body_json)
        # print("text的值是：",text)
        assert assret_info in text
        # 如果断言通过，就会生成正常日志内容
        logger.info(caseName + "- 测试用例,执行成功！实际响应结果为：" + text)
        return True

    except Exception as e:
        text = json.dumps(body_json)
        logger.error(caseName + ",执行失败！实际响应结果中不包含：{}".format(assret_info) + ",实际结果为：{}".format(text))
        raise e


# 200断言
def assret_statusCode(caseName, code, statusCode):
    #  code        实际的响应码
    #  statusCode  预期的响应码
    try:
        assert int(code) == statusCode
        logger.info(str(caseName) + "- 测试用例,执行成功！实际响应码为：" + str(code))
        return True

    except Exception as e:
        logger.error(str(caseName) + ",执行失败！实际响应码为：{}".format(str(code)) + ",预期响应码为：{}".format(str(statusCode)))
        raise e



