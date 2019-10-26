BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TIMEZONE = 'Asia/Shanghai' # 指定时区

# 导入指定模块

CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'

)

from datetime import timedelta
from celery.schedules import crontab

# 配置定时任务列表
CELERYBEAT_SCHEDULE = {

    "task1": {
        "task": "celery_app.task1.add",
        "schedule": timedelta(seconds=3),  # 每3S执行一次
        'args': (2, 8)
    },
    "task2": {
        "task": "celery_app.task2.multiply",
        "schedule": crontab(hour=23, minute=33),  # 每天23:33执行
        'args': (4, 5)
    }
}