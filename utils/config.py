import os
from utils.file_reader import YamlReader


BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yaml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRAIVE_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).get_config

    def get(self, element, index=0):
        return self.config[index].get(element)



# #调试脚本
# driver_path = Config().get('driver_path')
