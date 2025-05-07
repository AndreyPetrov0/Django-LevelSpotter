from django.shortcuts import render

def index(request):
    return render(request, 'download_app/index.html')
