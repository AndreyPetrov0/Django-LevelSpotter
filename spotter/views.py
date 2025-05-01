from django.http import HttpResponse
from django.shortcuts import render
# from func_calc import test_func

cache = {'csale': 0, 'correct_value': 0, 'number_value': 0}

def func_calc(scale, correct, number):
    mg = 65535
    calc_correct = int(number) + (int(correct) * int(scale))
    if calc_correct < 0:
        return str(mg + calc_correct)
    if calc_correct > mg:
        return str(calc_correct - mg)
    else:
        return str(calc_correct)

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
            print(type(request.GET['correct_value']))
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

    function = {'func_calc': func_calc(cache['csale'], cache['correct_value'], cache['number_value'])}
    return render(request, 'spotter/index_3.html', context=function)

