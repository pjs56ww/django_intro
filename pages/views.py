# pages/views.py
from django.shortcuts import render
from datetime import datetime
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

# practice
# Template Variable Example
# Variable routing 으로 'name' 을 받아서 context 에 'name' 도 함께 넣는다.
# dinner.html 에서 'name' 님의 저녁식사는 'pick'입니다. 가 출력될 수 있도록
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name,
    }
    # Django template 으로 context 전달
    return render(request, 'dinner.html', context)

def image(request):
    rnd_img = 'https://picsum.photos/1000'
    context = {
        'rnd_img': rnd_img,
    }
    return render(request, 'image.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)

def times(request, num1, num2):
    result = num1 * num2
    context = {
        'result': result,
        'num1': num1,
        'num2': num2,
    }
    return render(request, 'times.html', context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python.'
    messages = ['apple', 'banana', 'mango', 'cucumber']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)


def info(request):

    return render(request, 'info.html')


def student(request, name):
    context = {
        'name': name
    }
    return render(request, 'student.html', context)    


def isitBirthday(request):
    return render(request, 'isitBirthday.html', context)


def lotto(request):
    real_lotto = [21, 25, 30, 32, 40 ,42]
    lotto = []
    for i in range(6):
        lotto = lotto + [random.randrange(1, 46)]
    lotto = sorted(lotto)
    context = {
        'real_lotto': real_lotto,
        'lotto': lotto,
    }

    return render(request, 'lotto.html', context)


def search(request):
    return render(request, 'search.html')


def result(request):
    query = request.GET.get('query')
    category = request.GET.get('categories')
    context = {
        'query': query,
        'category': category
    }
    return render(request, 'result.html', context)


def lotto_pick(request):
    
    return render(request, 'lotto_pick.html')

def lotto_result(request):
    lotto_num = list(map(int, request.GET.get('lotto_number').split()))
    lotto_870 = [21, 25, 30, 32, 40, 42]
    cnt = 7
    for i in lotto_num:
        if i in lotto_870:
            cnt -= 1

    
    context = {
        'lotto_num': lotto_num,
        'lotto_870': lotto_870,
        'rank': cnt,
    }
    return render(request, 'lotto_result.html', context)


def static_example(request):
    return render(request, 'static_example.html')
