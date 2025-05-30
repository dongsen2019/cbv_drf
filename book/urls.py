"""
URL configuration for CBV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views

from django.urls import include

urlpatterns = [
    path('', views.BookView.as_view()),

]

'''
django的原生View源码解析

path('', views.BookView.as_view()) ==> path('', View.view)

# 一旦用户访问book,比如get请求访问/book/

get 请求访问/book/ => view()  => return dispatch() => return get()
post 请求访问/book/ => view()  => return dispatch() => return post()
!!!
1.在FBV中返回的是 视图函数 的返回值
2.而在CBV中先用as_view()方法返回一个名为view的函数名,等价于FBV中的 视图函数的函数名 比如index

-------------------
class BookView(View):    -->BookView继承自View
    def get(self, request):
        return HttpResponse("这是一个get请求")

    def post(self, request):
        return HttpResponse("这是一个post请求")

    def delete(self, request):
        return HttpResponse("这是一个delete请求")
        
class View:

    @classonlymethod  -->这是一个类方法,仅供类调用
    def as_view(cls,...)  而谁调用了这个类方法,cls就是那个类 
        def view():
            #cls: BookView
            self = cls() 先用 BookView 做了一个实例化赋值给self
            return self.dispatch(request, *args, **kwargs) # view函数return的是dispatch方法函数
            
        return view
    
    def dispatch(self, request, *args, **kwargs):
    
        if request.method.lower() in self.http_method_names:
            handler = getattr(
                self, request.method.lower(), self.http_method_not_allowed
            )  # handler = self.get 如果是发送的 get 请求
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs) # 等价于 self.get(request,...)
'''


'''
# DRF的APIView源码解析

class BookView(APIView):
    def get(self, request):
        return HttpResponse("这是一个 APIView get请求")

    def post(self, request):
        return HttpResponse("这是一个 APIView post请求")

    def delete(self, request):
        return HttpResponse("这是一个 APIView delete请求")
        

class APIView:

    def as_view(cls):
        view = super().as_view()
        
        return view
        
    def dispatch(self, request, *args, **kwargs):
        # 构建新的request对象
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        # 初始化: 认证 权限 限流组件三件套
        self.initial(request, *args, **kwargs)
        
        #分发逻辑
        handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs) # 等价于 self.get(request,...)
        
    
class View:

    @classonlymethod  -->这是一个类方法,仅供类调用
    def as_view(cls,...)  而谁调用了这个类方法,cls就是那个类 
        def view():
            #cls: BookView
            self = cls() 先用 BookView 做了一个实例化赋值给self
            return self.dispatch(request, *args, **kwargs) # view函数return的是dispatch方法函数
            
        return view
    
    def dispatch(self, request, *args, **kwargs):
    
        if request.method.lower() in self.http_method_names:
            handler = getattr(
                self, request.method.lower(), self.http_method_not_allowed
            )  # handler = self.get 如果是发送的 get 请求
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs) # 等价于 self.get(request,...)



path('', views.BookView.as_view()) ==> path('', View.view)

# 一旦用户访问book,比如get请求
get 请求访问/book/ => APIView.as_view() => View.view()  => return dispatch() => return get()
post 请求访问/book/ => APIView.as_view() => View.view()  => return dispatch() => return post()

'''


'''
"contentType: urlencoded \r\n\r\na=1&b=2  原生django的request.POST 针对的是urlencoded数据"
'contentTyoe: json \r\n\r\n{"a":1,"b":2}' 原生django的request.POST 无法解析json数据'
'''
