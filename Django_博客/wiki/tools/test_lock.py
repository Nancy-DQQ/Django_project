"""
模拟30个请求
发给:http://127.0.0.1:8000/test/
    http://127.0.0.1:8000/test/
"""


# 线程事件函数 - 随机向8000或8001发请求
import random

# 请求模块
from threading import Thread

import requests


def get_request():
    url = "http://127.0.0.1:8000/test/"
    url2 = "http://127.0.0.1:8001/test/"
    get_url = random.choice([url,url2])
    # 真正发请求
    html = requests.get(get_url).text
    print(html)

t_list = []
for i in range(30):
    t = Thread(target=get_request)
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()









