LOGGING_DIC = {
    'version': 1,
    # 禁用已经存在的logger实例
    'disable_existing_loggers': False,
    # 定义日志 格式化的 工具
    'formatters': {
        'simple': {
            'format': '[%(levelname)s][%(asctime)s] %(message)s'
        }
    },
    'handlers': {
        #打印到终端的日志
        'stream': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'access': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'simple',
            'filename': 'access.log',       # 日志文件路径
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        }
    },
    # logger实例
    'loggers': {
        # 默认的logger应用如下配置
        'zhang': {
            'handlers': ['stream', 'access'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        }
    },
}