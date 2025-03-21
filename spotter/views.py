from django.http import HttpResponse
from django.shortcuts import render

cache = {'csale': 0, 'correct_value': 0, 'number_value': 0}

def index(request):
    if cache['csale'] != 0:
        cache['csale'] = 0
        cache['correct_value'] = 0
        cache['number_value'] = 0
        print(cache)

    print(request.GET, 'index')
    return render(request, 'spotter/index.html')

def  index_1(request):
    if cache['csale'] == 0:
        cache['csale'] = int(request.GET['csale'])
        print(cache, 'index_1 IF')
    else:
        cache['correct_value'] = 0
        print(cache, 'index_1 ELSE')

    print(request.GET, 'index_1')
    return render(request, 'spotter/index_1.html')

def  index_2(request):
    if cache['correct_value'] == 0:
        if request.GET['correct_value'] == '':
            cache['correct_value'] = 0
        else:
            cache['correct_value'] = int(request.GET['correct_value'])
        print(cache, 'index_2 IF')
    else:
        cache['number_value'] = 0
        print(cache, 'index_2 ELSE')

    print(request.GET, 'index_2')
    return render(request, 'spotter/index_2.html')

def  index_3(request):
    if cache['number_value'] == 0:
        if request.GET['number_value'] == '':
            cache['number_value'] = 0
        else:
            cache['number_value'] = int(request.GET['number_value'])
        print(cache, 'index_3 IF')
    else:
        pass

    print(request.GET, 'index_3')
    return render(request, 'spotter/index_3.html')
