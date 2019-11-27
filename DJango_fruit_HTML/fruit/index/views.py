import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    return render(request, 'index.html')

def check_login(request):
    #检查登录状态
    #1 检查session
    #2 如果session没有数据，则检查Cookie
    #3-1 如果Cookie有，需要把Cookie数据回写给session
    #3-2 如果Cookie没有，用户肯定没登录

    #未登录返回结构
    #res = {'loginState':0}
    #登录状态返回
    res = {'loginState':1, 'username':'guoxiaonao'}
    return JsonResponse(res)

def load_goods(request):
    #加载商品
    #[{'type':{'title':'热带水果'},'goods':[{},]}..]
    all_list = []
    all_types = GoodsType.objects.all()
    for _type in all_types:
        data = {}
        data['type'] = {'title': _type.title}
        data['goods'] = []
        all_goods = _type.goods_set.filter(isActive=True).order_by('-created_time')[:10]
        for good in all_goods:
            d = {}
            d['title'] = good.title
            d['price'] = str(good.price)
            d['spec'] = good.spec
            #good.picture 是个 Django 的image 对象
            d['picture'] = str(good.picture)
            data['goods'].append(d)
        all_list.append(data)

    return HttpResponse(json.dumps(all_list),content_type='application/json')







