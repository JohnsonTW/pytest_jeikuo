from PIL import Image
from common.log_utils import logger


def open_files(file_path):
    with open(file_path, 'rb') as f:
        files = {"files_buffer": f}
        return files


def ImageType(filename):
    img = Image.open(filename)
    if img.format == "JPG" or "JPEG" or "PNG":
        logger.info("此文件的类型为：" + img.format)
        return True
    else:
        logger.info("此文件的类型不属于合格的图片类型！")
        return False
