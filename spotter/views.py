from django.http import HttpResponse
from django.shortcuts import render

lst_res = {'csale': 0, 'correct_value': 0, 'number_value': 0}

def index(request):
    if lst_res['csale'] != 0:
        lst_res['csale'] = 0
        lst_res['correct_value'] = 0
        lst_res['number_value'] = 0
        print(lst_res)

    print(request.GET, 'index')
    return render(request, 'spotter/index.html')

def  index_1(request):
    if lst_res['csale'] == 0:
        lst_res['csale'] = int(request.GET['csale'])
        print(lst_res, 'index_1 IF')
    else:
        lst_res['correct_value'] = 0
        print(lst_res, 'index_1 ELSE')

    print(request.GET, 'index_1')
    return render(request, 'spotter/index_1.html')

def  index_2(request):
    if lst_res['correct_value'] == 0:
        if request.GET['correct_value'] == '':
            lst_res['correct_value'] = 0
        else:
            lst_res['correct_value'] = int(request.GET['correct_value'])
        print(lst_res, 'index_2 IF')
    else:
        lst_res['number_value'] = 0
        print(lst_res, 'index_2 ELSE')

    print(request.GET, 'index_2')
    return render(request, 'spotter/index_2.html')

def  index_3(request):
    if lst_res['number_value'] == 0:
        if request.GET['number_value'] == '':
            lst_res['number_value'] = 0
        else:
            lst_res['number_value'] = int(request.GET['number_value'])
        print(lst_res, 'index_3 IF')
    else:
        pass

    print(request.GET, 'index_3')
    return render(request, 'spotter/index_3.html')
