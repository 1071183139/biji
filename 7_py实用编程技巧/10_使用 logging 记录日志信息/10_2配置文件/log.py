import logging
from logging import config
# 读取日志配置文件内容
logging.config.fileConfig('logging.ini')

# 创建一个日志器logger
logger = logging.getLogger('root')

# 日志输出
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')