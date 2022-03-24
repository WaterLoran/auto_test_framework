import os
import yaml


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("自动化测试框架配置文件不存在")
        self.__data = None

    @property
    def get_config(self):
        if not self.__data:
            with open(self.yamlf, 'rb') as open_file:
                self.__data = list(yaml.safe_load_all(open_file))[0]  # 这里加一个0下标是因为的出来的数据外围有两层中括号
            open_file.close()
        return self.__data



