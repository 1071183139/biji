#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import BookInfo,HeroInfo
from datetime import date
from django.db.models import F,Q
from django.db.models import Sum
#查询所有图书并显示


def index(request):

    # list = BookInfo.objects.all()
    # return render(request, 'booktest/index.html', {'list': list})

    #1 限制查询集
    # list=BookInfo.objects.all()[0:2]
    # return render(request, 'booktest/index.html', {'list': list})

    #2 exact：表示判等
    # list=BookInfo.objects.filter(id__exact=4)
    # 简写
    # list = BookInfo.objects.filter(id=1)
    # return render(request, 'booktest/index.html', {'list': list})



    #基本查询

    # 3 contains：是否包含
    # 查询书名包含‘传’的图书
    # list=BookInfo.objects.filter(btitle__contains='传')
    # return render(request, 'booktest/index.html', {'list': list})

    #4 startswith、endswith：以指定值开头或结尾
    # 查询书名以‘部’结尾的图书
    # list=BookInfo.objects.filter(btitle__endswith='部')
    # return render(request, 'booktest/index.html', {'list': list})

    #5 isnull：是否为null
    # 查询书名不为空的图书
    # list=BookInfo.objects.filter(btitle__isnull=False)
    # return render(request,'booktest/index.html',{'list':list})

    #6  in ：是否包含在范围内
    # 查询编号为1或3或5的图书
    # list=BookInfo.objects.filter(pk__in=[1,3])
    # return render(request,'booktest/index.html',{'list':list})

    #7 gt、gte、lt、lte：大于、大于等于、小于、小于等于
    # 查询编号大于3的图书
    # list=BookInfo.objects.filter(id__gt=3)
    # return render(request,'booktest/index.html',{'list':list})

    #8 不等于使用等于的运算符，使用exclude()过滤器
    # 例：查询编号不等于3的图书
    # list=BookInfo.objects.exclude(id=3)
    # return render(request,'booktest/index.html',{'list':list})

    #9 year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算
    # 查询1980年发表的图书
    # list=BookInfo.objects.filter(bpub_date__year=1980)
    # return render(request,'booktest/index.html',{'list':list})

    #10 查询1980年1月1日后发表的图书
    # list=BookInfo.objects.filter(bpub_date__gt=date(1980,5,1))
    # return render(request,'booktest/index.html',{'list':list})

    #11 F对象 两个对象之间的比较
    # 查询阅读量大于等于评论量的图书
    # list=BookInfo.objects.filter(bread__gt=F('bcommet'))
    # return render(request,'booktest/index.html',{'list':list})

    # 查询阅读量大于2倍评论量的图书
    # list = BookInfo.objects.filter(bread__gt=F('bcommet')*2)
    # return render(request, 'booktest/index.html', {'list': list})

    # 11逻辑关系（Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或）
    # 逻辑与  ，
    # 查询阅读量大于20，并且编号小于3的图书
    # list=BookInfo.objects.filter(bcommet__gt=20,id__lt=3)
    # list=BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))

    # return render(request, 'booktest/index.html', {'list': list})

    # Q(属性名__运算符=值)
    # 逻辑或
    # 查询阅读量大于20，或编号小于3的图书

    # list = BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3))
    return render(request, 'booktest/index.html', {'list': list})

    # 逻辑非
    # 查询编号不等于3的图书
    # list=BookInfo.objects.filter(~Q(id=3))

    #第二种方法
    # list=BookInfo.objects.exclude(id=2)
    # return render(request, 'booktest/index.html', {'list': list})



    # 关联查询
    # 关联模型类名小写__属性名__运算符 = 值
    # 查询图书，要求图书中英雄的描述包含‘八’

    # list=BookInfo.objects.filter(heroinfo__hcontent__contains='六')
    # return render(request, 'booktest/index.html', {'list': list})

    # heros=HeroInfo.objects.get(hcontent='降龙十八掌')[0,1]
    # list=heros.hbook()
    # return render(request, 'booktest/index.html', {'list': list})


    # 查询书名为“天龙八部”的所有英雄
    # list=HeroInfo.objects.filter(hbook__btitle='天龙八部')
    # return render(request, 'booktest/index.html', {'list': list})


    # 聚合函数
    # 使用aggregate()过滤器调用聚合函数
    # 聚合函数包括：Avg，Count，Max，Min，Sum，被定义在django.db.models中
    # 例：查询图书的总阅读量
    # list = BookInfo.objects.aggregate(Sum('bread'))
    # print(list)
    # return HttpResponse(list['bread__sum'])

    # 查询图书总数
    # list=BookInfo.objects.count()
    # print(list)
    # return HttpResponse(list)

    # 关联的查询
    # 查询编号为1的图书
    # book=BookInfo.objects.get(id=1)
    # 获得book图书的所有英雄(一找多)
    # heros=book.heroinfo_set.all()
    # print(heros)
    # return HttpResponse(heros)


    # 获得编号为1的英雄
    # hero = HeroInfo.objects.get(id=1)
    # # 查询英雄对应的书(多找一)
    # book = hero.hbook
    # print(book.btitle)
    # return HttpResponse(book)

#创建新图书
def create(request):
    # book=BookInfo.objects.create('流星蝴蝶剑')
    book = BookInfo.objects.create('流星蝴蝶剑', date(1995,12,30))
    book.save()
    #转向到首页
    return redirect('/')

#逻辑删除指定编号的图书
def delete(request,id):
    print(id)
    book=BookInfo.objects.get(pk=int(id))
    book.isDelete=True
    book.save()
    #转向到首页
    return redirect('/')











