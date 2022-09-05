from django.shortcuts import render
from .models import AboutMe

# Create your views here.

def HomePage(request):
    try:
        aboutMe = get_object_or_404(AboutMe)
    except:
        aboutMe = AboutMe.objects.latest('id') # if two or more data in databse then last data find out 
    data={
        "aboutme":aboutMe,
    }

    return render(request,'mainapp/index.html',data)

def ContactPage(request):
    return render(request,'mainapp/about_me.html')
    