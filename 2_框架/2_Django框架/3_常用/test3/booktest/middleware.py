#coding=utf-8
from django.http import HttpResponse

class my_mid:
    def __init__(self):
        print('--------------init')

    # 处理请求前：在每个请求上调用，返回None或HttpResponse对象
    def process_request(self,request):
        print('--------------request')

    # 处理视图前：在每个请求上调用，返回None或HttpResponse对象
    def process_view(self,request, view_func, view_args, view_kwargs):
        print('--------------view')

    # 处理模板响应前：在每个请求上调用，返回实现了render方法的响应对象
    def process_template_response(self,request, response):
        print('--------------template')
        return response

    # .处理响应后：所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
    def process_response(self,request, response):
        print('--------------response')
        return response

class exp1:
    # 异常处理：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象
    #先注册的后调用
    def process_exception(self,request,exception):
        print('--------------exp1')
class exp2:
    def process_exception(self,request,exception):
        print('--------------exp2')