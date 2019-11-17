>学习资料：[Django基础入门](https://www.shiyanlou.com/courses/1127)

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

Django的项目设置都包含在了mysite/mysite/settings.py中。
对于数据库，配置文件使用了SQLite作为默认的数据库文件。

记得配置设置文件中的TIME_ZONE为自己所在地的时区，中国地区为Asia/Shanghai。
TIME_ZONE = 'Asia/Shanghai'

创建模型
```
# lib/models.py
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

```

安装模型
将lib应用安装到我们项目中。
因为LibConfig类写在文件lib/apps.py中，所以它的路径为lib.apps.LibConfig
在设置文件中添加路径：
```
# mysite/mysite/settings.py
INSTALLED_APPS = [
    'lib.apps.LibConfig',
    'django.contrib.admin',
    ...
]
```
现在你的Django项目会包含lib应用。 运行下面的命令：
```
$ python3 manage.py makemigrations lib
```
让我们看看迁移命令会执行哪些SQL语句。
```
$ python3 manage.py sqlmigrate lib 0001
```
现在运行migrate命令，在数据库里创建新定义的模型的数据表：
```
$ python3 manage.py migrate 
```
使用API
```
>>>from lib.models import Book
>>>Book.objects.all()   #获取Book所有对象
<QuerySet []>
>>>from django.utils import timezone
>>>b = Book(name='Business', author='Tom', pub_house='First Press', pub_date=timezone.now())    #创建
>>>b.save() #保存
>>>b.id
1
>>>b.name
'Business'
>>>b.pub_date
datetime.datetime(2018, 7, 4, 2, 29, 7, 578323, tzinfo=<UTC>)
```