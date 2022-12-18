from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'ambal.html')

def index3(request):
    return render(request,'evan_gravin.html')

def index4(request):
    return render(request,'tpehep.html')

def index5(request):
    return render(request,'wtonop.html')