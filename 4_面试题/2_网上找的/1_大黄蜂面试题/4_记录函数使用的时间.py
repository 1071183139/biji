# import time
#
#
# def log_time(func):
#     def log():
#         beg=time.time()
#         func()
#         res=time.time()-beg
#         return res
#     return log
#
# @log_time #@装饰器的语法糖
# def mysleep():
#     time.sleep(1)
#
# print(mysleep())

# import time
#
# #如何使用类编写装饰器
# class Log_time:
#     def __call__(self, func):
#         def log():
#             beg=time.time()
#             func()
#             res=time.time()-beg
#             return res
#         return log
#
# @Log_time() #@装饰器的语法糖
# def mysleep():
#     time.sleep(1)
#
# print(mysleep())




import time

#如何给装饰器传递参数（使用类装饰器比较方便）
class Log_time:
    def __init__(self,use_time=False):
        self.use_time=use_time


    def __call__(self, func):
        def log():
            beg=time.time()
            func()
            res=time.time()-beg
            if self.use_time:
                return int(res)
            else:
                return res
        return log

@Log_time(True) #@装饰器的语法糖
def mysleep():
    time.sleep(1)

print(mysleep())