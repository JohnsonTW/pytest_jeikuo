# PIL库是一个Python的图像处理库
import logging
from PIL import Image


def is_imgs(imgName):
    try:
        # 指定的文件并将其作为一个图像对象打开。
        # 如果文件不能被正确地打开或不是图像文件，那么将会抛出一个异常
        with Image.open(imgName) as img:
            # 这个方法会检查图像文件的完整性。
            # 如果文件不能被正确地打开或不是有效的图像文件，那么这个方法将会抛出一个异常。
            img.verify()
            # 获取图片格式
            format = img.format
            logging.info("该图片的格式为：" + format)
        return True

    except (IOError, SyntaxError) as e:
        logging.info("该文件不是一张图片")
        return False


# print(is_imgs("D:\Python_Code\Pytest_JieKou_Test\imgs\测试.txt"))
