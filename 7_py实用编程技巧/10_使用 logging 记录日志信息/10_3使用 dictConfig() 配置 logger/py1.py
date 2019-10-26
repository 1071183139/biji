import logging
from logging import config


from dict_config import LOGGING_DIC


logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
logger = logging.getLogger('zhang')
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10, 'log')