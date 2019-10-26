#coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader,RequestContext

from booktest.models import BookInfo


def index(request):
    return HttpResponse("index")

def index1(request):
    # 1.获取模板
    template=loader.get_template('booktest/index.html')
    # 2.定义上下文
    context=RequestContext(request,{'title':'图书列表','list':range(10)})
    # 3.渲染模板
    return HttpResponse(template.render(context))

def index2(request):
    context={'title':'图书列表','list':range(5)}
    return render(request,'booktest/index.html',context)


#首页，展示所有图书
def index3(reqeust):
    #查询所有图书
    booklist = BookInfo.objects.all()
    #将图书列表传递到模板中，然后渲染模板
    return render(reqeust, 'booktest/index.html', {'booklist': booklist})

#详细页，接收图书的编号，根据编号查询，再通过关系找到本图书的所有英雄并展示
def detail(reqeust, id):
    #根据图书编号对应图书
    book = BookInfo.objects.get(pk=id)
    #将图书信息传递到模板中，然后渲染模板
    return render(reqeust, 'booktest/detail.html', {'book': book})