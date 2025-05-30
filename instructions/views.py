from django.shortcuts import render

def instructions(request):
    return render(request, 'instructions/instructions.html')