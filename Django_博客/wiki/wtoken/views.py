import datetime
import hashlib
import json
import time

import jwt

from user.models import Userprofile

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def tokens(request):

    if request.method != 'POST':
        result = {'code':20101,'error':'Please use POST'}
        return JsonResponse(result)

    json_str = request.body
    #TODO 检查参数是否存在
    json_obj = json.loads(json_str)
    username = json_obj.get('username')
    password = json_obj.get('password')
    # 找用户
    users = Userprofile.objects.filter(username = username)
    if not users:
        result = {'code':20102,'error':'The username or error'}
        return JsonResponse(result)
    user = users[0]

    pm = hashlib.md5()
    pm.update(password.encode())

    if user.password != pm.hexdigest():
        result = {'code':20103,'error':'The username or password is '}
        return JsonResponse(result)

    # 生成token
    now_datetime = datetime.datetime.now()
    user.login_time = now_datetime
    user.save()

    token = make_token(username,3600*24,str(now_datetime))
    result = {'code':200,'username':username,'data':{'token':token.decode()}}


    return JsonResponse(result)




def make_token(username,exp,now_datetime):
    # 生成token
    key = '12345678ABC'
    now_t = time.time()
    payload = {'username':username,'exp':int(now_t+exp),'login_time':str(now_datetime)}
    return jwt.encode(payload,key,algorithm='HS256')






