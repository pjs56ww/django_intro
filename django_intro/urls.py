"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# django_intro/urls.py
from django.contrib import admin
from django.urls import path
from pages import views


# django 의 목차를 생성하는 곳
# ex) www.ssafy.com/admin/ => 성공
# ex) www.ssafy.com/login/ => 페이지 없음 => 404 not found
# 사용자가 들어올 경로를 설정해주는 것
urlpatterns = [ # 작성하고자 하는 path를 위부터 작성
    # path('사용자가 접속하는 경로', )
    path('static_example/', views.static_example),

    path('lotto_result/', views.lotto_result),
    path('lotto_pick/', views.lotto_pick),

    path('result/', views.result),
    path('search/', views.search),

    path('lotto/', views.lotto),
    
    path('isitBirthday/', views.isitBirthday),
    path('student/<str:name>/', views.student),
    path('info/', views.info),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
# view, url, page.html 3가지가 맵핑이 되어야 한다.

#localhost: 8000/introduce/
# introduce => render => introduce.html


# path: image/
# template: image.html
# view: def image(request):
# imege url을 context에 담아서 image.html 에 전달한다.

# template: image.html // 전달받은 image.url을 img 태그 src 속성에 담아서 랜덤 이미지를 보여준다.


# url: times/
# Variable routing 으로 숫자 2개를 각각 'num1', 'num2' 이름으로 받는다.
# view: 두 숫자를 곱한 result 변수와, num1, num2를 context 에 담아서 times.html 에 전달한다.
