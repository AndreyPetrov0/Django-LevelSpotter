from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateNewList

lst_res = {}

def index(request):
    print(request.GET, 'index')
    return render(request, 'spotter/index.html')

def  index_1(request):
    if request.method == "get":
        print('pass')
    else:
        # form = CreateNewList()
        lst_res['csale'] = request.GET['csale']
        print(lst_res)
        # print('2')

    print(request.GET, 'index_1')
    return render(request, 'spotter/index_1.html')
    # return render(request, 'spotter/index_1.html', {"form": form})

def  index_2(request):
    if request.method == "get":
        print('pass')
    else:
        # form = CreateNewList()
        lst_res['sameone'] = request.GET['sameone']
        print(lst_res)
        # print('2')

    print(request.GET, 'index_2')
    return render(request, 'spotter/index_2.html')

def  index_3(request):
    return render(request, 'spotter/index_3.html')
