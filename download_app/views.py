from django.shortcuts import render

def page_download_app(request):
    return render(request, 'download_app/page_download_app.html')
