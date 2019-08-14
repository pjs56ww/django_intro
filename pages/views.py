# pages/views.py
from django.shortcuts import render
import random

# Create your views here.

# 중요!!

# 작업들이 실제로 작동하는 함수들을 작성하는 곳

# url 과 view 함수가 연동이 될 것이다.

def index(request): # 보통 page 이름과 맞추는 편
    # 요청이 들어오면 templates 의 'index.html'을 보여준다.
    # 첫 번째 인자는 반드시 request 가 온다. => 사용자가 보내는 요청에 대한 정보
    return render(request, 'index.html') # render의 첫번째 인자도 반드시 request가 들어간다.


def introduce(request):
    return render(request, 'introduce.html')


# Template Variable Example
def dinner(request):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }
    # Django template 으로 context 전달
    return render(request, 'dinner.html', context)
    