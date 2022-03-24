import os
import unittest
from utils.config import Config
from utils.log import Logger


class BaseCase(unittest.TestCase):

    URL = Config().get('URL')
    base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
    # driver_path = os.path.abspath(base_path+'\drivers\chrromedriver.exe') # 之前直接将Chromedriver的地址指定在这里,可灵活更改
    driver_path = r"E:\代码空间\auto_test_framework\drivers\chromedriver.exe"
    # driver_path = Config().get('driver_path')
    log = Logger()
    pass
