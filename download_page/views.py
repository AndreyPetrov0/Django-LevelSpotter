from django.shortcuts import render

def page_download(request):
    return render(request, 'download_page/page_download.html')
