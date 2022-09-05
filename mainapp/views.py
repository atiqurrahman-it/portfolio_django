from django.shortcuts import render
from .models import AboutMe,Skills,TESTIMONIALS,Counts

# Create your views here.

def HomePage(request):
    try:
        aboutMe = get_object_or_404(AboutMe)
    except:
        aboutMe = AboutMe.objects.latest('id') # if two or more data in databse then last data find out 

    try:
        count = get_object_or_404(Counts)
    except:
        count = Counts.objects.latest('id') # if two or more data in databse then last data find out 

    skill = Skills.objects.all().order_by('-id')[:6]
    testimonial=TESTIMONIALS .objects.all().order_by('-id')
    data={
        "aboutme":aboutMe,
        "count":count,
        "skills":skill,
        "testimonials":testimonial,
    }

    return render(request,'mainapp/index.html',data)

def ContactPage(request):
    return render(request,'mainapp/about_me.html')
    