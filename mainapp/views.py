from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request,'mainapp/index.html')

def ContactPage(request):
    return render(request,'mainapp/about_me.html')
    