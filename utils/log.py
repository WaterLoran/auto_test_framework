import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH
import time

class Logger(logging.Logger):
    def __init__(self):
        super().__init__("")
        self.log_file_name = "test_case.log"
        #TODO 这里要去判断,如果没有该目录和文件的话,则需要开始创建开日志文件
        #TODO 这里的话,需要去获取脚本中的信息,然后用脚本信息中的case_ID作为日志名字,并且根据目录层级以及时间关系来创建目录
        self.backup_count = 5

        self.info_color = "\033[0;29m%s\033[0m"
        self.msg_color = "\033[0;36m%s\033[0m"
        self.warning_color = "\033[0;33m%s\033[0m"
        self.error_color = "\033[0;31m%s\033[0m"
        self.path_color = "\033[0;20m%s\033[0m"
        self.log_level_color = self.error_color

        self.formatter = self.update_logging_formatter()

        self.console_output_level = "INFO"
        self.file_output_level = "INFO"
        self.get_logger()  # 在初始化的时候,去创建控制台句柄和文件句柄



    def update_logging_formatter(self):
        return logging.Formatter(self.info_color % '%(asctime)s -' +
                                           self.path_color % ' %(pathname)s[line:%(lineno)d] - ' +
                                           self.log_level_color % '%(levelname)s: ' +
                                           self.msg_color % '%(message)s')

    def set_log_level(self, level):
        level = level.strip().upper()
        self.console_handler.setLevel(level)
        self.file_handler.setLevel(level)
        pass

    def mod_font_color_by_level(self, level):
        if level == "ERROR":
            self.log_level_color = self.error_color
        elif level == "WARNING":
            self.log_level_color = self.warning_color
        elif level == "INFO":
            self.log_level_color = self.info_color
        self.formatter = self.update_logging_formatter()
        self.console_handler.setFormatter(self.formatter)
        self.file_handler.setFormatter(self.formatter)


    def error(self, *msg):
        self.mod_font_color_by_level("ERROR")
        super().error(msg)
        pass

    def warning(self, *msg):
        self.mod_font_color_by_level("WARNING")
        super().warning(msg)


    def info(self, *msg):
        self.mod_font_color_by_level("INFO")
        super().info(msg)

    def get_logger(self):
        if not self.handlers:
            self.console_handler = logging.StreamHandler()
            self.console_handler.setFormatter(self.formatter)
            self.console_handler.setLevel(self.console_output_level)
            self.addHandler(self.console_handler)

            self.file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8')
            self.file_handler.setFormatter(self.formatter)
            self.file_handler.setLevel(self.file_output_level)
            self.addHandler(self.file_handler)

#测试代码
# log = Logger()
# log.info("这里我要打印一个info日志")
# log.warning("这里我要打印一个warning日志")
# log.error("这里我要打印一个error日志")
#
# log.set_log_level("WARNING")
# log.info("修改level为warning后,打印一个info日志")
# log.warning("修改level为warning后,打印一个warning日志")
# log.error("修改level为warning后,打印一个error日志")


