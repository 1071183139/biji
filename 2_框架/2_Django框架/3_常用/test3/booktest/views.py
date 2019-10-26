from django.shortcuts import render
from django.http import HttpResponse

from booktest.models import PicTest


def jingtai(request):
    return render(request,'booktest/jingtai.html')

def index(request):
    print('======index======')
    # raise Exception('自定义异常')
    return render(request,'booktest/index.html')
    # return HttpResponse('ahsfkgksgfk')


def pic_upload(request):
    return render(request,'booktest/pic_upload.html')


from django.core.files.storage import FileSystemStorage

def pic_handle(request):
    f1=request.FILES.get('pic')

    f2=FileSystemStorage()
    r=f2.save('booktest/%s'%(f1.name),f1)#返回文件名，如果文件名存在则会创建一个不重复的名称

    p1=PicTest()
    p1.pic=r
    p1.save()

    return HttpResponse('OK')

def pic_show(request):
    pic=PicTest.objects.get(pk=1)
    context={'pic':pic}
    return render(request,'booktest/pic_show.html',context)




def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    title=request.POST.get('title')
    return HttpResponse(title)