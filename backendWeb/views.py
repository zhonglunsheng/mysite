from django.shortcuts import render
from .models import LoginUser
# Create your views here.


def get_login(request):
    return render(request, 'login.html')


def login_form(request):
    # 查询所有
    record = LoginUser.objects.all()
    # 带条件查询
    record = LoginUser.objects.filter(user_name='zhonglunsheng')
    # 新增
    item = LoginUser()
    item.user_id = '1'
    item.user_name = 'tom'
    item.user_password = 'abcd1234'
    item.save()
    # 删除


    for item in record:
        print(item.user_name)
        # 删除
        item.delete()
    return render(request, 'login.html')
