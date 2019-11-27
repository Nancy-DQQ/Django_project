from django.http import JsonResponse
from user.models import Userprofile
import redis

def test(request):

    r = redis.Redis(host="127.0.0.1",port=6379,db=0,password=123456)
    while True:
        try:
            with r.lock('guoxiaonao',blocking_timeout=3) as lock:

                # 对score字段进行 +1 操作
                u = Userprofile.objects.get(username = 'guoxiaonao')
                u.score += 1
                u.save()
            break

        except Exception as e:
            print('lock failed')


    return JsonResponse({'code':200,'data':{}})


# 麻花 火锅料