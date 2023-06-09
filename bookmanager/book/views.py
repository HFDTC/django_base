from django.shortcuts import render

# Create your views here.
"""
视图
所谓视图就是 python 函数
视图函数有2个要求 :
    1. 视图函数的第一个参数就是接受请求 . 这个请求其实就是 HttpRequest 的类对象
    2. 必须返回一个响应
"""
# request
from django.http import HttpRequest
from django.http import HttpResponse


# 我们期望用户输入  http://127.0.0.1:8000/index/
# 来访问视图函数

def index(request):
    # return HttpResponse('ok')

    # render 渲染模板
    # 参数 : request , templates_name , context=None
    # request           请求
    # templates_name    模板名字
    # context=None

    # context 上下文 , 此处模拟数据查询
    context = {
        'name': '守护最好的坤坤'
    }

    return render(request, 'book/index.html', context=context)
