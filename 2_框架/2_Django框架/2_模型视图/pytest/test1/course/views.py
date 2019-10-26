from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def set_cookie(request):
    response=HttpResponse('设置cookie')
    response.set_cookie('h1','zb')

    return response

def get_cookie(request):
    # a=request.COOKIES['h1']
    a=request.COOKIES.get('h1')
    request.session.clear()
    return HttpResponse(a)


def set_session(request):
    request.session['h2']='hello'
    request.session['h3']='hell'
    request.session['h4']='helo'
    request.session['h5']='hllo'
    return HttpResponse('设置好session')

def get_session(request):
    # a=request.session['h2']
    # a1=request.session['h3']
    a2=request.session['h4']
    a3=request.session['h5']
    print(a2,a3)
    return HttpResponse('haole')



def json1(request):
    return render(request,'booktest/json1.html')
def json2(request):
    print(type({'h1':'hello','h2':'world'}))
    return JsonResponse({'h1':'hello','h2':'world'})

# def show1(request):
#     return HttpResponse('show 1')


def show1(request,id):
    return HttpResponse('show %s'%id)


def show1(request,id1):
    return HttpResponse('show %s'%id1)


def method1(request):
    return render(request,'booktest/method1.html')
def method2(request):
    return HttpResponse(request.method)
def method3(request):
    return HttpResponse(request.method)



# 创建链接
def get1(request):
    return render(request,'booktest/get1.html')
# 接收一键一值

def get2(request):
    dict=request.GET
    a=dict.get('a')
    b=dict.get('b')
    c=dict.get('c','1')
    context={'a':a,'b':b,'c':c}
    return render(request,'booktest/get2.html',context)
# 接收一键多值
# 接收一键多值
def get3(request):
    dict=request.GET
    a=dict.getlist('a')
    b=dict.get('b')
    context={'a':a,'b':b}
    return render(request,'booktest/get3.html',context)


# 创建表单
def post1(request):
    return render(request,'booktest/post1.html')
# 接收表单请求的数据
# 接收表单请求的数据
def post2(request):
    dict=request.POST
    uname=dict.get('uname')
    upwd=dict.get('upwd')
    ugender=dict.get('ugender')
    uhobby=dict.getlist('uhobby')
    context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/post2.html',context)



#反向解析
def fan1(request):
    return render(request, 'booktest/fan1.html')
def fan2(request):
    return HttpResponse('fan2')

















