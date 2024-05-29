import os
import pytest
from api_tools.get_token import get_token

# from common.send_email import send_email
# from time import sleep

# 主执行函数
if __name__ == '__main__':
    get_token()
    pytest.main()
    # pytest.main(["-vs", "./testcase/qrcode"])
    os.system('allure generate ./temp_JsonReport -o ./report --clean')
    # sleep(1)
    # send_email()
