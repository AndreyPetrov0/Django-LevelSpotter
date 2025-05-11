from django.shortcuts import render

def page_start(request):
    return render(request, 'start_page/page_start.html')
