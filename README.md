安装Django
```
$ sudo pip3 install Django==2.0.6
```

测试Django安装
我们可以在终端中测试Django是否安装成功。
```
$ python3
>>> import django
>>> print(django.get_version())
2.0.6
```

创建Django项目
```
django-admin startproject mysite
```

运行项目
```
python3 manage.py runserver
```

创建新的模块
```
python3 manage.py startapp lib
```

MTV流程
视图文件
```
# lib/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
```
本地模块映射
```
# lib/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

全局引入
```
# mysite/mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lib/', include('lib.urls')),
    path('admin/', admin.site.urls),
]
```
